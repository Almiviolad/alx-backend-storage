#!/usr/bin/env python3
"""Create a Cache class.
In the __init__ method, store an instance of the Redis
 client as a private variable
named _redis (using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid),
store the input data in Redis using the random key and return the key."""
import uuid
from typing import Union
import redis


class Cache:
    """ Cache class"""

    def __init__(self):
        """ constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in redus db"""
        id = uuid.uuid4()
        key = str(id)
        self._redis.set(key, data)
        self._redis.close()
        return key
