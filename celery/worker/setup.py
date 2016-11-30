# -*- coding: utf-8 -

import os
import sys

from setuptools import setup, find_packages

CLASSIFIERS = []

setup(
    name='worker',
    version="0.1.0",

    description='Celery Worker Service',
    long_description='',
    author='Petar Efnushev',
    author_email='petar.efnushev@keitaro.com',
    classifiers=CLASSIFIERS,
    zip_safe=False,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    entry_points=""""""
)
