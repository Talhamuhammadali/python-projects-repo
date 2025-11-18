"""Experimenting with some decorators"""
import time

from typing import Callable


# Lets create a timer decorator
def timer(func: Callable):
    """Time the function that has the decorator."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print(f"{func.__name__} processing time: {stop - start:.2f}s")
        return result
    return wrapper


# Testing decorator
@timer
def test_function():
    time.sleep(1)
    return "Done"


if __name__ == "__main__":
    test_function()