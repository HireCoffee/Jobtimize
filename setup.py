# -*- coding: utf-8 -*-

import setuptools
import Jobtimize


setuptools.setup(
    name = "Jobtimize",
    packages = ["Jobtimize"],
    version = Jobtimize.__version__,
    install_requires = ["beautifulsoup4", "pandas", "jsonschema", "lxml", "requests"],
    author = "Loïc Rakotoson",
    author_email = "contact@loicrakotoson.com",
    url = "https://loicrakotoson.com/Jobtimize/",
    description = "Collect and standardize data on job posting platforms.",
    long_description = open("README.md", encoding="utf8").read(),
    long_description_content_type = "text/markdown",
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "Topic :: Database",
        "Topic :: Education",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'

)