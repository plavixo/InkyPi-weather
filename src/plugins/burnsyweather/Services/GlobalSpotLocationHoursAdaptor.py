from datetime import datetime

class GlobalSpotLocationHoursAdaptor:
    def get_spot_hourly_forecast(self, weather_data):     
        
        # global_spot_location_hours ={
        #     "hour_1_time": (datetime.fromisoformat(weather_data.features[0].properties.timeSeries[0].time)).strftime('%H:%M'),
        #     "hour_1_precip": weather_data.features[0].properties.timeSeries[0].probOfPrecipitation,
        # }

        timed_series = weather_data.features[0].properties.timeSeries

        global_spot_location_hours = {}
        
        for i in range(12):
            global_spot_location_hours[f"hour_{i+1}_time"] = (datetime.fromisoformat(timed_series[i].time)).strftime('%H:%M')
            global_spot_location_hours[f"hour_{i+1}_precip"] = timed_series[i].probOfPrecipitation
            global_spot_location_hours[f"hour_{i+1}_temp"] = timed_series[i].screenTemperature
            global_spot_location_hours[f"hour_{i+1}_feels"] = timed_series[i].feelsLikeTemperature
            global_spot_location_hours[f"hour_{i+1}_wind_dir"] = timed_series[i].windDirectionFrom10m
            global_spot_location_hours[f"hour_{i+1}_wind_gust"] = timed_series[i].windGustSpeed10m
            global_spot_location_hours[f"hour_{i+1}_visibility"] = timed_series[i].visibility
            global_spot_location_hours[f"hour_{i+1}_humidity"] = timed_series[i].screenRelativeHumidity
            global_spot_location_hours[f"hour_{i+1}_uv"] = timed_series[i].uvIndex
            
        return global_spot_location_hours