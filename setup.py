# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import accounts


setup(
    name='django-accounts',
    version=accounts.__version__,
    author=u'Bernardo Brik',
    author_email='bernardobrik@gmail.com',
    url='http://bitbucket.org/bruno/django-geoportail',
    description='Simple registration with bootstrap forms',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
)
