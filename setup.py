import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "totp",
    version = "0.0.1",
    author = "Aniket Hande",
    author_email = "aniket.hande@protonmail.com",
    description = ("Time based OTP for auth gateways."),
    license = "MIT",
    url = "https://github.com/aniketor/totp",
    packages=['totp', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
