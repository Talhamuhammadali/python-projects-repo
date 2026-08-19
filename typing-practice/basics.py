from typing import Generic, TypeVar


T = TypeVar('T', bound=int)

def test_function(value: T) -> T:
    return value


test_value = 42
result = test_function(test_value)

print(f"Input: {test_value}, Output: {result}")
