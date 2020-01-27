# -*- coding: utf-8 -*-

from setuptools import setup
import Jobtimize

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = "Jobtimize",
    packages = ["Jobtimize"],
    version = Jobtimize.__version__,
    install_requires = requirements,
    author = "Loïc Rakotoson",
    author_email = "contact@loicrakotoson.com",
    url = "https://github.com/Lrakotoson/Jobtimize",
    description = "Collect and standardize data on job posting platforms.",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "Operating System :: OS Independent"
    ]

)