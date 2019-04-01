VERSION = (0, 1, 5)
NAME = "vt2geojson"
DESCRIPTION = "Dump vector tiles to GeoJSON from remote URLs or local system files."
AUTHOR = "Theophile Dancoisne"
AUTHOR_EMAIL = "dancoisne.theophile@gmail.com"
URL = "https://github.com/Amyantis/python-vt2geojson"


def get_version():
    return '.'.join(map(str, VERSION))


__version__ = get_version()
