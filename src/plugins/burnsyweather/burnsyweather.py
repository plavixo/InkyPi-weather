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
        
        # api_key = device_config.load_env_key("OPEN_AI_SECRET")
        # if not api_key:
        #     raise RuntimeError("OPEN AI API Key not configured.")

        title = settings.get("title")
        if not title:
            raise RuntimeError("Title is required.")

        content = self.get_content()

        image_template_params = {
            "title": title,
            "content": content,
            "plugin_settings": settings
        }

        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]
        
        image = self.render_image(dimensions, "burnsyweather.html", "burnsyweather.css", image_template_params)

        return image

    def get_content(self):
        weather_getter = WeatherGetter()
        return weather_getter.get_content()
        
    
    # def generate_settings_template(self):
    #     template_params = super().generate_settings_template()
    #     template_params['api_key'] = {
    #         "required": True,
    #         "service": "OpenAI",
    #         "expected_key": "OPEN_AI_SECRET"
    #     }
    #     template_params['style_settings'] = True
    #     return template_params
