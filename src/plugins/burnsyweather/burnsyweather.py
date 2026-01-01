from plugins.base_plugin.base_plugin import BasePlugin
from utils.app_utils import resolve_path
from plugins.burnsyweather.Services.WeatherGetter import WeatherGetter
from plugins.burnsyweather.Services.GlobalSpotLocationHoursAdaptor import GlobalSpotLocationHoursAdaptor

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
        # Get Weather Data - this bit may move into GlobalSpotLocationHoursAdaptor if that's the only class that consumes it
        try: 
            lat = float(settings.get('latitude'))
            long = float(settings.get('longitude'))
            if not lat or not long:
                raise RuntimeError("Latitude and Longitude are required.")
            
            weather_getter = WeatherGetter()
            weather_data =  weather_getter.get_content(lat, long)
        except Exception as e:
            logger.error("Error getting weather content: %s", e)
            raise RuntimeError("Error retrieving weather data, please check logs.")

        # Adapt Weather Data
        global_spot_location_hours = GlobalSpotLocationHoursAdaptor().get_spot_hourly_forecast(weather_data, self.get_plugin_dir())

        # Prepare Additional Params
        standard_params = self.prepare_standard_params(settings, weather_data)

        # Combine Params
        image_template_params = standard_params | global_spot_location_hours

        return image_template_params 




    def prepare_standard_params(self, settings, weather_data):
        icon_set = 'old'
        hour_one_weather_symbol = self.get_plugin_dir(f'icons/{icon_set}/{weather_data.features[0].properties.timeSeries[0].significantWeatherCode}.svg')
        location_of_forecast = str(weather_data.features[0].geometry.coordinates[0]) +", " + str(weather_data.features[0].geometry.coordinates[1])
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
   