import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-tellafriend",
    version = __import__('tellafriend').get_version(),
    author = "Philipp Bosch",
    author_email = "hello@pb.io",
    description = "Tell-a-friend functionality for Django-based websites",
    license = "MIT",
    keywords = "django tellafriend recommend",
    url = "http://github.com/philippbosch/django-tellafriend/",
    packages=find_packages(),
    package_data={
        'tellafriend': [
            'templates/tellafriend/*.html',
            'templates/tellafriend/*.txt',
        ],
    },
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
    ],
)