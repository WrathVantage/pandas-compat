#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import versioneer


NAME = 'pandas-compat'


# versioning
cmdclass = versioneer.get_cmdclass()


def readme():
    with open('README.rst') as f:
        return f.read()


INSTALL_REQUIRES = (
    ['pandas'],
)


setup(
    name=NAME,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Pandas API compatiblity layer",
    long_description=readme(),
    license='BSD License',
    author='The PyData Development Team',
    author_email='pydata@googlegroups.com',
    url='https://github.com/pandas-dev/pandas-compat',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
    ],
    keywords='data',
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    test_suite='tests',
)
