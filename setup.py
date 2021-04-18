#!/usr/bin/env python3

# setup.py
from distutils.core import setup

setup(
    name='miflora-mqtt-daemon',
    version='0.0.1',
    scripts=['miflora-mqtt-daemon.py',],
    install_requires=[
    	"miflora==0.7.1",
		"bluepy==1.3.0",
		"btlewrap==0.0.10",
		"paho-mqtt==1.4.0",
		# "wheel==0.29.0",
		"sdnotify==0.3.1",
		"colorama==0.3.9",
		"Unidecode==0.4.21",
		"setuptools"
    ],
    include_package_data=True,
    package_data= [
    	"config.ini"
    ]
)
