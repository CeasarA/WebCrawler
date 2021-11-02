import os
import unittest
import requests
from logo_crawler import download_image, get_url


# class TestLogoCrawler(unittest.TestCase):
#     """"
#     Set up test fixed variables
#     """
#     def setUp(self):
#         self.url = "https://nsano.com"
#         self.get_url_response = get_url(self.url)

#     def test_url_starts_with_https(self):
#         """Whether links starts with https"""
#         self.assertIsNotNone(self.get_url_response)

#     def test_url_exists(self):
#         "whether the url exists"
#         url_response = requests.get(url=self.url)
#         # assert url_response.status_code < 400
#         self.assertEqual(url_response.status_code, 200)

#     def test_check_empty_url(self):
#         """ whether the url is empty """
#         self.empty_url = ""
#         get_url_response = get_url(self.empty_url)
#         self.assertEqual(get_url_response, None)

#     def test_get_url_returns_an_image(self):
#         """whether the get_url function returns an image"""
        
#         image_formats = ("image/png", "image/jpeg", "image/jpg")

#         for i in range(len(self.get_url_response)):
#             response = requests.head(self.get_url_response[i])
#             format = response.headers["content-type"] in image_formats
#             self.assertEqual(format, True)

#     def tearDown(self):
#         self.url = ""


class TestDownloadLogoCrawler(unittest.TestCase):
    def setUp(self):
        """ Set initial values """
        self.links = []
        self.pathname = "images"
    
    def test_path_exists(self):
        """
        Should return true since the file exists
        """
        self.assertTrue(os.path.isdir(self.pathname))
    
    def test_new_path(self):
        """
        Should create a new path since it does not exists
        """
        self.new_pathname = 'try_folder'
        os.makedirs(self.new_pathname, exist_ok=False)
        self.assertEqual(os.path.isdir(self.new_pathname), True)    

    def tearDown(self):
        """Deset the initial values """
        self.pathname = ""


# url = TestLogoCrawler
download = TestDownloadLogoCrawler


if __name__ == '__main__':
    unittest.main()