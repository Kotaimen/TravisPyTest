#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='TravisPyTest',
    version='0.0.2.dev0',
    description='A Python Travis-CI Test',
    long_description='Yes, a complicated python travis-ci test, with geo goodies',
    author='kotaimen',
    author_email='kotaimen.c@gmail.com',
    url='',
    license='',
    platforms=['linux'],
    packages=find_packages(exclude=['tests']),
    test_suite='tests',
    install_requires=[
        'python-memcached>=1.5.3',
        'shapely>=1.5',
        'psycopg2>=2.5'
    ],
    tests_require=[
        'nose>=1.3',
        'coverage>=3.7',
    ],
    classifiers=[
    ],
)
