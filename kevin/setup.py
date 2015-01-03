#!/usr/bin/env python

from setuptools import setup, find_packages
setup(name='kevin',
      version='0.1.0',
      author='Kevin Walchko',
      author_email='kevin.walchko@outlook.com',
      license='MIT',
      description='useful functions and classes',
      url='https://github.com/walchko',
      long_description=open('README.rst').read(),
      install_requires=[
      	"json",
      	"yaml"],
      packages=find_packages())