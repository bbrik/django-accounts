# -*- coding: utf-8 -*-

from urlparse import urlparse

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from ..base import LOGOUT_REDIRECT_URL, PASSWORD_CHANGE_REDIRECT_URL


class AccountsViewsTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('steve', 'steve@gmail.com', '12345')

    def check_user_logged_in(self):
        self.assertIn('_auth_user_id', self.client.session)

    def check_no_user_logged_in(self):
        self.assertNotIn('_auth_user_id', self.client.session)

    def check_redirect_to_url(self, response, url):
        self.assertEqual(response.status_code, 302)
        path = urlparse(response['location']).path
        self.assertEqual(path, url)

    def test_login(self):
        url = reverse('accounts:login')
        self.check_no_user_logged_in()
        self.client.post(url, data={'username': 'steve', 'password': '12345'})
        self.check_user_logged_in()

    def test_logout(self):
        url = reverse('accounts:logout')
        self.client.login(username='steve', password='12345')
        self.check_user_logged_in()
        response = self.client.get(url)
        self.check_no_user_logged_in()
        self.check_redirect_to_url(response, LOGOUT_REDIRECT_URL)

    def test_password_change(self):
        url = reverse('accounts:password_change')
        self.client.login(username='steve', password='12345')
        response = self.client.post(url, data={
            'old_password': '12345',
            'new_password1': '67890',
            'new_password2': '67890',
        })
        self.check_redirect_to_url(response, PASSWORD_CHANGE_REDIRECT_URL)
        self.client.logout()
        self.client.login(username='steve', password='67890')
