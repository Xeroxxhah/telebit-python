from setuptools import setup, find_packages
import codecs
import os


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = 'v0.1.0'
DESCRIPTION = 'A wrapper around telebit (ngrok like service).'
LONG_DESCRIPTION = 'A wrapper around telebit (ngrok like service).'

# Setting up
setup(
    name="telebit-python",
    version=VERSION,
    author="Xeroxxhah (Muhammad Nauman Azeem)",
    author_email="xeroxxhah@pm.me",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python', 'python3', 'telebit', 'tunnel'],
)