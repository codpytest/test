#! /usr/bin/env python
#
# Copyright (C) 

from setuptools import setup, Extension, Command
from setuptools import setup, find_packages
from distutils.core import setup
from distutils import sysconfig
import os,sys
from shutil import copy
__version__ = '0.1.7'

DISTNAME = 'test'
DESCRIPTION = 'Test'
MAINTAINER = 'BB'
MAINTAINER_EMAIL = 'bg'
URL = 'www.appleworld.com'
#DOWNLOAD_URL = 'https://github.com/johnlem/codpy_alpha'
LICENSE = 'new BSD'
PROJECT_URLS = {
    'Bug Tracker': 'https://github.com/johnlem/codpy_alpha/issues',
    'Documentation': 'https://',
    'Source Code': 'https://github.com/johnlem/codpy_alpha'
}

#codpy_path = os.path.dirname(__file__)
#codpy_path = os.path.join(codpy_path,"codpy")

# def package_files(directory):
    # paths = []
    # for (path, directories, filenames) in os.walk(directory):
        # for filename in filenames:
            # paths.append(os.path.join('..', path, filename))
    # return paths

#extra_files = package_files(codpy_path)
long_description = open("README.md","r").read()

print("find_packages():",find_packages(),)



cmdclass = {}
ext_modules = []
include_dirs = []


# Build extension with previously Cython generated source.
# ext_modules.append(Extension("printf", ["codpy/printf.c"]))




setup(
    name=DISTNAME,
    version=__version__,
    author=MAINTAINER,
    maintainer=MAINTAINER,
    author_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    packages= find_packages(),
    include_package_data=True,
    #package_data={'': extra_files},
    classifiers=[
        # trove classifiers
        # the full list is here: https://pypi.python.org/pypi?%3aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        #'Environment :: Win32 (MS Windows)',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
       # 'Operating System :: Microsoft :: Windows :: Windows 10'
    ],
    #install_requires=['SobolSequence==0.2.1','google-api-python-client==2.63.0','oauth2client==4.1.3','pybind11==2.10.0','pandas==1.5.0','tk','numpy==1.22.0','matplotlib==3.6.0','mkl','scikit-learn==1.1.3','scipy==1.9.2','tensorflow==2.10.0','seaborn==0.12.0', 'scikit-image==0.19.3','tensorflow-datasets==4.6.0','torch==1.12.1','xgboost==1.6.2','jupyter==1.0.0','quantlib==1.27','xlrd==2.0.1','pydicom==2.3.0','yfinance==0.1.74','xarray==2022.9.0','kaggle==1.5.12','pandera','statsmodels'],
    long_description=long_description,
    long_description_content_type='text/markdown'
  #  extras_require={
  #  'win32': 'pywin32'
  #}
)
