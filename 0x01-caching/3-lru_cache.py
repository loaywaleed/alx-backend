#!/usr/bin/env python3
"""
Basic caching module in python
"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Class representing basic caching in python"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Method that adds data to cache"""
        if key and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.cache_data.pop(self.order[0])
                self.order.pop(0)
                print("DISCARD: {}".format(discarded))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Method that gets data from cache"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)