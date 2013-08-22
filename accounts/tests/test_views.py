# -*- coding: utf-8 -*-

import re
from urlparse import urlparse

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core import mail

from ..base import LOGOUT_REDIRECT_URL, PASSWORD_CHANGE_REDIRECT_URL, \
    PASSWORD_RESET_REDIRECT_URL


URL_RE = re.compile(r"""((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.‌​][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))*))+(?:(([^\s()<>]+|(‌​([^\s()<>]+)))*)|[^\s`!()[]{};:'".,<>?«»“”‘’]))""", re.DOTALL)


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

    def test_password_reset(self):
        url = reverse('accounts:password_reset')
        response = self.client.post(url, data={'email': 'steve@gmail.com'})
        self.check_redirect_to_url(response, PASSWORD_RESET_REDIRECT_URL)
        self.assertEquals(len(mail.outbox), 1)
        # find url message text
        message = mail.outbox[0]
        match = URL_RE.search(message.body)
        url = match.group(0)
        path = urlparse(url).path[:-1] # remove last " from end of url
        # test set new password
        response = self.client.post(path, data={'new_password1': '67890',
                                                'new_password2': '67890'})
        self.check_redirect_to_url(response, PASSWORD_RESET_REDIRECT_URL)
        self.check_no_user_logged_in()
        self.client.login(username='steve', password='67890')
        self.check_user_logged_in()
