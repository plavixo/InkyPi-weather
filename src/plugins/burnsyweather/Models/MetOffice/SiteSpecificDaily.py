from typing import List
from typing import Any
from dataclasses import dataclass
import json

@dataclass
class DailyRoot:
    type: str
    features: List[Feature]
    parameters: List[Parameter]

    @staticmethod
    def from_dict(obj: Any) -> 'DailyRoot':
        _type = str(obj.get("type"))
        _features = [Feature.from_dict(y) for y in obj.get("features")]
        _parameters = [Parameter.from_dict(y) for y in obj.get("parameters")]
        return DailyRoot(_type, _features, _parameters)

@dataclass
class DayLowerBoundMaxFeelsLikeTemp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayLowerBoundMaxFeelsLikeTemp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayLowerBoundMaxFeelsLikeTemp(_type, _description, _unit)

@dataclass
class DayLowerBoundMaxTemp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayLowerBoundMaxTemp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayLowerBoundMaxTemp(_type, _description, _unit)

@dataclass
class DayMaxFeelsLikeTemp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayMaxFeelsLikeTemp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayMaxFeelsLikeTemp(_type, _description, _unit)

@dataclass
class DayMaxScreenTemperature:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayMaxScreenTemperature':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayMaxScreenTemperature(_type, _description, _unit)

@dataclass
class DayProbabilityOfHail:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayProbabilityOfHail':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayProbabilityOfHail(_type, _description, _unit)

@dataclass
class DayProbabilityOfHeavyRain:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayProbabilityOfHeavyRain':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayProbabilityOfHeavyRain(_type, _description, _unit)

@dataclass
class DayProbabilityOfHeavySnow:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayProbabilityOfHeavySnow':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayProbabilityOfHeavySnow(_type, _description, _unit)

@dataclass
class DayProbabilityOfPrecipitation:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayProbabilityOfPrecipitation':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayProbabilityOfPrecipitation(_type, _description, _unit)

@dataclass
class DayProbabilityOfRain:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayProbabilityOfRain':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayProbabilityOfRain(_type, _description, _unit)

@dataclass
class DayProbabilityOfSferics:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayProbabilityOfSferics':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayProbabilityOfSferics(_type, _description, _unit)

@dataclass
class DayProbabilityOfSnow:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayProbabilityOfSnow':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayProbabilityOfSnow(_type, _description, _unit)

@dataclass
class DaySignificantWeatherCode:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DaySignificantWeatherCode':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DaySignificantWeatherCode(_type, _description, _unit)

@dataclass
class DayUpperBoundMaxFeelsLikeTemp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayUpperBoundMaxFeelsLikeTemp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayUpperBoundMaxFeelsLikeTemp(_type, _description, _unit)

@dataclass
class DayUpperBoundMaxTemp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'DayUpperBoundMaxTemp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return DayUpperBoundMaxTemp(_type, _description, _unit)

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
class Location:
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Location':
        _name = str(obj.get("name"))
        return Location(_name)

@dataclass
class MaxUvIndex:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'MaxUvIndex':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return MaxUvIndex(_type, _description, _unit)

@dataclass
class Midday10MWindDirection:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'Midday10MWindDirection':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return Midday10MWindDirection(_type, _description, _unit)

@dataclass
class Midday10MWindGust:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'Midday10MWindGust':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return Midday10MWindGust(_type, _description, _unit)

@dataclass
class Midday10MWindSpeed:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'Midday10MWindSpeed':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return Midday10MWindSpeed(_type, _description, _unit)

@dataclass
class MiddayMslp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'MiddayMslp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return MiddayMslp(_type, _description, _unit)

@dataclass
class MiddayRelativeHumidity:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'MiddayRelativeHumidity':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return MiddayRelativeHumidity(_type, _description, _unit)

@dataclass
class MiddayVisibility:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'MiddayVisibility':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return MiddayVisibility(_type, _description, _unit)

@dataclass
class Midnight10MWindDirection:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'Midnight10MWindDirection':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return Midnight10MWindDirection(_type, _description, _unit)

@dataclass
class Midnight10MWindGust:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'Midnight10MWindGust':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return Midnight10MWindGust(_type, _description, _unit)

