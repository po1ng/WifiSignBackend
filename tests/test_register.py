import requests
import unittest
from flask_testing import TestCase
from app import create_app


class RegisterTestCase(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_auth_logout(self):
        response = requests.get('http://127.0.0.1:8847/auth/logout')
        assert 'hello logout' in response.text

    def test_post_register_email_used(self):
        data = {
            'email': '71@qq.com',
            'username': 'wsx',
            'password': '123',
            'nickname': 'kk',
            'class_number': '1718012',
            'csrf_token': False
        }
        repsonse = requests.post(data=data, url='http://127.0.0.1:8847/auth/register').json()
        assert repsonse['status'] == 1000

    def test_post_register_nickname_used(self):
        data = {
            'email': '71ve@qq.com',
            'username': 'wsx',
            'password': '123',
            'nickname': 'kk',
            'class_number': '1718012',
            'csrf_token': False
        }
        response = requests.post(data=data, url='http://127.0.0.1:8847/auth/register').json()
        assert response['status'] == 1001

    def test_post_register(self):
        data = {
            'email': '71e@qq.com',
            'username': 'wsx',
            'password': '123',
            'nickname': 'kkv',
            'class_number': '1718012',
            'csrf_token': False
        }
        response = requests.post(data=data, url='http://127.0.0.1:8847/auth/register').json()
        # assert response['status'] == 0
if __name__ == '__main__':
    unittest.main()
