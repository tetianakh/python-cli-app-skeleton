#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


install_requires = []

tests_require = [
    'pytest',
    'pytest-coverage',
    'pytest-mock',
]


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='myapp',
    version='0.1.dev0',
    author='Tetiana Khotiaintseva',
    packages=find_packages(),
    install_requires=install_requires,
    test_suite="myapp.tests",
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': [
            'myapp = myapp.main:main'
        ]
    },)
