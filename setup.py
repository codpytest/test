# from __future__ import annotations
from setuptools import Extension
from setuptools import setup
__version__ = '0.0.1'





printf = Extension(
    'printf',
    sources=["src/printf.cpp"],
    # include_dirs=[pybind11.get_include()],
)

if __name__ == "__main__":
    setup(
        name = 'test',
        version=__version__,
        author="test",
        author_email="",
        url="",
        description="test",
        long_description="",
        ext_modules=[printf],
        python_requires=">=3.7"
    )