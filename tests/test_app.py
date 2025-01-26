import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True;


    def test_add_new_product(self):
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

    def test_add_invalid_product(self):
        product =  {
            "productName": "",
            "quantity": 0,
            "unitPrice": 0
        }

        response = self.app.post('/shopping_list/add', json=product)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"message": "Invalid product data"})

    def test_delete_product(self):
        response = self.app.delete('/shopping_list/delete/35')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Product deleted successfully!"})
    
    def test_delete_non_existent_product(self):
        response = self.app.delete('/shopping_list/delete/33')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Product not found!"})
    


if __name__ == '__main__':
    unittest.main()


