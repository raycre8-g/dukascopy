#!/usr/bin/env python3

from setuptools import setup, find_packages

NAME = "dukascopy"
VERSION = '0.3.0'

setup(
    name=NAME,
    packages=find_packages(),
    install_requires=['requests>=2.9.1'],
    version=VERSION,
    description='Dukascopy Bank SA historical data downloader',
    author='Andrea Monni',
    author_email='cranties76@gmail.com',
    url='https://github.com/cranties/dukascopy',
    download_url='https://github.com/cranties/dukascopy/tarball/' + VERSION,
    keywords=['dukascopy', 'forex', 'finance', 'historical data', 'price', 'currency'],
    entry_points={
        'console_scripts': [
            'dukascopy = dukascopy.main:main',
        ],
    },

    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

