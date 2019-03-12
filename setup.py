from setuptools import setup

from vt2geojson import NAME, DESCRIPTION, AUTHOR, AUTHOR_EMAIL, URL, __version__

setup(
    name=NAME,
    version=__version__,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    entry_points={
        "console_scripts": ['vt2geojson=vt2geojson.cli:main']
    },
    install_requires=[
        "mapbox_vector_tile"
    ]
)
