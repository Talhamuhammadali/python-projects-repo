from typing import TypeVar
from collections.abc import Iterable


def greet_all(names: list[str]) -> None:
    greetings = [f"Hello, {name}!" for name in names]
    print("\n".join(greetings))

valid_type_list = ["Alice", "Bob", "Charlie"]
invalid_type_list = ["Alice", 42, "Charlie"]
valid_type_set = {"Alice", "Bob", "Charlie"}

greet_all(valid_type_list)  # This will work fine
greet_all(invalid_type_list)
greet_all(valid_type_set)  # This will raise a type error since it's not a list

def greet_all_iterable(names: Iterable[str]) -> None:
    greetings = [f"Hello, {name}!" for name in names]
    print("\n".join(greetings))

greet_all_iterable(valid_type_list)  # This will work fine
greet_all_iterable(invalid_type_list)  # This will raise a type error since it's not a list of strings
greet_all_iterable(valid_type_set)  # This will work fine now

T = TypeVar('T', bound=int)

def test_function(value: T) -> T:
    return value


test_value = "42"
result = test_function(test_value)

print(f"Input: {test_value}, Output: {result}")
