from datetime import datetime
import json
import os

from plugins.burnsyweather.Models.MetOffice.SiteSpecificHourly import HourlyRoot
from plugins.burnsyweather.Services.WeatherGetter import WeatherGetter

class GlobalSpotLocationHoursAdaptor:
    def get_spot_hourly_forecast(self, plugin_dir, lat, long):     


        weather_getter = WeatherGetter()

        raw_weather_data_hourly =  weather_getter.get_content(lat, long, "hourly")
        jsonstring = json.loads(raw_weather_data_hourly)
        weather_data = HourlyRoot.from_dict(jsonstring)
        
        timed_series = weather_data.features[0].properties.timeSeries

        global_spot_location_hours = {}
        
        for i in range(12):
            global_spot_location_hours[f"hour_{i+1}_weather_symbol"] = os.path.join(plugin_dir, 'icons', 'old', f'{timed_series[i].significantWeatherCode}.svg')
            global_spot_location_hours[f"hour_{i+1}_time"] = (datetime.fromisoformat(timed_series[i].time)).strftime('%H:%M')
            global_spot_location_hours[f"hour_{i+1}_precip"] = str(timed_series[i].probOfPrecipitation) + '%'
            global_spot_location_hours[f"hour_{i+1}_temp"] = str(round(timed_series[i].screenTemperature)) + '°C'
            global_spot_location_hours[f"hour_{i+1}_feels"] = str(round(timed_series[i].feelsLikeTemperature)) + '°C'
            global_spot_location_hours[f"hour_{i+1}_wind_dir"] = timed_series[i].windDirectionFrom10m
            global_spot_location_hours[f"hour_{i+1}_wind_gust"] = round(timed_series[i].windGustSpeed10m)
            global_spot_location_hours[f"hour_{i+1}_visibility"] = timed_series[i].visibility
            global_spot_location_hours[f"hour_{i+1}_humidity"] = str(round(timed_series[i].screenRelativeHumidity)) + '%'
            global_spot_location_hours[f"hour_{i+1}_uv"] = timed_series[i].uvIndex
        
        # Debug: Print out the first 12 hours of weather symbols because 0 is missing
        for j in range(12):
            print(f"Signifiant Weather Code for hour {j+1}: ", global_spot_location_hours[f"hour_{j+1}_weather_symbol"])

        return global_spot_location_hours