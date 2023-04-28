import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_empty_wallet(self):
        response = self.app.get('/?wallet=')
        self.assertIn(b'No nodes are running on this wallet address', response.data)
    

    def test_404(self):
        response = self.app.get('/invalid-url')
        self.assertEqual(response.status_code, 404)
        
if __name__ == '__main__':
    unittest.main()        