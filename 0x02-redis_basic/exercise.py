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
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator that take Callable argument and returns a Callable."""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """function that counts the time method is called
and returns the value returned by the original method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Cache class"""

    def __init__(self):
        """ constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in redus db"""
        self.id = uuid.uuid4()
        self.key = str(self.id)
        self._redis.set(self.key, data)
        self._redis.close()
        return self.key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """gets value from redis db using key, fn changes it to fotmat"""
        value = self._redis.get(key)
        if (fn):
            return fn(value)
        return value

    def get_str(self, key: bytes) -> str:
        """converts byte to str"""
        return self.get(key, fn=lambda v: v.decode('utf-8'))

    def get_int(self, key: bytes) -> int:
        """ converts byte to int"""
        return self.get(key, fn=int)
