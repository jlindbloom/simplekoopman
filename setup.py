from setuptools import setup, find_packages

setup(
    name='simplekoopman',
    version='0.0.1',
    author='Jonathan Lindbloom, Casey Dowdle.',
    author_email='jonathan@lindbloom.com',
    license='LICENSE',
    packages=find_packages(),
    description='Some simple code for making a finite-rank approximation to a Koopman operator.',
    long_description=open('README.md').read(),
)