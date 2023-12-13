# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:42:34 2023

@author: marti
"""

from setuptools import setup

setup(
    name="uf-calculator",  # Change this to your desired library name
    version="0.1.0",  # Update this to your desired version number
    description="Calculate the UF value for any day in Chile",
    author="Your Name",  # Update this to your name
    author_email="your@email.com",  # Update this to your email address
    url="https://github.com/your-username/uf-calculator",  # Update this to your GitHub repository URL
    packages=["uf_calculator"],  # Update this to the name of your main package directory
    install_requires=[
        "datetime",
        "calendar",
    ],
    python_requires=">=3.6",  # Update this if your library requires a specific Python version
)
