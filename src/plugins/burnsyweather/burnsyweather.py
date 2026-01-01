from plugins.base_plugin.base_plugin import BasePlugin
from utils.app_utils import resolve_path
from plugins.burnsyweather.WeatherGetter import WeatherGetter

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
        image_template_params = self.parse_weather_data(settings)

        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]
        
        image = self.render_image(dimensions, "burnsyweather.html", "burnsyweather.css", image_template_params)

        return image

    

    def parse_weather_data(self, settings):
        # Get Weather Data
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
        icon_set = 'old'

        location_of_forecast = str(weather_data.features[0].geometry.coordinates[0]) +", " + str(weather_data.features[0].geometry.coordinates[1])
        model_run_date = weather_data.features[0].properties.modelRunDate
        hour_one_weather_symbol = self.get_plugin_dir(f'icons/{icon_set}/{weather_data.features[0].properties.timeSeries[0].significantWeatherCode}.svg')
        

        # Prepare Template Params
        image_template_params = {
            "title": 'MetOffice Weather',
            "location_of_forecast": location_of_forecast,
            "model_run_time": model_run_date,
            "hour_one_weather_symbol": hour_one_weather_symbol,
            "met_office_logo": self.get_plugin_dir('icons/Met_Office.png'),
            "plugin_settings": settings
        }
        return image_template_params 
   