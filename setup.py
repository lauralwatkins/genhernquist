#!/usr/bin/env python

from setuptools import setup

setup(
    name="genhernquist",
    version="0.0",
    description="A collection of Python functions for generating various quantities for generalised Hernquist profiles.",
    author="Laura L Watkins",
    author_email="lauralwatkins@gmail.com",
    url="https://github.com/lauralwatkins/genhernquist",
    package_dir = {
        "genhernquist": "genhernquist",
    },
    packages=["genhernquist"],
)
