# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import accounts


setup(
    name='django-accounts',
    version=accounts.__version__,
    author=u'Bernardo Brik',
    author_email='bernardobrik@gmail.com',
    url='https://github.com/bbrik/django-accounts',
    description='Simple registration with bootstrap forms',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
)
