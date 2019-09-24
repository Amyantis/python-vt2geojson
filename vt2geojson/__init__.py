from pkg_resources import get_distribution, DistributionNotFound

NAME = "vt2geojson"
DESCRIPTION = "Dump vector tiles to GeoJSON from remote URLs or local system files."
AUTHOR = "Theophile Dancoisne"
AUTHOR_EMAIL = "dancoisne.theophile@gmail.com"
URL = "https://github.com/Amyantis/python-vt2geojson"

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
