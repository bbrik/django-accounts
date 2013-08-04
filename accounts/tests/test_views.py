# -*- coding: utf-8 -*-

from django.test import TestCase


class AccountsViewsTestCase(TestCase):
    def setUp(self):
        pass

    def test_login(self):
        self.assertEqual(1+1, 2)