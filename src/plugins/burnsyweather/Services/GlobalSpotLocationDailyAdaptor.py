from datetime import datetime
import json
import os

from plugins.burnsyweather.Models.MetOffice.SiteSpecificDaily import DailyRoot
from plugins.burnsyweather.Services.WeatherGetter import WeatherGetter

class GlobalSpotLocationDailyAdaptor:
    def get_spot_daily_forecast(self, icons_path,lat, long):

        weather_getter = WeatherGetter()
        raw_weather_data_daily = weather_getter.get_content(lat, long, "daily")

        jsonstring_daily = json.loads(raw_weather_data_daily)
        weather_data = DailyRoot.from_dict(jsonstring_daily)
        
        global_spot_location_daily = {}
        
        # for elements 2, 3, and 4 - tomorrow, day after, and day after that
        for i in range(2,5):
            ts = weather_data.features[0].properties.timeSeries[i]
            # Day heading: first of the three days should always read "Tomorrow"
            if i == 2:
                heading = "Tomorrow"
            else:
                try:
                    dt = datetime.fromisoformat(ts.time)
                    heading = dt.strftime('%a')
                except Exception:
                    heading = ''

            global_spot_location_daily[f"daily_{i-1}_heading"] = heading
            global_spot_location_daily[f"day_{i-1}_weather_symbol"] = os.path.join(icons_path, f'{ts.daySignificantWeatherCode}.svg')
            global_spot_location_daily[f"day_{i-1}_temp_max"] = str(round(ts.dayMaxScreenTemperature)) + '°C'
            global_spot_location_daily[f"day_{i-1}_temp_min"] = str(round(ts.nightMinScreenTemperature)) + '°C'

        return global_spot_location_daily