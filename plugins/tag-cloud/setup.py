#!/usr/bin/env python
from setuptools import setup

requires=['pelican>=3.6.0']

setup(
    name="tag_cloud",
    version="0.0.1",
    url='https://github.com/getpelican/pelican-plugins',
    description="A tool to generate Pelican tag clouds.",
    py_modules=['tag_cloud'],
    install_requires=requires,
)
