import datetime
import re

from httpie_vimond_auth import *


def test_get_auth_headers():
    plugin = VimondAuthPlugin()
    request = MockRequest()
    request.headers['date'] = 'Tue, 10 Nov 2009 23:00:00 +0000'

    auth = plugin.get_auth('xyz', '123')
    result = auth(request)

    assert result.headers == {
        'date': 'Tue, 10 Nov 2009 23:00:00 +0000',
        'Authorization': 'SUMO xyz:6hJ55znNIpZBWG6kDweLxr++bWQ='
    }


def test_date_format():
    plugin = VimondAuthPlugin()
    request = MockRequest()

    auth = plugin.get_auth('user', 'secret')
    result = auth(request)

    assert re.match(
        r'^[a-zA-Z]{3}, \d\d [a-zA-Z]{3} \d\d\d\d \d\d:\d\d:\d\d \+\d\d\d\d$',
        result.headers['Date'])


class MockRequest:
    def __init__(self):
        self.method = 'GET'
        self.headers = {}
        self.url = 'foo'
