"""Demonstrating why @wraps matters when importing decorators."""
import sys
sys.path.insert(0, '.')

from decorators import timer, timer_wraps, repeat

# --- timer (NO @wraps) ---
@timer
def my_task():
    """I am the original task."""
    return 42

print("=== timer (without @wraps) ===")
print(f"  __name__: {my_task.__name__}")    # expect: "wrapper"
print(f"  __doc__:  {my_task.__doc__}")      # expect: None
print()

# --- timer_wraps (HAS @wraps) ---
@timer_wraps
def my_task_wraps():
    """I am the original task with wraps."""
    return 42

print("=== timer_wraps (with @wraps) ===")
print(f"  __name__: {my_task_wraps.__name__}")    # expect: "my_task_wraps"
print(f"  __doc__:  {my_task_wraps.__doc__}")      # expect: "I am the original task with wraps."
print()

# --- repeat (HAS @wraps) ---
@repeat(times=2)
def greet(name):
    """I greet people."""
    print(f"Hello {name}")

print("=== repeat (with @wraps) ===")
print(f"  __name__: {greet.__name__}")       # expect: "greet"
print(f"  __doc__:  {greet.__doc__}")         # expect: "I greet people."
print()
