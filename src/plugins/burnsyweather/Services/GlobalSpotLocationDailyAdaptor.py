from datetime import datetime
import json
import os

from plugins.burnsyweather.Models.MetOffice.SiteSpecificDaily import DailyRoot
from plugins.burnsyweather.Services.WeatherGetter import WeatherGetter

class GlobalSpotLocationDailyAdaptor:
    def get_spot_daily_forecast(self, plugin_dir,lat, long):

        weather_getter = WeatherGetter()
        raw_weather_data_daily = weather_getter.get_content(lat, long, "daily")

        jsonstring_daily = json.loads(raw_weather_data_daily)
        weather_data = DailyRoot.from_dict(jsonstring_daily)
        
        global_spot_location_daily = {}
        
        # for elements 2, 3, and 4 - tomorrow, day after, and day after that
        for i in range(2,5):
            global_spot_location_daily[f"day_{i-1}_weather_symbol"] = os.path.join(plugin_dir, 'icons', 'old', f'{weather_data.features[0].properties.timeSeries[i].daySignificantWeatherCode}.svg')
            global_spot_location_daily[f"day_{i-1}_temp_max"] = weather_data.features[0].properties.timeSeries[i].dayMaxScreenTemperature
            global_spot_location_daily[f"day_{i-1}_temp_min"] = weather_data.features[0].properties.timeSeries[i].nightMinScreenTemperature
     
        return global_spot_location_daily