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

        # should get same results if polygon has same last and first coordinates
        g['coordinates'][0].append([-100.0, 34.0])
        assert expected == geojson.get_centroid(g)

    def test_polygon_with_hole(test):
        g = {
           "type": "Polygon",
           "coordinates": [
                [
                    [-100.0, 34.0], [-101.0, 35.4], [-101.5, 34.4]
                ],
                # the hole is ignored in centroid computation
                [
                    [-100.2, 35.2], [-100.3, 34.4], [-100.1, 34.3]
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
                    # centroid is [-100.83333333333333, 34.6]
                    [
                        [-100.0, 34.0], [-101.0, 35.4], [-101.5, 34.4]
                    ],
                    # the hole is ignored in centroid computation
                    [
                        [-100.2, 35.2], [-100.3, 34.4], [-100.1, 34.3]
                    ]
                ],
                [
                    # centroid is [-102.96666666666665, 34.19333333333333]
                    [
                        [-104.1, 34.12], [-102.4, 33.23], [-102.4, 35.23]
                    ]
                ]
            ]
        }
        expected = [-101.89999999999999, 34.39666666666666]
        assert expected == geojson.get_centroid(g)

        # should get same results if polygons have same last and first coordinates
        g['coordinates'][0][0].append([-100.0, 34.0])
        g['coordinates'][1][0].insert(0, [-102.4, 35.23])
        assert expected == geojson.get_centroid(g)