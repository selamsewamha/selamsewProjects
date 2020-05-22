"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import os
import glob

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='radnogip',
    version='1.0.19',
    description='A simple Python project to get my IP',
    long_description=long_description,
    url='https://github.com/selamsewamha/selamsewProjects',
    author='Selamsew Hilawi',
    author_email='amha.selam@amazon.com',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires = ['requests', 'pyyaml'],
    tests_require=['pytest', 'mock'],
    setup_requires=['pytest-runner'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage', 'mock'],
    },

    include_package_data = True,
    package_data = {
        'configurations': ['configurations/getmyip.yaml'],
    },
    data_files=[('configurations', glob.glob('configurations/*'))],
    scripts=['bin/getip.py'],
)
