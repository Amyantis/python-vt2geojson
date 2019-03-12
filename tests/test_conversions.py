import os
from unittest import TestCase

from vt2geojson.tools import vt_bytes_to_geojson

DIRPATH = os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILEPATH = os.path.join(DIRPATH, "sample_14_8185_5449.pbf")

with open(SAMPLE_FILEPATH, "rb") as f:
    sample_content = f.read()


class TestConversions(TestCase):
    def test_bytes_to_geojson(self):
        result = vt_bytes_to_geojson(sample_content, 8185, 5449, 14)
        assert result['features']
