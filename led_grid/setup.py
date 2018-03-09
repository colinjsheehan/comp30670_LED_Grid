#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
#2
    author="Colin John Sheehan",
#3
    author_email='colin.sheehan@ucdconnect.ie',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
#4
    description="This program inputs the sie of a grid and a series of instructions to switch on/off 'LEDs' at various coordinates. It outputs the number of lite LEDs. ",
    install_requires=requirements,
#5
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='led_grid',
#1
    name='led_grid',
#6
    packages=find_packages(include=['led_grid']),
#7 ...
    entry_points={'console_scripts': [ 'led_grid=led_grid.main:main'],},
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
#8
    url='https://github.com/colinjsheehan/led_grid',
#9
    version='1',
    zip_safe=False,
)
