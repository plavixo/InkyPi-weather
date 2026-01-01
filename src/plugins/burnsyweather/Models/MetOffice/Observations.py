from typing import Any, List
from dataclasses import dataclass
import json
@dataclass
class Root:
    datetime: str
    humidity: int
    mslp: int
    pressure_tendency: str
    temperature: float
    visibility: float
    weather_code: int
    wind_direction: str
    wind_gust: float
    wind_speed: float

    @staticmethod
    def from_list(objs: Any) -> List["Root"]:
        return [Root.from_dict(obj) for obj in objs]

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _datetime = str(obj.get("datetime"))
        def _f(v, default=0.0):
            return default if v is None else float(v)
        def _i(v, default=0):
            return default if v is None else int(v)

        _humidity = _i(obj.get("humidity"))
        _mslp = _i(obj.get("mslp"))
        _pressure_tendency = obj.get("pressure_tendency") or ""
        _temperature = _f(obj.get("temperature"))
        _visibility = _f(obj.get("visibility"))
        _weather_code = _i(obj.get("weather_code"))
        _wind_direction = obj.get("wind_direction") or ""
        _wind_gust = _f(obj.get("wind_gust"))
        _wind_speed = _f(obj.get("wind_speed"))
        return Root(_datetime, _humidity, _mslp, _pressure_tendency, _temperature, _visibility, _weather_code, _wind_direction, _wind_gust, _wind_speed)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