@dataclass
class Midnight10MWindSpeed:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'Midnight10MWindSpeed':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return Midnight10MWindSpeed(_type, _description, _unit)

@dataclass
class MidnightMslp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'MidnightMslp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return MidnightMslp(_type, _description, _unit)

@dataclass
class MidnightRelativeHumidity:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'MidnightRelativeHumidity':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return MidnightRelativeHumidity(_type, _description, _unit)

@dataclass
class MidnightVisibility:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'MidnightVisibility':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return MidnightVisibility(_type, _description, _unit)

@dataclass
class NightLowerBoundMinFeelsLikeTemp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightLowerBoundMinFeelsLikeTemp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightLowerBoundMinFeelsLikeTemp(_type, _description, _unit)

@dataclass
class NightLowerBoundMinTemp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightLowerBoundMinTemp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightLowerBoundMinTemp(_type, _description, _unit)

@dataclass
class NightMinFeelsLikeTemp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightMinFeelsLikeTemp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightMinFeelsLikeTemp(_type, _description, _unit)

@dataclass
class NightMinScreenTemperature:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightMinScreenTemperature':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightMinScreenTemperature(_type, _description, _unit)

@dataclass
class NightProbabilityOfHail:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightProbabilityOfHail':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightProbabilityOfHail(_type, _description, _unit)

@dataclass
class NightProbabilityOfHeavyRain:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightProbabilityOfHeavyRain':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightProbabilityOfHeavyRain(_type, _description, _unit)

@dataclass
class NightProbabilityOfHeavySnow:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightProbabilityOfHeavySnow':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightProbabilityOfHeavySnow(_type, _description, _unit)

@dataclass
class NightProbabilityOfPrecipitation:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightProbabilityOfPrecipitation':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightProbabilityOfPrecipitation(_type, _description, _unit)

@dataclass
class NightProbabilityOfRain:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightProbabilityOfRain':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightProbabilityOfRain(_type, _description, _unit)

@dataclass
class NightProbabilityOfSferics:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightProbabilityOfSferics':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightProbabilityOfSferics(_type, _description, _unit)

@dataclass
class NightProbabilityOfSnow:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightProbabilityOfSnow':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightProbabilityOfSnow(_type, _description, _unit)

@dataclass
class NightSignificantWeatherCode:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightSignificantWeatherCode':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightSignificantWeatherCode(_type, _description, _unit)

@dataclass
class NightUpperBoundMinFeelsLikeTemp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightUpperBoundMinFeelsLikeTemp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightUpperBoundMinFeelsLikeTemp(_type, _description, _unit)

@dataclass
class NightUpperBoundMinTemp:
    type: str
    description: str
    unit: Unit

    @staticmethod
    def from_dict(obj: Any) -> 'NightUpperBoundMinTemp':
        _type = str(obj.get("type"))
        _description = str(obj.get("description"))
        _unit = Unit.from_dict(obj.get("unit"))
        return NightUpperBoundMinTemp(_type, _description, _unit)

