#!/usr/bin/env python

from setuptools import setup

setup(
    name="genids",
    version="0.0.1",
    description="Create a column of unique integers",
    author="Adam Hooper",
    author_email="adam@adamhooper.com",
    url="https://github.com/CJWorkbench/genids",
    packages=[""],
    py_modules=["genids"],
    install_requires=["pandas==0.25.3", "cjwmodule>=1.4.0"],
)
