from urllib.parse import urlparse

from mapbox_vector_tile import decode

from vt2geojson.features import Layer


def _is_url(uri):
    return urlparse(uri).scheme != ""


def vt_bytes_to_geojson(b_content, x, y, z, layer=None):
    data = decode(b_content)
    features_collections = [Layer(x=x, y=y, z=z, name=name, obj=layer_obj).toGeoJSON()
                            for name, layer_obj in data.items() if layer is None or name == layer]
    return {
        "type": "FeatureCollection",
        "features": [fc["features"] for fc in features_collections]
    }
