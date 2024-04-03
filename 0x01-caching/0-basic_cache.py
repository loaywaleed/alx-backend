#!/usr/bin/env python3
"""
Basic caching module in python
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Class representing basic caching in python"""

    def put(self, key, item):
        """Method that adds data to cache"""
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Method that gets data from cache"""
        return self.cache_data.get(key)
