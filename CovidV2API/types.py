import typing
from dataclasses import dataclass


@dataclass
class Coordinates:
    latitude: str
    longitude: str


@dataclass
class Latest:
    confirmed: int
    deaths: int
    recovered: int


@dataclass
class TimelineData:
    latest: int
    timeline: typing.Dict[str, int]


class Timelines:
    confirmed: TimelineData
    deaths: TimelineData
    recovered: TimelineData

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, TimelineData(**value))


class Location:
    id: int
    country: str
    country_code: str
    country_population: int
    province: str
    county: str
    last_updated: str
    coordinates: Coordinates
    latest: Latest
    timelines: Timelines

    def __init__(self, **kwargs):
        for key, value in kwargs.get('location').items():
            obj = None
            if key == 'coordinates':
                obj = Coordinates(**value)
            if key == 'latest':
                obj = Latest(**value)
            if key == 'timelines':
                obj = Timelines(**value)

            if obj:
                setattr(self, key, obj)
            else:
                setattr(self, key, value)


class LocationsAnswer:
    latest: Latest
    locations: typing.List[Location]

    def __init__(self, latest, locations):
        self.latest = Latest(**latest)
        self.locations = [Location(**location) for location in locations]
