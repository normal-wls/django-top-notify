# -*- coding: utf-8 -*-
import os
from codecs import open
from setuptools import find_packages, setup

with open(
    os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8"
) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-top-notify",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/normal-wls/django-top-notify",
    description="A top notification bar based on Django project",
    long_description=README,
    long_description_content_type="text/markdown",
    author="waylon",
    author_email="1158341873@qq.com",
    install_requires=[],
    zip_safe=False,
)
