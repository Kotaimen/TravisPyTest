# -*- encoding: utf-8 -*-

__author__ = 'kotaimen'
__date__ = '12/23/14'

import unittest
from TravisTest import Cache


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Cache()

    def test_put(self):
        self.client.put('A', 'a')
        self.assertEqual(self.client.get('A'), 'a')

if __name__ == '__main__':
    unittest.main()
