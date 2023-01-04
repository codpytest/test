import os, sys
import pybind11
from pybind11 import get_cmake_dir
from pybind11.setup_helpers import Pybind11Extension, build_ext

from distutils.core import setup, Extension
from distutils import sysconfig
__version__ = '0.0.17'
cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']


ext_modules = [
    Extension(
    'inv',
        ['src/inv.cpp'],
        include_dirs=[pybind11.get_include(),
        'src/include'],
    language='c++',
    #extra_compile_args = cpp_args,
    define_macros = [('VERSION_INFO', __version__)]
    ),
]

setup(
    name='testing202212',
    version=__version__,
    author='smi',
    author_email='smi@miryusupov.com',
    url="https://pypi.org/project/testing202212/",
    description='testing 2022_',
    long_description_content_type='text/markdown',
    long_description="",
    ext_modules=ext_modules,
    classifiers=["License :: OSI Approved :: MIT License",
                 "Programming Language :: Python :: 3"]
)
