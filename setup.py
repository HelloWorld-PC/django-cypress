from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    README = f.read()


setup(
    name="django-cypress",
    version="1.0.0",
    description="Integration of Cypress in a Django project.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="HelloWorld PC",
    url="https://github.com/HelloWorld-PC/django-cypress",
    license="MIT License",
    include_package_data=True,
    packages=find_packages(),
    package_data={
        "stubs": ["*"],
    },
    requires=[
        "Django (>=3.2)",
    ],
    install_requires=[
        "Django>=3.2",
    ],
)
