# python-vt2geojson [![Build Status](https://travis-ci.org/Amyantis/python-vt2geojson.svg?branch=master)](https://travis-ci.org/Amyantis/python-vt2geojson)
Dump vector tiles to GeoJSON from remote URLs or local system files.

Inspired from https://github.com/mapbox/vt2geojson.

## Installation
```
pip install python-vt2geojson
```

## Usage
Using the CLI:
```
vt2geojson --help
```

Making a GeoDataframe from a PBF vector tile file:
```python
import geopandas as gpd
import requests

from vt2geojson.tools import vt_bytes_to_geojson

MAPBOX_ACCESS_TOKEN = "*****"

x = 150
y = 194
z = 9

url = f"https://api.mapbox.com/v4/mapbox.mapbox-streets-v6/{z}/{x}/{z}.vector.pbf?access_token={MAPBOX_ACCESS_TOKEN}"
r = requests.get(url)
assert r.status_code == 200, r.content
vt_content = r.content

features = vt_bytes_to_geojson(vt_content, x, y, z)
gdf = gpd.GeoDataFrame.from_features(features)
```

## Notes
This library has only been tested against **Python 3.6**.

Feel free to [submit your issues](https://github.com/Amyantis/python-vt2geojson/issues).