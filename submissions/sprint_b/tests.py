import unittest
from flask_testing import TestCase
from app import app


class TestFlaskResponses(TestCase):

    def create_app(self):
        self.app = app
        return self.app

    def test_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_vocab(self):
        response = self.client.get('/vocabulary')
        self.assertEqual(response.status_code, 200)

    # def test_mult_epithets(self):
    #     response = self.client.get


if __name__ == "__main__":
    unittest.main()
