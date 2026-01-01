from datetime import datetime
import os

class GlobalSpotLocationDailyAdaptor:
    def get_spot_daily_forecast(self, weather_data, plugin_dir):     
        
        global_spot_location_daily = {}
        
        # for elements 2, 3, and 4 - tomowrrow, day after, and day after that
        for i in range(2,5):
            global_spot_location_daily[f"day_{i-1}_weather_symbol"] = os.path.join(plugin_dir, 'icons', 'old', f'{weather_data.features[0].properties.timeSeries[i].daySignificantWeatherCode}.svg')
            global_spot_location_daily[f"day_{i-1}_temp_max"] = weather_data.features[0].properties.timeSeries[i].dayMaxScreenTemperature
            global_spot_location_daily[f"day_{i-1}_temp_min"] = weather_data.features[0].properties.timeSeries[i].nightMinScreenTemperature
     
        return global_spot_location_daily