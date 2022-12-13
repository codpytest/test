#! /usr/bin/env python
#
# Copyright (C) 

from setuptools import setup, Extension, Command
from setuptools import setup, find_packages
from __future__ import annotations
from distutils.core import setup
from distutils import sysconfig
import os,sys
from shutil import copy
__version__ = '0.1.7'





setup(ext_modules=[Extension(name="printf", sources=["src/printf.c"])])