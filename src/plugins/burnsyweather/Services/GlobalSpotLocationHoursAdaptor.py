from datetime import datetime
import json
import os

from plugins.burnsyweather.Models.MetOffice.SiteSpecificHourly import HourlyRoot
from plugins.burnsyweather.Services.WeatherGetter import WeatherGetter

class GlobalSpotLocationHoursAdaptor:
    def get_spot_hourly_forecast(self, icons_path, lat, long):     
        weather_getter = WeatherGetter()

        raw_weather_data_hourly =  weather_getter.get_content(lat, long, "hourly")
        jsonstring = json.loads(raw_weather_data_hourly)
        weather_data = HourlyRoot.from_dict(jsonstring)
        
        timed_series = weather_data.features[0].properties.timeSeries

        global_spot_location_hours = {}
        
        for i in range(12):
            global_spot_location_hours[f"hour_{i+1}_weather_symbol"] = os.path.join(icons_path, f'{timed_series[i].significantWeatherCode}.svg')
            global_spot_location_hours[f"hour_{i+1}_time"] = (datetime.fromisoformat(timed_series[i].time)).strftime('%H:%M')
            global_spot_location_hours[f"hour_{i+1}_precip"] = str(timed_series[i].probOfPrecipitation) + '%'
            global_spot_location_hours[f"hour_{i+1}_temp"] = str(round(timed_series[i].screenTemperature)) + '°C'
            global_spot_location_hours[f"hour_{i+1}_feels"] = str(round(timed_series[i].feelsLikeTemperature)) + '°C'
            global_spot_location_hours[f"hour_{i+1}_wind_dir"] = timed_series[i].windDirectionFrom10m
            global_spot_location_hours[f"hour_{i+1}_wind_gust"] = round(timed_series[i].windGustSpeed10m)
            global_spot_location_hours[f"hour_{i+1}_visibility"] = timed_series[i].visibility
            global_spot_location_hours[f"hour_{i+1}_humidity"] = str(round(timed_series[i].screenRelativeHumidity)) + '%'
            global_spot_location_hours[f"hour_{i+1}_uv"] = timed_series[i].uvIndex
 
        # Special items
        model_run_date = weather_data.features[0].properties.modelRunDate
        global_spot_location_hours["model_run_time"] = model_run_date

        hour_one_weather_symbol = os.path.join(icons_path, f'{weather_data.features[0].properties.timeSeries[0].significantWeatherCode}.svg')
        global_spot_location_hours["hour_one_weather_symbol"] = hour_one_weather_symbol

        return global_spot_location_hours