import os, sys

from distutils.core import setup, Extension
from distutils import sysconfig

cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']

ext_modules = [
    Extension(
    'wrap',
        ['src/funcs.cpp', 'src/wrap.cpp'],
        include_dirs=['pybind11/include'],
    language='c++',
    extra_compile_args = cpp_args,
    ),
]

setup(
    name='testing202212',
    version='0.0.1',
    author='smi',
    author_email='smi@miryusupov.com',
    url="",
    description='testing 2022_',
    long_description="",
    ext_modules=ext_modules,
)