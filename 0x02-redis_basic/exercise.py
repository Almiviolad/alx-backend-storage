#!/usr/bin/env python3

"""Create a Cache class.
In the __init__ method, store an instance of the Redis client as a private
variable named _redis (using redis.Redis()) and flush the instance using
flushdb.

Create a store method that takes a data argument and returns a string.
The methodshould generate a random key (e.g. using uuid),
store the input data in Redis usingthe random key and return the key.
"""

import uuid
from typing import Union, Callable, Optional
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that takes a Callable argument and returns a Callable."""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """Function that counts the time the method is called and returns
        value returned by the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a
particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """Wrapper function that returns method."""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, str(method(self, *args, **kwargs)))
        return str(method(self, *args, **kwargs))
    return wrapper


def replay(method: Callable):
    """Replay and display the history of inputs and outputs for a particular
    function.
    """
    red = redis.Redis()
    fn_name = method.__qualname__
    count = int(red.get(fn_name).decode('utf-8'))
    input_list = red.lrange("{}:inputs".format(fn_name), 0, -1)
    output_list = red.lrange("{}:outputs".format(fn_name), 0, -1)

    io_combined = zip(input_list, output_list)
    print("{} was called {} times:".format(fn_name, count))

    for i, o in io_combined:
        i = i.decode('utf-8')
        o = o.decode('utf-8')
        print("{}(*{}) -> {}".format(fn_name, i, o))


class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self,
              data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis DB"""
        self.id = uuid.uuid4()
        self.key = str(self.id)
        self._redis.set(self.key, data)
        self._redis.close()
        return self.key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Gets value from Redis with key, fn.change to format"""
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: bytes) -> str:
        """Converts bytes to a string."""
        return self.get(key, fn=lambda v: v.decode('utf-8'))

    def get_int(self, key: bytes) -> int:
        """Converts bytes to an integer."""
        return self.get(key, fn=int)
