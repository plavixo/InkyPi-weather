from typing import List
from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Feature:
    type: str
    geometry: Geometry
    properties: Properties

    @staticmethod
    def from_dict(obj: Any) -> 'Feature':
        _type = str(obj.get("type"))
        _geometry = Geometry.from_dict(obj.get("geometry"))
        _properties = Properties.from_dict(obj.get("properties"))
        return Feature(_type, _geometry, _properties)

@dataclass
class FeelsLikeTemperature:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'FeelsLikeTemperature':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return FeelsLikeTemperature(_type, _description, _unit)

@dataclass
class Geometry:
    type: str
    coordinates: List[float]

    @staticmethod
    def from_dict(obj: Any) -> 'Geometry':
        _type = str(obj.get("type"))
        def _parse_coords(o):
            if isinstance(o, list):
                return [_parse_coords(x) for x in o]
            return float(o)
        _coordinates = _parse_coords(obj.get("coordinates"))
        return Geometry(_type, _coordinates)

@dataclass
class Max10mWindGust:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'Max10mWindGust':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return Max10mWindGust(_type, _description, _unit)

@dataclass
class MaxScreenAirTemp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'MaxScreenAirTemp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return MaxScreenAirTemp(_type, _description, _unit)

@dataclass
class MinScreenAirTemp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'MinScreenAirTemp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return MinScreenAirTemp(_type, _description, _unit)

@dataclass
class Mslp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'Mslp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return Mslp(_type, _description, _unit)

@dataclass
class Parameter:
    totalSnowAmount: TotalSnowAmount
    screenTemperature: ScreenTemperature
    visibility: Visibility
    windDirectionFrom10m: WindDirectionFrom10m
    precipitationRate: PrecipitationRate
    maxScreenAirTemp: MaxScreenAirTemp
    feelsLikeTemperature: FeelsLikeTemperature
    screenDewPointTemperature: ScreenDewPointTemperature
    screenRelativeHumidity: ScreenRelativeHumidity
    windSpeed10m: WindSpeed10m
    probOfPrecipitation: ProbOfPrecipitation
    max10mWindGust: Max10mWindGust
    significantWeatherCode: SignificantWeatherCode
    minScreenAirTemp: MinScreenAirTemp
    totalPrecipAmount: TotalPrecipAmount
    mslp: Mslp
    windGustSpeed10m: WindGustSpeed10m
    uvIndex: UvIndex

    @staticmethod
    def from_dict(obj: Any) -> 'Parameter':
        _totalSnowAmount = TotalSnowAmount.from_dict(obj.get("totalSnowAmount"))
        _screenTemperature = ScreenTemperature.from_dict(obj.get("screenTemperature"))
        _visibility = Visibility.from_dict(obj.get("visibility"))
        _windDirectionFrom10m = WindDirectionFrom10m.from_dict(obj.get("windDirectionFrom10m"))
        _precipitationRate = PrecipitationRate.from_dict(obj.get("precipitationRate"))
        _maxScreenAirTemp = MaxScreenAirTemp.from_dict(obj.get("maxScreenAirTemp"))
        _feelsLikeTemperature = FeelsLikeTemperature.from_dict(obj.get("feelsLikeTemperature"))
        _screenDewPointTemperature = ScreenDewPointTemperature.from_dict(obj.get("screenDewPointTemperature"))
        _screenRelativeHumidity = ScreenRelativeHumidity.from_dict(obj.get("screenRelativeHumidity"))
        _windSpeed10m = WindSpeed10m.from_dict(obj.get("windSpeed10m"))
        _probOfPrecipitation = ProbOfPrecipitation.from_dict(obj.get("probOfPrecipitation"))
        _max10mWindGust = Max10mWindGust.from_dict(obj.get("max10mWindGust"))
        _significantWeatherCode = SignificantWeatherCode.from_dict(obj.get("significantWeatherCode"))
        _minScreenAirTemp = MinScreenAirTemp.from_dict(obj.get("minScreenAirTemp"))
        _totalPrecipAmount = TotalPrecipAmount.from_dict(obj.get("totalPrecipAmount"))
        _mslp = Mslp.from_dict(obj.get("mslp"))
        _windGustSpeed10m = WindGustSpeed10m.from_dict(obj.get("windGustSpeed10m"))
        _uvIndex = UvIndex.from_dict(obj.get("uvIndex"))
        return Parameter(_totalSnowAmount, _screenTemperature, _visibility, _windDirectionFrom10m, _precipitationRate, _maxScreenAirTemp, _feelsLikeTemperature, _screenDewPointTemperature, _screenRelativeHumidity, _windSpeed10m, _probOfPrecipitation, _max10mWindGust, _significantWeatherCode, _minScreenAirTemp, _totalPrecipAmount, _mslp, _windGustSpeed10m, _uvIndex)

@dataclass
class PrecipitationRate:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'PrecipitationRate':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return PrecipitationRate(_type, _description, _unit)

@dataclass
class ProbOfPrecipitation:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'ProbOfPrecipitation':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return ProbOfPrecipitation(_type, _description, _unit)

