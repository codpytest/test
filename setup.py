import os, sys
import pybind11
from pybind11 import get_cmake_dir
from pybind11.setup_helpers import Pybind11Extension, build_ext

from distutils.core import setup, Extension
from distutils import sysconfig
__version__ = '0.0.6'
cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']
# <%
# cfg['compiler_args'] = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']
# cfg['include_dirs'] = ['C:/libraries/eigen-3.4.0']
# setup_pybind11(cfg)
# %>


ext_modules = [
    Extension(
    'wrap',
        ['src/funcs.cpp', 'src/wrap.cpp','src/inv.cpp'],
        include_dirs=[pybind11.get_include(),
        'src/include'],
    language='c++',
    extra_compile_args = cpp_args,
    define_macros = [('VERSION_INFO', __version__)]
    ),
]

setup(
    name='testing202212',
    version=__version__,
    author='smi',
    author_email='smi@miryusupov.com',
    url="",
    description='testing 2022_',
    long_description_content_type='text/markdown',
    long_description="",
    ext_modules=ext_modules,
    classifiers=["License :: OSI Approved :: MIT License",
                 "Programming Language :: Python :: 3"]
)

#toml
# [tool.cibuildwheel.windows]
# before-all = ["choco install eigen opencv"]
# environment = { OpenCV_DIR="c:/tools/opencv/build" }
# before-build = "pip install delvewheel"
# repair-wheel-command = "delvewheel repair -w {dest_dir} {wheel} --add-path C:/tools/opencv/build/x64/vc15/bin"