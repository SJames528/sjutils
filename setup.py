from setuptools import setup

setup(
    name='sjutils',
    version='1.0',
    package_dir = {"sjutils":"/home/sjames528/Projects/sjutils/sjutils"},
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
