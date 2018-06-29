from setuptools import setup, find_packages
import PyouPlay.pyouplay

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Pyoutube",
    version="0.1",
    author="Omkar Yadav",
    author_email="omkar10859@gmail.com",
    description="This is a simple python package when passed with a search argument returns link to video.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Mozilla Public License Version 2.0',
    keywords='youtube',
    url="https://github.com/omi10859/PyouPlay",
    packages=find_packages),
classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7  ',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Operating System :: OS Independent",
    ),
install_requires=[
    'beautifulsoup4'
    ],
include_package_data=True,
zip_safe=False
)
