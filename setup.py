# from __future__ import annotations
from setuptools import Extension
from setuptools import setup
__version__ = '0.0.1'





setup(ext_modules=[Extension(name="printf", sources=["src/printf.c"])])