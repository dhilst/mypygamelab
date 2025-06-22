import random
from typing import TypedDict

class Coord(TypedDict):
    x: int
    y: int

def random_int(min_val: int, max_val: int) -> int:
    """
    Return a random integer between min_val and max_val (inclusive).
    
    Args:
        min_val: The minimum value (inclusive)
        max_val: The maximum value (inclusive)
    
    Returns:
        A random integer in the range [min_val, max_val]
    
    Raises:
        ValueError: If min_val is greater than max_val
    """
    if min_val > max_val:
        raise ValueError("min_val must be less than or equal to max_val")
    return random.randint(min_val, max_val)


def random_coord(max_x: int, max_y: int) -> Coord:
    return {"x": random_int(0, max_x-1), "y": random_int(0, max_y-1)}
