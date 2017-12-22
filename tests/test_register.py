import requests
import unittest
from flask_testing import TestCase
from app import create_app
from app.constants import TEST_HOST, TEST_PORT

host = ''.join(['http://', TEST_HOST, ':', str(TEST_PORT)])


class RegisterTestCase(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_post_register_email_used(self):
        data = {
            'email': '71@qq.com',
            'username': 'wsx',
            'password': '123',
            'nickname': 'kk',
            'class_id': '1718012',
            'csrf_token': False
        }
        url = ''.join([host, '/auth/register'])
        repsonse = requests.post(data=data, url=url).json()
        assert repsonse['status'] == 1000

    def test_post_register_nickname_used(self):
        data = {
            'email': '71ve@qq.com',
            'username': 'wsx',
            'password': '123',
            'nickname': 'kk',
            'class_id': '1718012',
            'csrf_token': False
        }
        url = ''.join([host, '/auth/register'])
        response = requests.post(data=data, url=url).json()
        assert response['status'] == 1001

    def test_post_register(self):
        data = {
            'email': '71e@qq.com',
            'username': 'wsx',
            'password': '123',
            'nickname': 'kkv',
            'class_id': '1718012',
            'csrf_token': False
        }
        response = requests.post(data=data, url='http://127.0.0.1:8847/auth/register').json()

if __name__ == '__main__':
    unittest.main()
