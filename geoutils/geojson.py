__author__ = "Joel Dubowy"

import numpy

def get_centroid(geometry):
    # TODO: There must be a lib that takes GeoJSON as input and

    if geometry["type"] == "Point":
        coords = [geometry["coordinates"]]

    elif geometry["type"] in ("MultiPoint", "LineString"):
        coords = geometry["coordinates"]

    elif geometry["type"] == "Polygon":
        coords = geometry["coordinates"][0]

    elif geometry["type"] == "MultiLineString":
        coords = [c for p in geometry["coordinates"] for c in p]

    elif geometry["type"] == "MultiPolygon":
        coords = [e for p in geometry["coordinates"]
            for c in p for e in c]
    else:
        raise ValueError("Unsupported GeoJSON geometry type: %s",
            geometry["type"])

    coords = numpy.array(coords)

    return numpy.mean(coords[:,:], axis=0).tolist()
