from setuptools import setup, find_packages

from geoutils import __version__

setup(
    name='geoutils',
    version=__version__,
    license='GPLv3+',
    author='Joel Dubowy',
    author_email='jdubowy@gmail.com',
    packages=find_packages(),
    scripts=[
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.5",
        "Operating System :: POSIX",
        "Operating System :: MacOS"
    ],
    url='https://github.com/pnwairfire/geoutils',
    description='Utilities for interacting with chat services',
    install_requires=[
        "numpy"
    ],
    dependency_links=[
        "https://pypi.airfire.org/simple/geoutils/",
    ]
)
