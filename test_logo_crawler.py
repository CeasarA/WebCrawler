import os
import unittest
import requests
from logo_crawler import download_image, get_url


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
        # assert url_response.status_code < 400
        self.assertEqual(url_response.status_code, 200)

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


class TestDownloadLogoCrawler(unittest.TestCase):
    def setUp(self):
        """ Set initial values """
        self.links = [
            'https://nsano.com/images/logo.png',
            'https://nsano.com/images/logo.png'
        ]

        self.pathname = "images"
    
    def test_links_and_images_are_right(self):
        """Whether with right inputs, it will download everything 
        """
        status_code = download_image(links=self.links, pathname=self.pathname)
        self.assertEqual(status_code, 200)

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
        os.makedirs(self.new_pathname, exist_ok=True)
        self.assertEqual(os.path.isdir(self.new_pathname), True)    

    def test_empty_link_list(self):
        "Return None if the List"
        self.empty_links = []
        response = download_image(self.empty_links, self.pathname)
        self.assertIsNone(response)

    def test_empty_string_list(self):
        "Return None if the List"
        self.empty_string_links = ['']
        response = download_image(self.empty_string_links, self.pathname)
        self.assertIsNone(response)

    def tearDown(self):
        """Deset the initial values """
        self.pathname = ""
        self.links = []

if __name__ == '__main__':
    unittest.main()