from plugins.base_plugin.base_plugin import BasePlugin
from utils.app_utils import resolve_path

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
    # def generate_settings_template(self):
    #     template_params = super().generate_settings_template()
    #     template_params['api_key'] = {
    #         "required": True,
    #         "service": "OpenAI",
    #         "expected_key": "OPEN_AI_SECRET"
    #     }
    #     template_params['style_settings'] = True
    #     return template_params

    def generate_image(self, settings, device_config):
        # api_key = device_config.load_env_key("OPEN_AI_SECRET")
        # if not api_key:
        #     raise RuntimeError("OPEN AI API Key not configured.")

        title = settings.get("title")
        if not title:
            raise RuntimeError("Title is required.")

        # text_model = settings.get('textModel')
        # if not text_model:
        #     raise RuntimeError("Text Model is required.")

        # text_prompt = settings.get('textPrompt', '')
        # if not text_prompt.strip():
        #     raise RuntimeError("Text Prompt is required.")

        # try:
        #     ai_client = OpenAI(api_key = api_key)
        #     prompt_response = AIText.fetch_text_prompt(ai_client, text_model, text_prompt)
        # except Exception as e:
        #     logger.error(f"Failed to make Open AI request: {str(e)}")
        #     raise RuntimeError("Open AI request failure, please check logs.")

        prompt_response ="Here's hoping it's a lovely day"



        image_template_params = {
            "title": title,
            "content": prompt_response,
            "plugin_settings": settings
        }

        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]
        
        image = self.render_image(dimensions, "burnsyweather.html", "burnsyweather.css", image_template_params)

        return image