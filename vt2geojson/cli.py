import argparse
import json
from re import search
from urllib.request import urlopen

from vt2geojson import DESCRIPTION
from vt2geojson.tools import vt_bytes_to_geojson, _is_url

XYZ_REGEX = r"\/(\d+)\/(\d+)\/(\d+)"


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("uri", help="URI (url or filepath)")
    parser.add_argument("-l", "--layer", help="include only the specified layer", type=str)
    parser.add_argument("-x", help="tile x coordinate (normally inferred from the URL)", type=int)
    parser.add_argument("-y", help="tile y coordinate (normally inferred from the URL)", type=int)
    parser.add_argument("-z", help="tile z coordinate (normally inferred from the URL)", type=int)
    args = parser.parse_args()

    if _is_url(args.uri):
        matches = search(XYZ_REGEX, args.uri)
        if matches is None:
            raise ValueError("Unknown url, no `/z/x/y` pattern.")
        z, x, y = map(int, matches.groups())
        r = urlopen(args.uri)
        content = r.read()
    else:
        if args.x is None or args.y is None or args.z is None:
            raise ValueError("You provided a path to a file. Therefore you must specify x, y and z.")
        x = args.x
        y = args.y
        z = args.z
        with open(args.uri, "rb") as f:
            content = f.read()

    geojson_result = vt_bytes_to_geojson(content, x, y, z, args.layer)
    print(json.dumps(geojson_result))


if __name__ == "__main__":
    main()
