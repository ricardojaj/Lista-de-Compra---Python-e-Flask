import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True;


    def test_adc_new_product(self):
        product =  {
            "productName": "PAO",
            "quantity": 1,
            "unitPrice": 7
        }

        response = self.app.post('/shopping_list/add', json=product)
        self.assertEqual(response.status_code, 201)

        data = response.json
        self.assertIn('id', data['data'][0]) 
        self.assertEqual(data['data'][0]['productName'], 'PAO')  
        self.assertEqual(data['data'][0]['quantity'], 1)    
        self.assertEqual(data['data'][0]['unitPrice'], 7) 
  
"""    def test_view_products(self):
        response = self.app.get('/shopping_list/view')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])
"""       
if __name__ == '__main__':
    unittest.main()

