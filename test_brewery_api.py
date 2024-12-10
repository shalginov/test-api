import pytest
import requests


def test_get_random_brewery():
    res = requests.get('https://api.openbrewerydb.org/v1/breweries/random')
    assert res.status_code == 200
    assert bool(res.json()[0]['id']) == True


list_brewery_ids = [
    "8135f18c-0c31-4b4d-bb22-84eccf498e9c",
    "02dcc02a-6cb5-4081-8d36-991f0d31dd09",
    "fbb7714c-4583-4d4d-96f4-369b4515476d",
    "a14fa9cd-bfe0-4c80-a928-0e8d97547e02",
    "5aafd9ac-cb3b-4a21-9952-9baff7a7d3e4",
    "06198bbc-2cab-40c1-b306-692a299452eb",
    "db18bb6e-f763-4c39-a823-a961aa19c5a1",
    "2ebb8fea-f982-43a0-bc95-b0ac01ae3f99",
    "678aa828-c482-4334-b05a-fe618c364226",
    "11074879-0fa1-4bbb-956e-d3d00a47262b"
]


@pytest.mark.parametrize("brewery_id", list_brewery_ids)
def test_get_brewery_by_id(brewery_id):
    url = f'https://api.openbrewerydb.org/v1/breweries?by_ids={brewery_id}'
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json()[0]['id'] == brewery_id


def test_get_list_breweries_by_ids():
    payload = ','.join(list_brewery_ids)
    res = requests.get(f'https://api.openbrewerydb.org/v1/breweries?by_ids={payload}')
    assert res.status_code == 200
    assert len(res.json()) == len(list_brewery_ids)


list_brewery_cities = [
    "South Haven",
    "Kansas City",
    "Watertown",
    "Orlando",
    "La Crosse",
    "Omro",
    "Memphis",
    "Anchorage",
    "Etna",
    "Chico"
]


@pytest.mark.parametrize('city', list_brewery_cities)
def test_search_breweries_by_city(city):
    res = requests.get('https://api.openbrewerydb.org/v1/breweries/search', params={'query': city})
    assert res.status_code == 200
    assert res.json()[0]['city'] == city


list_brewery_names = [
    "Barreled Souls Brewing Company LLC",
    "Full Sail Brewing Co",
    "Dempseys Brewery, Pub",
    "Yee-Haw Brewing, LLC.",
    "The Franciscan Well Brewery",
    "Sanitas Brewing Co",
    "Last Mile Brewery",
    "Sherpa Brewery Pvt. Ltd.",
    "Laurelwood Public House and Brewery - NE",
    "Ass Clown Brewing Co"
]


@pytest.mark.parametrize('name', list_brewery_names)
def test_metadata_breweries_by_name(name):
    res = requests.get('https://api.openbrewerydb.org/v1/breweries/meta', params={'by_name': name})
    assert res.status_code == 200
    assert bool(res.json())
