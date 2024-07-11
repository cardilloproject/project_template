from setuptools import setup, find_packages

name = "cardillo_add_ons"
version = "0.0.1"
author = ""
author_email = ""
description = ""
long_description = ""

setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    install_requires=[
        "cardillo @ git+https://github.com/cardilloproject/cardillo.git#egg=cardillo",
    ],
    packages=find_packages(),
    python_requires=">=3.10",
)
