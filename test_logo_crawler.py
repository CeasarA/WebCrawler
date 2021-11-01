import unittest
import requests
from logo_crawler import get_url

class TestLogoCrawler(unittest.TestCase):
    """"
    Set up test fixed variables
    """
    def setUp(self):
        self.url = "https://nsano.com"
        self.get_url_response = get_url(self.url)

    def test_url_starts_with_https(self):
        """Whether links starts with https"""
        self.assertIsNotNone(self.get_url_response)

    def test_url_exists(self):
        "whether the url exists"
        url_response = requests.get(url=self.url)
        assert url_response.status_code < 400

    def test_check_empty_url(self):
        """ whether the url is empty """
        self.empty_url = ""
        get_url_response = get_url(self.empty_url)
        self.assertEqual(get_url_response, None)

    def test_get_url_returns_an_image(self):
        """whether the get_url function returns an image"""
        
        image_formats = ("image/png", "image/jpeg", "image/jpg")

        for i in range(len(self.get_url_response)):
            response = requests.head(self.get_url_response[i])
            format = response.headers["content-type"] in image_formats
            self.assertEqual(format, True)

    def tearDown(self):
        self.url = ""


if __name__ == '__main__':
    unittest.main()