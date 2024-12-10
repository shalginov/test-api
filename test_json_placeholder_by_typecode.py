import pytest
import requests
import random

list_datas = [
    {
        "title": "Practice speech nature.",
        "body": "Character area I continue should. Middle short father something.\nTreat forward will cup job behind happy.",
        "userId": 6
    },
    {
        "title": "Suggest community management.",
        "body": "Once peace affect throw.\nWonder relationship customer page organization participant back. Scientist serve realize himself. Feel probably message move democratic tree.",
        "userId": 6
    },
    {
        "title": "Partner above despite.",
        "body": "Commercial either star information believe model. Sea reduce like fine. Success brother school might message discussion.",
        "userId": 1
    },
    {
        "title": "Manager resource night.",
        "body": "Agency young American occur. Read economy question discover activity word type property. Painting air parent.",
        "userId": 4
    },
    {
        "title": "Far source.",
        "body": "But claim take exactly goal list window. Course game couple check explain senior.\nSocial many rule moment plan involve. Interesting job ever. Investment room government of through.",
        "userId": 2
    },
    {
        "title": "Effect moment.",
        "body": "Break research indeed person difficult. Would ask require ground management. Trouble skill enter month low. Early happy home collection memory war owner.",
        "userId": 6
    }
]


def test_get_random_post():
    rnd = random.randrange(1, 100)
    res = requests.get(f'https://jsonplaceholder.typicode.com/posts/{rnd}')
    assert res.status_code == 200
    assert res.json()['id'] == rnd


@pytest.mark.parametrize('data', list_datas)
def test_create_post(data):
    res = requests.post('https://jsonplaceholder.typicode.com/posts', data=data)
    assert res.status_code == 201
    assert bool(res.json()['id']) == True


@pytest.mark.parametrize('data', list_datas)
def test_update_post(data):
    post_number = random.randrange(1, 100)
    data_with_post_number = {
        'id': post_number,
        'title': data['title'],
        'body': data['body'],
        'userId': data['userId']
    }
    res = requests.put(f'https://jsonplaceholder.typicode.com/posts/{post_number}', data=data_with_post_number)
    assert res.status_code == 200
    assert bool(res.json()['id']) == True

    res_upd = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_number}')
    assert res_upd.json() == data_with_post_number


@pytest.mark.parametrize('data', list_datas)
def test_patch_post(data):
    post_number = random.randrange(1, 100)
    data_to_patch = {
        'title': data['title']
    }
    res = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{post_number}', data=data_to_patch)
    assert res.status_code == 200
    assert bool(res.json()['title']) == True


def test_delete_post():
    post_number = random.randrange(1, 100)
    res = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_number}')
    assert res.status_code == 200
