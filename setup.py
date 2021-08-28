from setuptools import setup, find_packages


with open("requirements.txt", "r") as f:
    required = f.read().splitlines()

with open("README.md", "r") as f:
    readme = f.read()


setup(
    name="sed-cloud/ritoman-betting-service",
    version="0.0.1",
    description="A registry service for webhook providers and consumers",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Stephen Davis",
    author_email="stephenedavis17@gmail.com",
    packages=find_packages(),
    url="https://github.com/sed-cloud/ritoman-betting-service",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=required,
)