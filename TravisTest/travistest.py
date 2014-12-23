# -*- encoding: utf-8 -*-

__author__ = 'kotaimen'
__date__ = '12/23/14'

import memcache


class Cache(object):
    def __init__(self, servers=None):
        if servers:
            self.client = memcache.Client(servers=servers)
        else:
            self.client = memcache.Client(servers=['localhost:11211'])

    def put(self, k, v):
        self.client.set(k, v)

    def get(self, k):
        return self.client.get(k)

