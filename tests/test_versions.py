# -*- encoding: utf-8 -*-

__author__ = 'kotaimen'
__date__ = '12/24/14'

import unittest

from distutils.version import StrictVersion, LooseVersion

import shapely.geos


class TestVersions(unittest.TestCase):
    def test_numpy(self):
        import numpy

        self.assertGreaterEqual(StrictVersion(numpy.version.version),
                                StrictVersion('1.9.0'))

    def test_scipy(self):
        import scipy

        self.assertGreaterEqual(StrictVersion(scipy.version.version),
                                StrictVersion('0.9.0'))

    def test_gdal(self):
        import gdal

        self.assertGreaterEqual(int(gdal.VersionInfo()), 1100000)

    def test_shapely(self):
        self.assertGreaterEqual(
            StrictVersion('.'.join(map(str, shapely.geos.geos_version))),
            StrictVersion('3.3.8'))

    def test_mapnik(self):
        import mapnik

        self.assertGreaterEqual(LooseVersion(mapnik.mapnik_version_string()),
                                LooseVersion('2.2.0'))

    def test_psycopg2(self):
        import psycopg2

        self.assertGreaterEqual(StrictVersion(psycopg2.__version__.split(' ')[0]),
                                StrictVersion('2.5.0'))


if __name__ == '__main__':
    unittest.main()
