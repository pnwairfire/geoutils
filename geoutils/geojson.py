__author__ = "Joel Dubowy"

import numpy

def _compute_mean(coords):
    coords = numpy.array(coords)
    return numpy.mean(coords[:,:], axis=0).tolist()

def _get_polygon_coords(coords):
    # Note: this only considers the outer boundary. Subsquent
    # arrays are holes
    coords = coords[0]
    # if first and last coordinate in the polygon are the same
    # (which should be the case for valid geojson) pop the last one
    if coords[0] == coords[-1]:
        coords = coords[:-1]

    return coords

def get_centroid(geometry):
    # TODO: There must be a lib that takes GeoJSON as input and

    if geometry["type"] == "Point":
        coords = [geometry["coordinates"]]

    elif geometry["type"] in ("MultiPoint", "LineString"):
        coords = geometry["coordinates"]

    elif geometry["type"] == "Polygon":
        coords = _get_polygon_coords(geometry["coordinates"])

    elif geometry["type"] == "MultiLineString":
        coords = [c for p in geometry["coordinates"] for c in p]

    elif geometry["type"] == "MultiPolygon":
        # returns the centroid of the individual polygon centroids
        # Note: as with 'Polygon', this only considers the outer
        # boundaries if any of the polygons have hole(s)
        coords = [_compute_mean(_get_polygon_coords(c))
           for c in geometry["coordinates"]]
        #coords = [b for c in geometry["coordinates"] for b in c]

    else:
        raise ValueError("Unsupported GeoJSON geometry type: %s",
            geometry["type"])

    return _compute_mean(coords)
