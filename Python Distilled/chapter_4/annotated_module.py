"""This is a test module to demonstrate the use of annotations in Python."""
from dataclasses import dataclass
    
@dataclass
class Point:
    """A simple class to represent a point in 2D space."""
    x: float
    y: float
    
    def move(self, dx: float, dy: float) -> None:
        """Moves the point by the given offsets."""
        self.x += dx
        self.y += dy

Center: Point = Point(0, 0)    

def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

# untyped function
def multiply_numbers(a, b):
    """Multiplies two numbers together."""
    return a * b