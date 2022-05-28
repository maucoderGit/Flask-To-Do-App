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

        self.assertTrue(response.status_code, 304)

    def test_home_post(self):
        response = self.client.post(url_for('home'))

        self.assertTrue(response.status_code, 405)

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))

        self.assert200(response)

    def test_auth_login_template(self):
        self.client.get(url_for('auth.login'))

        self.assertTemplateUsed('login.html')

    def test_auth_login_post(self):
        self.fake_form = {
            'username': 'dataso',
            'password': 'fake-dataso'
        }

        response = self.client.post(url_for('auth.login'), data=self.fake_form)
        self.assertEqual(response.location, '/')
