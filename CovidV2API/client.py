import requests

from CovidV2API import urls
from CovidV2API.types import *


class API:

    @staticmethod
    def _request(url, payload=None):
        result = requests.get(url, params=payload)
        return result.json()

    @staticmethod
    def latest(source='jhu') -> Latest:
        response = API._request(urls.latest, payload={'source': source})
        return Latest(**response.get('latest'))

    @staticmethod
    def sources() -> typing.Dict[str, str]:
        response = API._request(urls.sources)
        return response

    @staticmethod
    def locations(
            source: str = 'jhu',
            country_code: str = None,
            province: str = None,
            county: str = None,
            timelines: bool = True
    ):
        payload = dict()
        payload['source'] = source

        if country_code:
            payload['country_code'] = country_code
        if province:
            payload['province'] = province
        if county:
            payload['county'] = county
        if timelines:
            payload['timelines'] = timelines

        response = API._request(urls.locations, payload)

        return LocationsAnswer(**response)

    @staticmethod
    def locations_by_id(id: int, source: str = 'jhu', timelines: bool = True):
        payload = dict()

        if source:
            payload['source'] = source
        if timelines:
            payload['timelines'] = timelines

        response = API._request(urls.locations_by_id(id), payload)
        return Location(**response)
