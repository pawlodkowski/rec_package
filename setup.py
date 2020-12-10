from setuptools import setup
import os


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="rec_package",  # name of your package
    version="0.0.1",
    description="a useful package",
    author="Spiced Academy",
    author_email="pw@spiced-academy.com",
    packages=["rec_package"],  # same as name
    url="https://github.com/pawlodkowski/rec_package",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
)