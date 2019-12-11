from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='dependent_bootstrap',

    packages=find_packages(),

    python_requires='>=3.7.3', install_requires=['matplotlib', 'numpy', 'networkx']

)
