from setuptools import setup
import os

dir = os.path.dirname(os.path.realpath(__file__))

setup(
    name='sjutils',
    version='1.0',
    package_dir = {"sjutils":dir+"/sjutils"},
    install_requires=[
        'numpy',
    ],
    description='Personal common utility functions and classes',
    url='http://github.com/SJames528/sjutils',
    author='S Harding',
    author_email='HardingSJ@cardiff.ac.uk',
    license='MIT',
    zip_safe=False
)
