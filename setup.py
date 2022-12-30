from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="lcexoplanet",
    version="0.1.1",
    author="Diego Hidalgo Soto",
    author_email="diego.hidalgo@hotmail.es",
    description="Light Curves for Exoplanets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DiegoHS79/lcexoplanet",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
