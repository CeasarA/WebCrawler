import unittest
import requests
from logo_crawler import get_url


class TestLogoCrawler(unittest.TestCase):
    """"
    Set up test fixed variables
    """
    def stepUp(self):
        self.url = 'https://nsano.com'

    def test_url_starts_with_https(self):
        """Whether links starts with https"""
        url = "https://nsano.com"
        self.assertAlmostEqual(url.startswith("https"), True)

    def test_url_exists(self):
        url = "https://nsano.com"
        get_url(url)
        url_response = requests.get(url=url)
        assert url_response.status_code < 400


if __name__ == '__main__':
    unittest.main()