@dataclass
class Properties:
    requestPointDistance: float
    modelRunDate: str
    timeSeries: List[TimeSeries]

    @staticmethod
    def from_dict(obj: Any) -> 'Properties':
        _requestPointDistance = float(obj.get("requestPointDistance"))
        _modelRunDate = str(obj.get("modelRunDate"))
        _timeSeries = [TimeSeries.from_dict(y) for y in obj.get("timeSeries")]
        return Properties(_requestPointDistance, _modelRunDate, _timeSeries)

@dataclass
class Root:
    type: str
    features: List[Feature]
    parameters: List[Parameter]

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _type = str(obj.get("type"))
        _features = [Feature.from_dict(y) for y in obj.get("features")]
        _parameters = [Parameter.from_dict(y) for y in obj.get("parameters")]
        return Root(_type, _features, _parameters)

@dataclass
class ScreenDewPointTemperature:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'ScreenDewPointTemperature':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return ScreenDewPointTemperature(_type, _description, _unit)

@dataclass
class ScreenRelativeHumidity:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'ScreenRelativeHumidity':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return ScreenRelativeHumidity(_type, _description, _unit)

@dataclass
class ScreenTemperature:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'ScreenTemperature':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return ScreenTemperature(_type, _description, _unit)

@dataclass
class SignificantWeatherCode:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'SignificantWeatherCode':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return SignificantWeatherCode(_type, _description, _unit)

@dataclass
class Symbol:
    value: str
    type: str

    @staticmethod
    def from_dict(obj: Any) -> 'Symbol':
        _value = str(obj.get("value"))
        _type = str(obj.get("type"))
        return Symbol(_value, _type)

@dataclass
class TimeSeries:
    time: str
    screenTemperature: float
    maxScreenAirTemp: float
    minScreenAirTemp: float
    screenDewPointTemperature: float
    feelsLikeTemperature: float
    windSpeed10m: float
    windDirectionFrom10m: int
    windGustSpeed10m: float
    max10mWindGust: float
    visibility: int
    screenRelativeHumidity: float
    mslp: int
    uvIndex: int
    significantWeatherCode: int
    precipitationRate: float
    totalPrecipAmount: float
    totalSnowAmount: int
    probOfPrecipitation: int

    @staticmethod
    def from_dict(obj: Any) -> 'TimeSeries':
        _time = str(obj.get("time"))
        def _f(v, default=0.0):
            return default if v is None else float(v)
        def _i(v, default=0):
            return default if v is None else int(v)

        _screenTemperature = _f(obj.get("screenTemperature"))
        _maxScreenAirTemp = _f(obj.get("maxScreenAirTemp"))
        _minScreenAirTemp = _f(obj.get("minScreenAirTemp"))
        _screenDewPointTemperature = _f(obj.get("screenDewPointTemperature"))
        _feelsLikeTemperature = _f(obj.get("feelsLikeTemperature"))
        _windSpeed10m = _f(obj.get("windSpeed10m"))
        _windDirectionFrom10m = _i(obj.get("windDirectionFrom10m"))
        _windGustSpeed10m = _f(obj.get("windGustSpeed10m"))
        _max10mWindGust = _f(obj.get("max10mWindGust"))
        _visibility = _i(obj.get("visibility"))
        _screenRelativeHumidity = _f(obj.get("screenRelativeHumidity"))
        _mslp = _i(obj.get("mslp"))
        _uvIndex = _i(obj.get("uvIndex"))
        _significantWeatherCode = _i(obj.get("significantWeatherCode"))
        _precipitationRate = _f(obj.get("precipitationRate"))
        _totalPrecipAmount = _f(obj.get("totalPrecipAmount"))
        _totalSnowAmount = _i(obj.get("totalSnowAmount"))
        _probOfPrecipitation = _i(obj.get("probOfPrecipitation"))
        return TimeSeries(_time, _screenTemperature, _maxScreenAirTemp, _minScreenAirTemp, _screenDewPointTemperature, _feelsLikeTemperature, _windSpeed10m, _windDirectionFrom10m, _windGustSpeed10m, _max10mWindGust, _visibility, _screenRelativeHumidity, _mslp, _uvIndex, _significantWeatherCode, _precipitationRate, _totalPrecipAmount, _totalSnowAmount, _probOfPrecipitation)

@dataclass
class TotalPrecipAmount:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'TotalPrecipAmount':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return TotalPrecipAmount(_type, _description, _unit)

@dataclass
class TotalSnowAmount:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'TotalSnowAmount':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return TotalSnowAmount(_type, _description, _unit)

@dataclass
class Unit:
    label: str
    symbol: Symbol

    @staticmethod
    def from_dict(obj: Any) -> 'Unit':
        _label = str(obj.get("label"))
        _symbol = Symbol.from_dict(obj.get("symbol"))
        return Unit(_label, _symbol)

@dataclass
class UvIndex:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'UvIndex':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return UvIndex(_type, _description, _unit)

@dataclass
class Visibility:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'Visibility':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return Visibility(_type, _description, _unit)

@dataclass
class WindDirectionFrom10m:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'WindDirectionFrom10m':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return WindDirectionFrom10m(_type, _description, _unit)

@dataclass
class WindGustSpeed10m:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'WindGustSpeed10m':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return WindGustSpeed10m(_type, _description, _unit)

@dataclass
class WindSpeed10m:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'WindSpeed10m':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return WindSpeed10m(_type, _description, _unit)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
