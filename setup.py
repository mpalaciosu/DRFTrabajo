# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:42:34 2023

@author: marti
"""

from setuptools import setup

setup(
    name="uf_calculator",
    version="0.1.0",  
    description="Calculate the UF value for any day in Chile",
    author="Martin Palacios", 
    author_email="martinpalaciosu@gmail.com",  
    url="https://github.com/mpalaciosu/DRFTrabajo.git",  
    packages=["uf_calculator"],  
    install_requires=[
        "datetime",
        "calendar",
    ],
    python_requires=">=3.6",  
)
