'''
Created on Feb 20, 2016

@author: Steve Posick
'''
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'Fibonacci Microservice',
    'description': 'Fibonacci Microservice',
    'author': 'Steve Posick',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'posicks@gmail.com',
    'version': '1.0',
    'install_requires': ['flask'],
    'py_modules': ['fibonacci', 'endpoints', 'tests'],
    'packages': ['fibonacci', 'endpoints',  'tests'],
    'scripts': []
}

setup(**config)