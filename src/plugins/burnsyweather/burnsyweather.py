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

    def get_content(self, settings):
        lat = float(settings.get('latitude'))
        long = float(settings.get('longitude'))
        if not lat or not long:
            raise RuntimeError("Latitude and Longitude are required.")
        
        weather_getter = WeatherGetter()
        return weather_getter.get_content(lat, long)

    def parse_weather_data(self, settings):
        try: 
            weather_data = self.get_content(settings)
        except Exception as e:
            logger.error("Error getting weather content: %s", e)
            raise RuntimeError("Error retrieving weather data, please check logs.")

        icon_set = 'old'

        print(f'icons/{icon_set}/{weather_data.features[0].properties.timeSeries[0].significantWeatherCode}.svg')

        image_template_params = {
            "title": 'MetOffice Weather',
            "model_run_time": weather_data.features[0].properties.modelRunDate,
            "hour_one_weather_symbol": self.get_plugin_dir(f'icons/{icon_set}/{weather_data.features[0].properties.timeSeries[0].significantWeatherCode}.svg'),
            "met_office_logo": self.get_plugin_dir('icons/Met_Office.png'),
            "plugin_settings": settings
        }

        return image_template_params 
    
    # def generate_settings_template(self):
    #     template_params = super().generate_settings_template()
    #     template_params['api_key'] = {
    #         "required": True,
    #         "service": "OpenAI",
    #         "expected_key": "OPEN_AI_SECRET"
    #     }
    #     template_params['style_settings'] = True
    #     return template_params
