from plugins.base_plugin.base_plugin import BasePlugin
from utils.app_utils import resolve_path
from plugins.burnsyweather.Services.WeatherGetter import WeatherGetter
from plugins.burnsyweather.Services.GlobalSpotLocationHoursAdaptor import GlobalSpotLocationHoursAdaptor
from plugins.burnsyweather.Services.GlobalSpotLocationDailyAdaptor import GlobalSpotLocationDailyAdaptor
from plugins.burnsyweather.Services.ObservationAdaptor import ObservationAdaptor
from plugins.burnsyweather.Models.MetOffice.SiteSpecificHourly import *
from plugins.burnsyweather.Models.MetOffice.SiteSpecificDaily import *

# from PIL import Image, ImageDraw, ImageFont
from utils.image_utils import resize_image
from io import BytesIO
from datetime import datetime
import requests
import logging
import textwrap
import os

logger = logging.getLogger(__name__)

class BurnsyWeather(BasePlugin):

    def generate_image(self, settings, device_config):
        image_template_params = self.create_weather_tokens(settings)

        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]
        
        image = self.render_image(dimensions, "burnsyweather.html", "burnsyweather.css", image_template_params)

        return image

    

    def create_weather_tokens(self, settings):
        # Get Weather Data - this bit may move into the Adaptors
        try: 
            lat = float(settings.get('latitude'))
            long = float(settings.get('longitude'))
            if not lat or not long:
                raise RuntimeError("Latitude and Longitude are required.")
            
            weather_getter = WeatherGetter()


            raw_weather_data_hourly =  weather_getter.get_content(lat, long, "hourly")
            jsonstring = json.loads(raw_weather_data_hourly)
            weather_data_hourly = HourlyRoot.from_dict(jsonstring)

            raw_weather_data_daily =  weather_getter.get_content(lat, long, "daily")
            jsonstring_daily = json.loads(raw_weather_data_daily)
            weather_data_daily = DailyRoot.from_dict(jsonstring_daily)


        except Exception as e:
            logger.error("Error getting weather content: %s", e)
            raise RuntimeError("Error retrieving weather data, please check logs.")

        # Adapt Weather Data
        global_spot_location_hours = GlobalSpotLocationHoursAdaptor().get_spot_hourly_forecast(weather_data_hourly, self.get_plugin_dir())
        global_spot_location_daily = GlobalSpotLocationDailyAdaptor().get_spot_daily_forecast(self.get_plugin_dir(), lat, long)
        observation_params = ObservationAdaptor().get_observation_params(lat, long)

        # Prepare Additional Params
        standard_params = self.prepare_standard_params(settings, weather_data_hourly)

        # Combine Params
        image_template_params = standard_params | global_spot_location_hours | global_spot_location_daily | observation_params

        return image_template_params 


    def prepare_standard_params(self, settings, weather_data):
        icon_set = 'old'
        hour_one_weather_symbol = self.get_plugin_dir(f'icons/{icon_set}/{weather_data.features[0].properties.timeSeries[0].significantWeatherCode}.svg')
        coords = weather_data.features[0].geometry.coordinates
        lon = float(coords[0])
        lat = float(coords[1])

        location_of_forecast = self.get_city_from_coords(lat, lon)

        model_run_date = weather_data.features[0].properties.modelRunDate
        
        basic_params = {
            "title": 'MetOffice Weather',
            "location_of_forecast": location_of_forecast,
            "model_run_time": model_run_date,
            "hour_one_weather_symbol": hour_one_weather_symbol,
            "met_office_logo": self.get_plugin_dir('icons/Met_Office.png'),
            "plugin_settings": settings
        }
        
        return basic_params
    
    def get_city_from_coords(self, lat, lon):
        # Default to coordinate pair; attempt reverse geocode to get a friendly place name
        location_of_forecast = f"{lat}, {lon}"
        try:
            resp = requests.get(
                "https://nominatim.openstreetmap.org/reverse",
                params={"lat": lat, "lon": lon, "format": "jsonv2", "addressdetails": 1},
                headers={"User-Agent": "InkyPi-weather"},
                timeout=5,
            )
            resp.raise_for_status()
            data = resp.json()
            addr = data.get("address", {}) or {}
            # Prefer specific place names (city/town/village/hamlet/municipality)
            for key in ("city", "town", "village", "hamlet", "municipality"):
                name = addr.get(key)
                if name:
                    return name
            # Fallback to broader area (county/state/country)
            for key in ("county", "state", "country"):
                name = addr.get(key)
                if name:
                    return name
            # No suitable name found; keep coords as text
            return location_of_forecast
        except Exception as e:
            logger.warning("Reverse geocode failed: %s", e)
            return location_of_forecast