import sys; print(sys.executable)
import pytest
import mock
from getmyip.getmyip import getip

@mock.patch('getmyip.getmyip.requests')
def test_working(requests_mock):
    requests_mock.get.return_value.json.return_value = {'ip': '1.1.1.1'}
    assert getip(url='foo.com') == '1.1.1.1'

if __name__ == '__main__':
    test_working()
