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
        "test whether the url exists"
        url = "https://nsano.com"
        get_url(url)
        url_response = requests.get(url=url)
        assert url_response.status_code < 400

    def test_get_url_return_a_list(self):
        url = "https://nsano.com"
        image_formats = ("image/png", "image/jpeg", "image/jpg")
        return_value = get_url(url)
        r = requests.head(return_value)
        format = r.headers["content-type"] in image_formats
        print(format)
        self.assertEqual(url, return_value)

if __name__ == '__main__':
    unittest.main()