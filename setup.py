"""Python setup.py for This_Is_Great package"""
import io
import os
from setuptools import find_packages, setup


def read(*names, **kwargs):
    """Read a file."""
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


setup(
    name="This_Is_Great",
    version="0.1.0",
    description="Awesome This_Is_Great created by rochacbruno",
    url="https://github.com/rochacbruno/This_Is_Great/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="rochacbruno",
    packages=find_packages(exclude=["tests"]),
    install_requires=[],
    entry_points={
        "console_scripts": ["This_Is_Great = This_Is_Great.__main__:main"]
    },
    extras_require={
        "test": [
            "pytest",
            "coverage",
            "flake8",
            "black",
            "isort",
            "pytest-cov",
            "codecov",
            "mypy",
            "gitchangelog",
            "mkdocs",
        ],
    },
)
