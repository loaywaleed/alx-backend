#!/usr/bin/env python3
"""
Basic caching module in python
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """Class representing basic caching in python"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Method that adds data to cache"""
        if key and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded, _ = self.cache_data.popitem()
                print("DISCARD: {}".format(discarded))
            self.cache_data[key] = item

    def get(self, key):
        """Method that gets data from cache"""
        return self.cache_data.get(key)
