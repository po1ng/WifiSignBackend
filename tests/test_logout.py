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

    def test_logout(self):
        data = {
            'email': '89898989@qq.com',
            'password': '123'
        }
        web_session = requests.session()
        login_url = ''.join([host, '/auth/login'])
        web_session.post(data=data, url=login_url)
        logout_url = ''.join([host, '/auth/logout'])
        reponse = web_session.get(url=logout_url).json()
        assert reponse['status'] == 1

if __name__ == '__main__':
    unittest.main()