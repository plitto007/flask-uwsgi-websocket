#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='Flask-uWSGI-WebSocket',
    version='0.6.1',
    url='https://github.com/plitto007/flask-uwsgi-websocket',
    license='MIT',
    author='Manh Pham',
    author_email='phammanh.bk56@gmail.com',
    description='Fork project from Flask-uWSGI-WebSocket with fixing issues.',
    long_description=open('README.rst').read(),
    py_modules=['flask_uwsgi_websocket'],
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    platforms='any',
    install_requires=[
        'Flask',
        'uwsgi',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='uwsgi flask websockets'
)
