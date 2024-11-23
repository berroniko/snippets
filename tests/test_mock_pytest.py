import requests


class ToBeMocked:

    def __init__(self, urls: dict):
        self.urls = urls
        self.result = None

    def my_method(self):
        url = self.urls.get("myIP")
        r = requests.get(url)
        self.result = r.json()


def test_tbm(monkeypatch):
    class MockResponse:
        @staticmethod
        def json():
            return {'origin': '94.134.109.79'}

    def mock_get(*args, **kwargs):
        return MockResponse

    monkeypatch.setattr(requests, "get", mock_get)

    urls = {"myIP": "https://httpbin.org/wrong"}
    tbm_mocked = ToBeMocked(urls=urls)
    tbm_mocked.my_method()
    assert tbm_mocked.result == {'origin': '94.134.109.79'}
