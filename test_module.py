import pytest
import requests

def test_url_status(url, status_code):
    try:
        res = requests.get(url)
        assert str(res.status_code) == str(status_code)
    except requests.exceptions.ConnectionError as err:
        pytest.raises(err)