"""Experimenting with some decorators"""
import time
import warnings

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

def timer_wraps(func: Callable):
    """Time the function that has the decorator with functools.wraps."""
    @wraps(func)
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
        
def depricated(reason: Optional[str]):
    """Mark a function, class or variables as depricated."""
    def decorator(obj):
        if isinstance(obj, type) or callable(obj):
            @wraps(obj)
            def wrapper(*args, **kwargs):
                warnings.warn(f"{obj.__name__} is deprecated. {reason}", category=DeprecationWarning, stacklevel=1)
                return obj(*args, **kwargs)
            return wrapper
        else:
            warnings.warn(f"This object has deprecated. {reason}", category=DeprecationWarning, stacklevel=1)
            
            return obj
    return decorator


# Testing decorators
@timer
def test_function():
    time.sleep(1)
    return "Done"

@repeat(times=2)
def hi(name: str):
    print(f"Hi {name}")

@depricated(reason="No reason just testing, deprication")
def hello():
    """Testing deprication"""
    print("Hello")

if __name__ == "__main__":
    test_function()
    hi(name="Talha")
    hello()