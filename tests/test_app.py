import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True;

    def test_view_Products(self):
        response = self.app.get('/shopping_list/view')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])




if __name__ == '__main__':
    unittest.main()
