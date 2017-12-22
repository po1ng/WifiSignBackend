import requests
import unittest
from flask_testing import TestCase
from app import create_app
from app.constants import TEST_PORT, TEST_HOST

host = ''.join(['http://', TEST_HOST, ':', str(TEST_PORT)])


class RegisterTestCase(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_login_faild(self):
        data = {
            'email': '889988@qq.com',
            'password': '123'
        }
        web_session = requests.session()
        url = ''.join([host, '/auth/login'])
        response = web_session.post(data=data, url=url).json()
        assert response['status'] == 1003

    def test_login_success(self):
        data = {
            'email': '89898989@qq.com',
            'password': '123'
        }
        web_session = requests.session()
        url = ''.join([host, '/auth/login'])
        response = web_session.post(data=data, url=url).json()
        assert response['status'] == 1

if __name__ == '__main__':
    unittest.main()