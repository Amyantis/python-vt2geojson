import geopandas as gpd
import requests

from vt2geojson.tools import vt_bytes_to_geojson

MAPBOX_ACCESS_TOKEN = "pk.eyJ1IjoiZXhhbXBsZXMiLCJhIjoiY2p0MG01MXRqMW45cjQzb2R6b2ptc3J4MSJ9.zA2W0IkI0c6KaAhJfk9bWg"

x = 150
y = 194
z = 9

url = f"https://api.mapbox.com/v4/mapbox.mapbox-streets-v6/{z}/{x}/{y}.vector.pbf?access_token={MAPBOX_ACCESS_TOKEN}"
r = requests.get(url)
assert r.status_code == 200, r.content
vt_content = r.content

features = vt_bytes_to_geojson(vt_content, x, y, z)
gdf = gpd.GeoDataFrame.from_features(features)
print(gdf.head())
