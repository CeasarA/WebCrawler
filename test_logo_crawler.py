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
        self.assertAlmostEqual(self.url.startswith("https"), True)

    def test_url_exists(self):
        "whether the url exists"
        # get_url(self.url)
        url_response = requests.get(url=self.url)
        assert url_response.status_code < 400

    def test_get_url_returns_an_image(self):
        "whether the get_url function returns an image"
        image_formats = ("image/png", "image/jpeg", "image/jpg")
        r = requests.head(self.get_url_response)
        format = r.headers["content-type"] in image_formats
        self.assertEqual(format, True)


    def tearDown(self) -> None:
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()