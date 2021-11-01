import unittest
from unittest.mock import Mock
from logo_crawler import get_url



class TestLogoCrawler(unittest.TestCase):
    def test_get_url(self):
        url = get_url("https://nsano.com")
        assert url == "nsano.com"





if __name__ == 'main':
    unittest.main()