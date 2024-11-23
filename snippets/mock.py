from unittest import mock

import requests


def get_ip():
    response = requests.get("https://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()['origin']


# get_ip()


mock_response = mock.Mock()
mock_response.json.return_value = {'origin': '0.0.0.0'}
mock_response.status_code = 200

# alternative way to define the mock
mock_response_2 = mock.Mock(name='mock response 2', **{'status_code': 200, 'json.return_value': {'origin': '0.1.2.3'}})

mock_requests_get = mock.Mock(return_value=mock_response_2)

print(f'just the mocked requests.get {mock_requests_get().json()}')

requests.get = mock_requests_get

print(f'and the mocked get_ip() returns:  {get_ip()}')

# to ensure the mock was called with the expected arguments:
mock_requests_get.assert_called_with('https://httpbin.org/ip')


# in the later test

@mock.patch("requests.get")  # must be the full local path to the function tested (usually in different folder)
def test_get_ip(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="mock response",
                                               **{'status_code': 200, 'json.return_value': {'origin': '0.0.0.0'}})

    assert get_ip() == "0.0.0.0"
    mock_requests_get.assert_called_once_with("https://httpbin.org/ip")
