from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Keyson Raphael Acioli da Conceição",
    author_email="keyson.rapha@gmail.com",
    description="image processing package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)