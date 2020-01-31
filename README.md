# Jobtimize
`Jobtimize` is a python package which collects, standardizes and completes information about job offers published on job search platforms.
The package is mainly based on scraping and text classification to fill in missing data.


|Release|Usage|Development|
|---	|---  |---	      |
|[![PyPI](https://img.shields.io/pypi/v/Jobtimize?logo=PyPI&style=for-the-badge&labelColor=%233775A9&logoColor=white)](https://pypi.org/project/Jobtimize/)|[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)|[![Build Status](https://img.shields.io/travis/com/Lrakotoson/Jobtimize/master.svg?style=for-the-badge&logo=Travis-CI&logoColor=white)](https://travis-ci.com/Lrakotoson/Jobtimize)|
|[![Conda](https://img.shields.io/conda/v/lrakotoson/jobtimize?label=CONDA&logo=anaconda&style=for-the-badge)](https://anaconda.org/lrakotoson/jobtimize)|[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Jobtimize?logo=python&logoColor=yellow&style=for-the-badge)](https://pypi.org/project/Jobtimize/)|[![Codecov](https://img.shields.io/codecov/c/gh/Lrakotoson/Jobtimize?logo=Codecov&style=for-the-badge)](https://codecov.io/gh/Lrakotoson/Jobtimize/)|
|![PyPI - Status](https://img.shields.io/pypi/status/Jobtimize?style=for-the-badge)|   	|[![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python&labelColor=yellow)](https://www.python.org/)|

# Dependencies

```
beautifulsoup4
jsonschema
lxml
pandas
```

# Installation
## Pypi
The safest way to install `Jobtimize` is to go through pip
```bash
pip install Jobtimize
```

## Conda
It is also possible to get the latest stable version with Anaconda Cloud
```bash
conda install -c lrakotoson jobtimize
```

## Git
The installation with git allows to have the latest version. However it can have some bugs.
```bash
pip install git+https://github.com/Lrakotoson/Jobtimize.git
```

# How to use ?
Since `Jobtimize` is a package, in python you just have to import it.
The main function (*for now*) is `Jobtimize.jobscrap`.
```python
from Jobtimize import jobscrap

df = jobscrap(["Data Scientist", "Data Analyst"],
              ["UK", "FR"]
    )

df.head()
```
The `df` object is a dataframe pandas, so it inherits all its methods.

# Contributing 🤝
🎊 Firstly, thank you for giving your time to contribute to `Jobtimize`. 🎊

If you have a new feature to submit, don't hesitate to **open an issue** _(By checking "new feature" to make it easier to read)_ We can discuss it freely there.  
Then you can make a "pull request" as explained in the [contribution guidelines](https://github.com/Lrakotoson/Jobtimize/blob/master/docs/CONTRIBUTING.md).

Same for all contributions, code improvement, documentation writing, translations... **all ideas are welcome!** Check out the [guidelines](https://github.com/Lrakotoson/Jobtimize/blob/master/docs/CONTRIBUTING.md) to make it easier.

`Jobtimize` gets better with contributions.