@dataclass
class Parameter:
    daySignificantWeatherCode: DaySignificantWeatherCode
    midnightRelativeHumidity: MidnightRelativeHumidity
    nightProbabilityOfHeavyRain: NightProbabilityOfHeavyRain
    midnight10MWindSpeed: Midnight10MWindSpeed
    nightUpperBoundMinFeelsLikeTemp: NightUpperBoundMinFeelsLikeTemp
    nightUpperBoundMinTemp: NightUpperBoundMinTemp
    midnightVisibility: MidnightVisibility
    dayUpperBoundMaxFeelsLikeTemp: DayUpperBoundMaxFeelsLikeTemp
    nightProbabilityOfRain: NightProbabilityOfRain
    midday10MWindDirection: Midday10MWindDirection
    nightLowerBoundMinFeelsLikeTemp: NightLowerBoundMinFeelsLikeTemp
    nightProbabilityOfHail: NightProbabilityOfHail
    middayMslp: MiddayMslp
    dayProbabilityOfHeavySnow: DayProbabilityOfHeavySnow
    nightProbabilityOfPrecipitation: NightProbabilityOfPrecipitation
    dayProbabilityOfHail: DayProbabilityOfHail
    dayProbabilityOfRain: DayProbabilityOfRain
    midday10MWindSpeed: Midday10MWindSpeed
    midday10MWindGust: Midday10MWindGust
    middayVisibility: MiddayVisibility
    midnight10MWindGust: Midnight10MWindGust
    midnightMslp: MidnightMslp
    dayProbabilityOfSferics: DayProbabilityOfSferics
    nightSignificantWeatherCode: NightSignificantWeatherCode
    dayProbabilityOfPrecipitation: DayProbabilityOfPrecipitation
    dayProbabilityOfHeavyRain: DayProbabilityOfHeavyRain
    dayMaxScreenTemperature: DayMaxScreenTemperature
    nightMinScreenTemperature: NightMinScreenTemperature
    midnight10MWindDirection: Midnight10MWindDirection
    maxUvIndex: MaxUvIndex
    dayProbabilityOfSnow: DayProbabilityOfSnow
    nightProbabilityOfSnow: NightProbabilityOfSnow
    dayLowerBoundMaxTemp: DayLowerBoundMaxTemp
    nightProbabilityOfHeavySnow: NightProbabilityOfHeavySnow
    dayLowerBoundMaxFeelsLikeTemp: DayLowerBoundMaxFeelsLikeTemp
    dayUpperBoundMaxTemp: DayUpperBoundMaxTemp
    dayMaxFeelsLikeTemp: DayMaxFeelsLikeTemp
    middayRelativeHumidity: MiddayRelativeHumidity
    nightLowerBoundMinTemp: NightLowerBoundMinTemp
    nightMinFeelsLikeTemp: NightMinFeelsLikeTemp
    nightProbabilityOfSferics: NightProbabilityOfSferics

    @staticmethod
    def from_dict(obj: Any) -> 'Parameter':
        _daySignificantWeatherCode = DaySignificantWeatherCode.from_dict(obj.get("daySignificantWeatherCode"))
        _midnightRelativeHumidity = MidnightRelativeHumidity.from_dict(obj.get("midnightRelativeHumidity"))
        _nightProbabilityOfHeavyRain = NightProbabilityOfHeavyRain.from_dict(obj.get("nightProbabilityOfHeavyRain"))
        _midnight10MWindSpeed = Midnight10MWindSpeed.from_dict(obj.get("midnight10MWindSpeed"))
        _nightUpperBoundMinFeelsLikeTemp = NightUpperBoundMinFeelsLikeTemp.from_dict(obj.get("nightUpperBoundMinFeelsLikeTemp"))
        _nightUpperBoundMinTemp = NightUpperBoundMinTemp.from_dict(obj.get("nightUpperBoundMinTemp"))
        _midnightVisibility = MidnightVisibility.from_dict(obj.get("midnightVisibility"))
        _dayUpperBoundMaxFeelsLikeTemp = DayUpperBoundMaxFeelsLikeTemp.from_dict(obj.get("dayUpperBoundMaxFeelsLikeTemp"))
        _nightProbabilityOfRain = NightProbabilityOfRain.from_dict(obj.get("nightProbabilityOfRain"))
        _midday10MWindDirection = Midday10MWindDirection.from_dict(obj.get("midday10MWindDirection"))
        _nightLowerBoundMinFeelsLikeTemp = NightLowerBoundMinFeelsLikeTemp.from_dict(obj.get("nightLowerBoundMinFeelsLikeTemp"))
        _nightProbabilityOfHail = NightProbabilityOfHail.from_dict(obj.get("nightProbabilityOfHail"))
        _middayMslp = MiddayMslp.from_dict(obj.get("middayMslp"))
        _dayProbabilityOfHeavySnow = DayProbabilityOfHeavySnow.from_dict(obj.get("dayProbabilityOfHeavySnow"))
        _nightProbabilityOfPrecipitation = NightProbabilityOfPrecipitation.from_dict(obj.get("nightProbabilityOfPrecipitation"))
        _dayProbabilityOfHail = DayProbabilityOfHail.from_dict(obj.get("dayProbabilityOfHail"))
        _dayProbabilityOfRain = DayProbabilityOfRain.from_dict(obj.get("dayProbabilityOfRain"))
        _midday10MWindSpeed = Midday10MWindSpeed.from_dict(obj.get("midday10MWindSpeed"))
        _midday10MWindGust = Midday10MWindGust.from_dict(obj.get("midday10MWindGust"))
        _middayVisibility = MiddayVisibility.from_dict(obj.get("middayVisibility"))
        _midnight10MWindGust = Midnight10MWindGust.from_dict(obj.get("midnight10MWindGust"))
        _midnightMslp = MidnightMslp.from_dict(obj.get("midnightMslp"))
        _dayProbabilityOfSferics = DayProbabilityOfSferics.from_dict(obj.get("dayProbabilityOfSferics"))
        _nightSignificantWeatherCode = NightSignificantWeatherCode.from_dict(obj.get("nightSignificantWeatherCode"))
        _dayProbabilityOfPrecipitation = DayProbabilityOfPrecipitation.from_dict(obj.get("dayProbabilityOfPrecipitation"))
        _dayProbabilityOfHeavyRain = DayProbabilityOfHeavyRain.from_dict(obj.get("dayProbabilityOfHeavyRain"))
        _dayMaxScreenTemperature = DayMaxScreenTemperature.from_dict(obj.get("dayMaxScreenTemperature"))
        _nightMinScreenTemperature = NightMinScreenTemperature.from_dict(obj.get("nightMinScreenTemperature"))
        _midnight10MWindDirection = Midnight10MWindDirection.from_dict(obj.get("midnight10MWindDirection"))
        _maxUvIndex = MaxUvIndex.from_dict(obj.get("maxUvIndex"))
        _dayProbabilityOfSnow = DayProbabilityOfSnow.from_dict(obj.get("dayProbabilityOfSnow"))
        _nightProbabilityOfSnow = NightProbabilityOfSnow.from_dict(obj.get("nightProbabilityOfSnow"))
        _dayLowerBoundMaxTemp = DayLowerBoundMaxTemp.from_dict(obj.get("dayLowerBoundMaxTemp"))
        _nightProbabilityOfHeavySnow = NightProbabilityOfHeavySnow.from_dict(obj.get("nightProbabilityOfHeavySnow"))
        _dayLowerBoundMaxFeelsLikeTemp = DayLowerBoundMaxFeelsLikeTemp.from_dict(obj.get("dayLowerBoundMaxFeelsLikeTemp"))
        _dayUpperBoundMaxTemp = DayUpperBoundMaxTemp.from_dict(obj.get("dayUpperBoundMaxTemp"))
        _dayMaxFeelsLikeTemp = DayMaxFeelsLikeTemp.from_dict(obj.get("dayMaxFeelsLikeTemp"))
        _middayRelativeHumidity = MiddayRelativeHumidity.from_dict(obj.get("middayRelativeHumidity"))
        _nightLowerBoundMinTemp = NightLowerBoundMinTemp.from_dict(obj.get("nightLowerBoundMinTemp"))
        _nightMinFeelsLikeTemp = NightMinFeelsLikeTemp.from_dict(obj.get("nightMinFeelsLikeTemp"))
        _nightProbabilityOfSferics = NightProbabilityOfSferics.from_dict(obj.get("nightProbabilityOfSferics"))
        return Parameter(_daySignificantWeatherCode, _midnightRelativeHumidity, _nightProbabilityOfHeavyRain, _midnight10MWindSpeed, _nightUpperBoundMinFeelsLikeTemp, _nightUpperBoundMinTemp, _midnightVisibility, _dayUpperBoundMaxFeelsLikeTemp, _nightProbabilityOfRain, _midday10MWindDirection, _nightLowerBoundMinFeelsLikeTemp, _nightProbabilityOfHail, _middayMslp, _dayProbabilityOfHeavySnow, _nightProbabilityOfPrecipitation, _dayProbabilityOfHail, _dayProbabilityOfRain, _midday10MWindSpeed, _midday10MWindGust, _middayVisibility, _midnight10MWindGust, _midnightMslp, _dayProbabilityOfSferics, _nightSignificantWeatherCode, _dayProbabilityOfPrecipitation, _dayProbabilityOfHeavyRain, _dayMaxScreenTemperature, _nightMinScreenTemperature, _midnight10MWindDirection, _maxUvIndex, _dayProbabilityOfSnow, _nightProbabilityOfSnow, _dayLowerBoundMaxTemp, _nightProbabilityOfHeavySnow, _dayLowerBoundMaxFeelsLikeTemp, _dayUpperBoundMaxTemp, _dayMaxFeelsLikeTemp, _middayRelativeHumidity, _nightLowerBoundMinTemp, _nightMinFeelsLikeTemp, _nightProbabilityOfSferics)

