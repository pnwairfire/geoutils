"""Unit tests for firspider.geojson"""

__author__ = "Joel Dubowy"

import copy
import datetime

from geoutils import geojson


class TestGetCentroid(object):

    def test_point(test):
        g = {
            "type": "Point",
            "coordinates": [-102.0, 39.5]
        }
        expected = [-102.0, 39.5]
        assert expected == geojson.get_centroid(g)

    def test_multi_point(test):
        g = {
            "type": "MultiPoint",
            "coordinates": [
                [-100.0, 34.0],
                [-101.0, 35.4]
            ]
        }
        expected = [-100.5, 34.7]
        assert expected == geojson.get_centroid(g)

    def test_line_string(test):
        g = {
            "type": "LineString",
            "coordinates": [
                [-100.0, 34.0],
                [-101.0, 35.4]
            ]
        }
        expected = [-100.5, 34.7]
        assert expected == geojson.get_centroid(g)

    def test_polygon(test):
        g = {
           "type": "Polygon",
           "coordinates": [
                [
                    [-100.0, 34.0], [-101.0, 35.4], [-101.5, 34.4]
                ]
           ]
        }
        expected = [-100.83333333333333, 34.6]
        assert expected == geojson.get_centroid(g)

    def test_multi_line_string(test):
        g = {
            "type": "MultiLineString",
            "coordinates": [
                [
                    [-100.0, 34.0], [-101.0, 35.4]
                ],
                [
                    [-101.5, 34.4]
                ]
            ]
        }
        expected = [-100.83333333333333, 34.6]
        assert expected == geojson.get_centroid(g)

    def test_multi_polygon(test):
        g = {
           "type": "MultiPolygon",
           "coordinates": [
                [
                    [
                        [-100.0, 34.0], [-101.0, 35.4], [-101.5, 34.4]
                    ]
                ],
                [
                    [
                        [-104.1, 34.12], [-102.4, 33.23]
                    ]
                ]
            ]
        }
        expected = [-101.8, 34.230000000000004]
        assert expected == geojson.get_centroid(g)
