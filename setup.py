from setuptools import setup, find_packages

from vt2geojson import NAME, DESCRIPTION, AUTHOR, AUTHOR_EMAIL, URL, __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=__version__,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),
    entry_points={
        "console_scripts": ['vt2geojson=vt2geojson.cli:main']
    },
    install_requires=[
        "mapbox_vector_tile"
    ],
    test_suite="tests"
)
