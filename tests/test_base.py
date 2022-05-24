from flask import current_app, url_for
from flask_testing import TestCase

from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    def test_app_exist(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'], True)

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))

        self.assertEqual(response.location, '/home')

    def test_home_get(self):
        response = self.client.get(url_for('home'))

        self.assert200(response)

    def test_home_post(self):
        fake_form: dict[str] = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('home'), data=fake_form)

        self.assertEqual(response.location, '/')