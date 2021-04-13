from enum import Enum
from math import pi, atan, exp


class GeometryType(Enum):
    UNKNOWN = 'Unknown'
    POINT = 'Point'
    LINESTRING = 'LineString'
    POLYGON = 'Polygon'
    MULTILINESTRING = 'MultiLineString'
    MULTIPOLYGON = 'MultiPolygon'
    MULTIPOINT = 'MultiPoint'


class Feature:
    def __init__(self, x, y, z, obj, extent=4096):
        self.x = x
        self.y = y
        self.z = z
        self.obj = obj
        self.extent = extent

    @property
    def tiles_coordinates(self):
        return self.obj['geometry']['coordinates']

    @property
    def geometry_type(self):
        return GeometryType(self.obj['geometry']['type'])

    @property
    def properties(self):
        return self.obj['properties']

    def toGeoJSON(self):
        size = self.extent * 2 ** self.z
        x0 = self.extent * self.x
        y0 = self.extent * self.y

        def project_one(p_x, p_y):
            y2 = 180 - (p_y + y0) * 360. / size
            long_res = (p_x + x0) * 360. / size - 180
            lat_res = 360. / pi * atan(exp(y2 * pi / 180)) - 90
            return [long_res, lat_res]

        def project(coords):
            if all(isinstance(x, int) or isinstance(x, float) for x in coords):
                assert len(coords) == 2
                return project_one(coords[0], coords[1])
            return [project(l) for l in coords]

        coords = project(self.tiles_coordinates)
        geometry_type = self.geometry_type.value

        result = {
            "type": "Feature",
            "geometry": {
                "type": geometry_type,
                "coordinates": coords
            },
            "properties": self.properties
        }
        return result


class Layer:
    def __init__(self, x, y, z, name, obj):
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        self.obj = obj

    @property
    def extent(self):
        return self.obj['extent']

    def toGeoJSON(self):
        return {
            "type": "FeatureCollection",
            "features": [Feature(x=self.x, y=self.y, z=self.z, obj=f, extent=self.extent).toGeoJSON()
                         for f in self.obj['features']]
        }
