#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module sets up the package for the transpyjs"""

from setuptools import find_packages, setup

#with open("README.md", "r", encoding="utf-8") as fh:
#    long_description = fh.read()

setup(    
    name="transpyjs",
    author="Guy-Yann VECTOL",
    author_email="guyyann.vectol@gmail.com",
    maintainer="Guy-Yann VECTOL",
    maintainer_email="guyyann.vectol@gmail.com",
    version="0.0.1",
    #url="https://github.com/jfuruness/lib_work_login.git",
    #download_url='https://github.com/jfuruness/lib_work_login.git',
    keywords=['pyjs', 'transcrypt', 'pytojs', 'py2js', 'transpy', 'transcript', 'Vectol', 'transpyjs', ],
    license="BSD",
    description="Write in Python, compile in Javascript",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    project_urls={
        "Transcrypt": "https://www.transcrypt.org/",
    },
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Transcrypt==3.9.3',
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'],
    entry_points={
        'console_scripts': [
            'create = transpyjs.__main__:main',
            'configure = transpyjs.__main__:configure',
        ]},
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)