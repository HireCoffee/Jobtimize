# -*- coding: utf-8 -*-

from setuptools import setup
import Jobtimize

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = "Jobtimize",
    version = Jobtimize.__version__,
    install_requires = requirements,
    author = "Loïc Rakotoson",
    author_email = "contact@loicrakotoson.com",
    description = "Collect and standardize data on job posting platforms.",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",

)