import unittest
import requests

class MainTest(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost/'
        self.response = requests.get(self.url)
        self.status_code = self.response.status_code

    def testIsWebsiteUp(self):
        status_code = self.status_code
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()
