# Based on setup.py master example at https://github.com/pypa/sampleproject/blob/master/setup.py

from io import open
from os import path

from setuptools import setup, find_packages

import mailcheck

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django-mailcheck",
    version=mailcheck.__version__,
    description="Pluggable Django email backend for capturing outbound mail for QA/review purposes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shacker/django-mailcheck",
    author="Scot Hacker",
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Email :: Post-Office",
    ],
    keywords="email django QA",
    packages=find_packages(),  # Finds modules with an __init__.py
    include_package_data=True,  # Pulls in non-module data from MANIFEST.in
    python_requires=">=3.5",
    install_requires=["unidecode"],
    project_urls={
        "Bug Reports": "https://github.com/shacker/django-mailcheck/issues",
        "Source": "https://github.com/shacker/django-mailcheck",
    },
)
