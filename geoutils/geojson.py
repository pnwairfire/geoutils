__author__ = "Joel Dubowy"

import numpy

def get_centroid(geometry):
    # TODO: There must be a lib that takes GeoJSON as input and

    if geometry["type"] == "Point":
        coords = [geometry["coordinates"]]

    elif geometry["type"] in ("MultiPoint", "LineString"):
        coords = geometry["coordinates"]

    elif geometry["type"] == "Polygon":
        # Note: this only considers the outer boundary in the case
        # where the polygon has hole(s)
        coords = geometry["coordinates"][0]

    elif geometry["type"] == "MultiLineString":
        coords = [c for p in geometry["coordinates"] for c in p]

    elif geometry["type"] == "MultiPolygon":
        # Note: as with 'Polygon', this only considers the outer
        # boundaries if any of the polygons have hole(s)
        coords = [e for p in geometry["coordinates"]
            for c in p[0:1] for e in c]
    else:
        raise ValueError("Unsupported GeoJSON geometry type: %s",
            geometry["type"])

    coords = numpy.array(coords)

    return numpy.mean(coords[:,:], axis=0).tolist()
