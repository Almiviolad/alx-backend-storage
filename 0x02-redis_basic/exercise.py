#!/usr/bin/env python3
"""Create a Cache class.
In the __init__ method, store an instance of the Redis
 client as a private variable
named _redis (using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid),
store the input data in Redis using the random key and return the key."""
import uuid
from typing import Union, Callable, Optional
import redis


class Cache:
    """ Cache class"""

    def __init__(self):
        """ constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in redus db"""
        self.id = uuid.uuid4()
        self.key = str(self.id)
        self._redis.set(self.key, data)
        self._redis.close()
        return self.key
    
    def get_str(self,byte_result: bytes) -> str:
        """converts byte to str"""
        return byte_result.decode('utf-8')

    def get_int(self, byte_result: bytes) -> int:
        """ converts byte to int"""
        return int(byte_result.decode('utf-8'))

    def get(self, key: str, fn: Optional[Callable]) -> bytes:
        """getts vlue using key frim refis db"""
        value = self._redis.get(key)
        print(fn)
        if (value):
            print(value)
            if (str(fn) == "<class 'str'>"):
                return self.get_str(value)
            elif (str(fn) == "<class 'int'>"):
                return self.get_int(value)
        return value
