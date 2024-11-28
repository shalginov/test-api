import pytest
import requests
import random

def test_get_random_image():
    res = requests.get('https://dog.ceo/api/breeds/image/random')
    assert res.status_code == 200
    assert res.json()['status'] == 'success'

def test_get_random_images():
    for i in range(3):
        rnd = random.randrange(1,50)
        url = f'https://dog.ceo/api/breeds/image/random/{rnd}'
        res = requests.get(url)
        assert res.status_code == 200
        assert res.json()['status'] == 'success'
        assert len(res.json()['message']) == rnd

def test_get_all_breeds():
    res = requests.get('https://dog.ceo/api/breeds/list/all')
    assert res.status_code == 200
    assert res.json()['status'] == 'success'


breeds_list = [
'affenpinscher',
'basenji',
'akita',
]

@pytest.mark.parametrize('breed', breeds_list)
def test_get_random_image_by_breed(breed):
    url = f'https://dog.ceo/api/breed/{breed}/images/random'
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json()['status'] == 'success'

sub_breeds_list = [
'buhund/norwegian',
'collie/border',
'pointer/germanlonghair',
]

@pytest.mark.parametrize('sub_breed', sub_breeds_list)
def test_get_random_image_by_sub_breed(sub_breed):
    url = f'https://dog.ceo/api/breed/{sub_breed}/images/random'
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json()['status'] == 'success'
