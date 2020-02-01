# Contributing to Jobtimize 🤝
🎊 Firstly, thank you for giving your time to contribute to `Jobtimize`. 🎊

What follows is a simple guide on how to contribute to Jobtimize in a way that makes it easy for everyone.  
Contributions are made only on Github, through *issue* and then *pull request*.

# How to contribute
To contribute to Jobtimize, come and discuss it first by creating an **issue** of the changes you wish to make.  
Please note that all contributions, at any level, are appreciated and everyone is free to discuss. Thus we have a code of conduct to follow for healthy interaction in the project.

There are generally 2 types of contributions: bug and new feature

## Bug report
**Bugs must be treated as a priority.**  
When creating the issue, please describe the bug with an appropriate title. A template is prewritten to help explain the error encountered.

If you also want to help fix this bug, check  
- [x] "I'd like to fix this bug"

We will try to answer you as soon as possible.

## Feature request
Several contributions are grouped in this. To help sort, at the beginning of the title of your issue insert the following keywords according to the contribution:
- `[FORM]` when improving the format/structure of the code
- `[PERF]` when improving performance
- `[DOCS]` when writing/translating docs
- `[SCRP]` when adding/modifying scraping method
- `[CLAS]` when improving text classification
- `[CODE]` anything else about code

A good title would be:
```
[SCRP] Add Job-Hunt scrapping
```

Then, just follow the template to make a simple description of the feature.

We will answer very quickly.

# Pull Request
## Create your branch
1. The best way to work is to fork the [repository](https://github.com/Lrakotoson/Jobtimize), ideally on a fork of the master branch if it is an independent feature or a specific branch for a development associated with it.  

2. Clone your fork from the repository to your local storage. Keep it synchronized with the original repository in case of major changes using an upstream: [Learn more](https://help.github.com/en/github/getting-started-with-github/fork-a-repo).
```bash
$ git clone git@github.com:USERNAME/Jobtimize.git
$ cd Jobtimize
```

3. Create a specific branch for your `feature` where you will implement it. Creating a branch allows you to perform tests without the risk of affecting the main program.
```bash
$ git pull
$ git checkout -b my-feature
```
4. Implement your code in a clear way *(explained in the following)*, commit everything and push your branch to your fork.  
Finally, make a pull request to the original Jobtimize repository [this way](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork)  
Please leave checked the option
- [x] Allow edits from maintainers
```bash
$ git add implemented-files
$ git commit
$ git push origin my-feature
```

## Setup the feature
The architecture of Jobtimize is quite special.  
For a python module `Jobtimize/module.py`, there is a **jupyter notebook** `docs/module.ipynb`.
The aim is to have a clearer explanation of the codes so that everyone can understand them more easily.

The ideal would be to have an explanation, or even a narration of what the developer thought, for each function/method and a main example.  
Starting by working on the notebook and then putting all the code into a script would be a good way to do it.

Of course, this is not a constraint, everyone is free to write as he wants but in the spirit of everyone's understanding.

## Format Pull Request
Following the feature request pattern in the issue associated with it, its associated Pull Request must have the same title but with a keyword in addition:
- `[MRG]` when the branch is ready for merge and therefore for a review first.
- `[WIP]` when the work is in progress. Once done, the title will have to pass to `[MRG]`.

A good example of a title would be:
```
[MRG] [SCRP] Add Job-Hunt scrapping
```
Please leave checked the option
- [x] Allow edits from maintainers

