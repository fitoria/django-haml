#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

import os

install_requires = [
    'hamlpy',
]

setup(
    name = "django-haml",
    version = "0.1",
    url = "http://github.com/fitoria/django-haml",
    licence = 'MIT',
    description = 'Django haml management command.',
    author = 'Adolfo Fitoria',
    author_email = 'adolfo.fitoria@gmail.com',
    install_requires = install_requires,
    packages = ['haml', 
                'haml.management',
                'haml.management.commands'],
    include_package_data = True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Licence :: OSI Approved :: MIT Licence',
        'Programming Languaje :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
