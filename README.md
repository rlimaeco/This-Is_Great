
> HOW TO USE THIS TEMPLATE

1. Click on 'Use this template' or go to https://github.com/rochacbruno/python-project-template/generate
2. Wait until the first run of CI finishes (Github Actions will process the template and commit to your new repo)
3. If you want coverage reports and automatic release to PyPI
  On repository `settings->secrets` add your `PIPY_API_TOKEN` and `CODECOV_TOKEN` (get the tokens on respective websites)
4. Read the file `CONTRIBUTING.md`
5. Then clone your new project and start coding!

What is included?

- A full feature Makefile with common targets to:
  - lint all python files
  - run all tests
  - run all tests and coverage report
  - format code using black
  - run mypy
  - release to github and pypi
  - create a virtualenv and install project for development
- A basic project structure with
  - `.gitignore`
  - Github Actions CI
  - `setup.py` with common parameters
  - Changelog generation
  - basic test structure using `pytest`
  - Entry point to run `$ This_Is_Great`
  - Entry point to run `$ python -m This_Is_Great`
- Basic documentation structure using `mkdocs`
- Integration with `codecov` and `pypi`

> Delete all lines above this ^^^

---
# This_Is_Great

[![codecov](https://codecov.io/gh/rochacbruno/This_Is_Great/branch/main/graph/badge.svg?token=I9ZGCFTQT9)](https://codecov.io/gh/rochacbruno/This_Is_Great)
[![CI](https://github.com/rochacbruno/This_Is_Great/actions/workflows/main.yml/badge.svg)](https://github.com/rochacbruno/This_Is_Great/actions/workflows/main.yml)

Awesome This_Is_Great created by rochacbruno

## Install it from PyPI

```bash
pip install This_Is_Great
```

## Usage

```py
from This_Is_Great import BaseClass
from This_Is_Great import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m This_Is_Great
#or
$ This_Is_Great
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
