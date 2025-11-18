"""Experimenting with some decorators"""
import time

from functools import wraps
from typing import Callable, Optional


# Lets create decorators
def timer(func: Callable):
    """Time the function that has the decorator."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print(f"{func.__name__} processing time: {stop - start:.2f}s")
        return result
    return wrapper

def repeat(times):
    """Repeat a function"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator    
        
        
# Testing decorators
@timer
def test_function():
    time.sleep(1)
    return "Done"

@repeat(times=2)
def hi(name: str):
    print(f"Hi {name}")

if __name__ == "__main__":
    test_function()
    hi(name="Talha")