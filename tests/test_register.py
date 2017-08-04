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

    def test_post_register(self):
        data = {
            'email': '71@qq.com',
            'username': 'wsx',
            'password': '123',
            'nickname': 'kk',
            'class_number': '1718012',
            'csrf_token': False
        }
        repsonse = requests.post(data=data, url='http://127.0.0.1:8847/auth/register')
        assert '1000' in repsonse.text



if __name__ == '__main__':
    unittest.main()
