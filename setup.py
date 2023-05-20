import sys
from setuptools import setup, find_packages
from packaging import version

python_requires = '>=3.11'
required_version = version.parse(python_requires.replace('>=', ''))

if sys.version_info < (required_version.major, required_version.minor):
    sys.exit(f'Python {required_version} or higher is required.')

setup(
    name="hello-python-audio",
    version="0.1.0",
    packages=find_packages(),
    python_requires=python_requires,
)
