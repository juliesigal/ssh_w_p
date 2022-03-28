from InvalidUrlException import InvalidUrlException
import pytest
import requests



@pytest.mark.parametrize('url, expected', [('https://google.com', True),
                                           ('https://stackoverflow.com', True),
                                           ('https://www.youtube.com', True)])
def test_check_url(url, expected):
    requests.get(url, stream=True)
    requests.status_code = 200
    assert expected

# def test_url_invalid():
#     with pytest.raises(InvalidUrlException):
#         requests.get('uhrjllhhh', stream=True)
#         requests.status_codes = 200