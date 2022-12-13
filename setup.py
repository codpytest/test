#! /usr/bin/env python
#
# Copyright (C) 

from __future__ import annotations
from setuptools import setup, Extension, Command
__version__ = '0.0.1'





setup(ext_modules=[Extension(name="printf", sources=["src/printf.c"])])