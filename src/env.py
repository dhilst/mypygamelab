from typing import Any, List, Optional

from src.typedefs import Positionable

class GridEnvironment:
    def __init__(self, width: int = 16, height: int = 16):
        self.width = width
        self.height = height
        # Initialize grid with empty lists to store objects
        self.grid = [[[] for _ in range(width)] for _ in range(height)]

    def is_valid_position(self, x: int, y: int) -> bool:
        """Check if the position is within grid boundaries."""
        return 0 <= x < self.width and 0 <= y < self.height

    def get_objects_at(self, x: int, y: int) -> List[Any]:
        """
        Get a list of objects at the specified grid position.
        
        Args:
            x (int): X-coordinate of the grid position
            y (int): Y-coordinate of the grid position
        
        Returns:
            List[Any]: List of objects at the position, empty list if invalid
        """
        if self.is_valid_position(x, y):
            return self.grid[y][x]
        return []


    def push_obj(self, obj: Positionable) -> bool:
        return self.push(obj.x, obj.y, obj)

    def push(self, x: int, y: int, obj: Any) -> bool:
        """
        Push an object to the list at the specified grid position.
        
        Args:
            x (int): X-coordinate of the grid position
            y (int): Y-coordinate of the grid position
            obj (Any): Object to push
        
        Returns:
            bool: True if the push was successful, False if position is invalid
        """
        if self.is_valid_position(x, y):
            self.grid[y][x].append(obj)
            return True
        return False

    def pop(self, x: int, y: int) -> Optional[Any]:
        """
        Pop and return the last object from the list at the specified grid position.
        
        Args:
            x (int): X-coordinate of the grid position
            y (int): Y-coordinate of the grid position
        
        Returns:
            Optional[Any]: The popped object, or None if position is invalid or list is empty
        """
        if self.is_valid_position(x, y) and self.grid[y][x]:
            return self.grid[y][x].pop()
        return None

    def peek(self, x: int, y: int) -> Optional[Any]:
        """
        Return the last object at the specified grid position without removing it.
        
        Args:
            x (int): X-coordinate of the grid position
            y (int): Y-coordinate of the grid position
        
        Returns:
            Optional[Any]: The last object, or None if position is invalid or list is empty
        """
        if self.is_valid_position(x, y) and self.grid[y][x]:
            return self.grid[y][x][-1]
        return None