@dataclass
class Properties:
    location: Location
    requestPointDistance: float
    modelRunDate: str
    timeSeries: List[TimeSeries]

    @staticmethod
    def from_dict(obj: Any) -> 'Properties':
        _location = Location.from_dict(obj.get("location"))
        _requestPointDistance = float(obj.get("requestPointDistance"))
        _modelRunDate = str(obj.get("modelRunDate"))
        _timeSeries = [TimeSeries.from_dict(y) for y in obj.get("timeSeries")]
        return Properties(_location, _requestPointDistance, _modelRunDate, _timeSeries)



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
    midday10MWindSpeed: float
    midnight10MWindSpeed: float
    midday10MWindDirection: int
    midnight10MWindDirection: int
    midday10MWindGust: float
    midnight10MWindGust: float
    middayVisibility: int
    midnightVisibility: int
    middayRelativeHumidity: float
    midnightRelativeHumidity: float
    middayMslp: int
    midnightMslp: int
    maxUvIndex: int
    daySignificantWeatherCode: int
    nightSignificantWeatherCode: int
    dayMaxScreenTemperature: float
    nightMinScreenTemperature: float
    dayUpperBoundMaxTemp: float
    nightUpperBoundMinTemp: float
    dayLowerBoundMaxTemp: float
    nightLowerBoundMinTemp: float
    dayMaxFeelsLikeTemp: float
    nightMinFeelsLikeTemp: float
    dayUpperBoundMaxFeelsLikeTemp: float
    nightUpperBoundMinFeelsLikeTemp: float
    dayLowerBoundMaxFeelsLikeTemp: float
    nightLowerBoundMinFeelsLikeTemp: float
    dayProbabilityOfPrecipitation: int
    nightProbabilityOfPrecipitation: int
    dayProbabilityOfSnow: int
    nightProbabilityOfSnow: int
    dayProbabilityOfHeavySnow: int
    nightProbabilityOfHeavySnow: int
    dayProbabilityOfRain: int
    nightProbabilityOfRain: int
    dayProbabilityOfHeavyRain: int
    nightProbabilityOfHeavyRain: int
    dayProbabilityOfHail: int
    nightProbabilityOfHail: int
    dayProbabilityOfSferics: int
    nightProbabilityOfSferics: int

    @staticmethod
    def from_dict(obj: Any) -> 'TimeSeries':
        _time = str(obj.get("time"))
        def _f(v, default=0.0):
            return default if v is None else float(v)
        def _i(v, default=0):
            return default if v is None else int(v)

        _midday10MWindSpeed = _f(obj.get("midday10MWindSpeed"))
        _midnight10MWindSpeed = _f(obj.get("midnight10MWindSpeed"))
        _midday10MWindDirection = _i(obj.get("midday10MWindDirection"))
        _midnight10MWindDirection = _i(obj.get("midnight10MWindDirection"))
        _midday10MWindGust = _f(obj.get("midday10MWindGust"))
        _midnight10MWindGust = _f(obj.get("midnight10MWindGust"))
        _middayVisibility = _i(obj.get("middayVisibility"))
        _midnightVisibility = _i(obj.get("midnightVisibility"))
        _middayRelativeHumidity = _f(obj.get("middayRelativeHumidity"))
        _midnightRelativeHumidity = _f(obj.get("midnightRelativeHumidity"))
        _middayMslp = _i(obj.get("middayMslp"))
        _midnightMslp = _i(obj.get("midnightMslp"))
        _maxUvIndex = _i(obj.get("maxUvIndex"))
        _daySignificantWeatherCode = _i(obj.get("daySignificantWeatherCode"))
        _nightSignificantWeatherCode = _i(obj.get("nightSignificantWeatherCode"))
        _dayMaxScreenTemperature = _f(obj.get("dayMaxScreenTemperature"))
        _nightMinScreenTemperature = _f(obj.get("nightMinScreenTemperature"))
        _dayUpperBoundMaxTemp = _f(obj.get("dayUpperBoundMaxTemp"))
        _nightUpperBoundMinTemp = _f(obj.get("nightUpperBoundMinTemp"))
        _dayLowerBoundMaxTemp = _f(obj.get("dayLowerBoundMaxTemp"))
        _nightLowerBoundMinTemp = _f(obj.get("nightLowerBoundMinTemp"))
        _dayMaxFeelsLikeTemp = _f(obj.get("dayMaxFeelsLikeTemp"))
        _nightMinFeelsLikeTemp = _f(obj.get("nightMinFeelsLikeTemp"))
        _dayUpperBoundMaxFeelsLikeTemp = _f(obj.get("dayUpperBoundMaxFeelsLikeTemp"))
        _nightUpperBoundMinFeelsLikeTemp = _f(obj.get("nightUpperBoundMinFeelsLikeTemp"))
        _dayLowerBoundMaxFeelsLikeTemp = _f(obj.get("dayLowerBoundMaxFeelsLikeTemp"))
        _nightLowerBoundMinFeelsLikeTemp = _f(obj.get("nightLowerBoundMinFeelsLikeTemp"))
        _dayProbabilityOfPrecipitation = _i(obj.get("dayProbabilityOfPrecipitation"))
        _nightProbabilityOfPrecipitation = _i(obj.get("nightProbabilityOfPrecipitation"))
        _dayProbabilityOfSnow = _i(obj.get("dayProbabilityOfSnow"))
        _nightProbabilityOfSnow = _i(obj.get("nightProbabilityOfSnow"))
        _dayProbabilityOfHeavySnow = _i(obj.get("dayProbabilityOfHeavySnow"))
        _nightProbabilityOfHeavySnow = _i(obj.get("nightProbabilityOfHeavySnow"))
        _dayProbabilityOfRain = _i(obj.get("dayProbabilityOfRain"))
        _nightProbabilityOfRain = _i(obj.get("nightProbabilityOfRain"))
        _dayProbabilityOfHeavyRain = _i(obj.get("dayProbabilityOfHeavyRain"))
        _nightProbabilityOfHeavyRain = _i(obj.get("nightProbabilityOfHeavyRain"))
        _dayProbabilityOfHail = _i(obj.get("dayProbabilityOfHail"))
        _nightProbabilityOfHail = _i(obj.get("nightProbabilityOfHail"))
        _dayProbabilityOfSferics = _i(obj.get("dayProbabilityOfSferics"))
        _nightProbabilityOfSferics = _i(obj.get("nightProbabilityOfSferics"))
        return TimeSeries(_time, _midday10MWindSpeed, _midnight10MWindSpeed, _midday10MWindDirection, _midnight10MWindDirection, _midday10MWindGust, _midnight10MWindGust, _middayVisibility, _midnightVisibility, _middayRelativeHumidity, _midnightRelativeHumidity, _middayMslp, _midnightMslp, _maxUvIndex, _daySignificantWeatherCode, _nightSignificantWeatherCode, _dayMaxScreenTemperature, _nightMinScreenTemperature, _dayUpperBoundMaxTemp, _nightUpperBoundMinTemp, _dayLowerBoundMaxTemp, _nightLowerBoundMinTemp, _dayMaxFeelsLikeTemp, _nightMinFeelsLikeTemp, _dayUpperBoundMaxFeelsLikeTemp, _nightUpperBoundMinFeelsLikeTemp, _dayLowerBoundMaxFeelsLikeTemp, _nightLowerBoundMinFeelsLikeTemp, _dayProbabilityOfPrecipitation, _nightProbabilityOfPrecipitation, _dayProbabilityOfSnow, _nightProbabilityOfSnow, _dayProbabilityOfHeavySnow, _nightProbabilityOfHeavySnow, _dayProbabilityOfRain, _nightProbabilityOfRain, _dayProbabilityOfHeavyRain, _nightProbabilityOfHeavyRain, _dayProbabilityOfHail, _nightProbabilityOfHail, _dayProbabilityOfSferics, _nightProbabilityOfSferics)

@dataclass
class Unit:
    label: str
    symbol: Symbol

    @staticmethod
    def from_dict(obj: Any) -> 'Unit':
        _label = str(obj.get("label"))
        _symbol = Symbol.from_dict(obj.get("symbol"))
        return Unit(_label, _symbol)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
