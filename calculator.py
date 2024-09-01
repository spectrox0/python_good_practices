from abc import ABC, abstractmethod
from math import pi
from typing import List, Union

from pydantic import BaseModel, Field, ValidationError, validator


class Shape(BaseModel, ABC):
    """
    Abstract base class for geometric shapes.

    This class defines the interface for geometric shapes, which includes
    methods to calculate area and volume. All shapes must inherit from this class
    and implement the area and volume methods.
    """
    
    @abstractmethod
    def area(self) -> float:
        """
        Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def volume(self) -> float:
        """
        Calculate the volume of the shape.

        Returns:
            float: The volume of the shape.
        """
        pass

class Circle(Shape):
    """
    Circle shape class inheriting from Shape.

    This class provides methods to calculate the area of a circle and the volume
    of a sphere.
    """
    radius: float = Field(..., gt=0, description="Radius of the circle")

    @validator('radius')
    def check_positive(cls, value):
        """
        Validator to ensure the radius is positive.

        Args:
            value (float): The radius of the circle.

        Returns:
            float: The validated radius.

        Raises:
            ValueError: If the radius is not positive.
        """
        if value <= 0:
            raise ValueError("Radius must be greater than zero.")
        return value

    def area(self) -> float:
        """
        Calculates the area of a circle.

        Returns:
            float: The area of the circle.
        """
        return pi * self.radius ** 2

    def volume(self) -> float:
        """
        Calculates the volume of a sphere.

        Returns:
            float: The volume of the sphere.
        """
        return (4/3) * pi * self.radius ** 3

class Square(Shape):
    """
    Square shape class inheriting from Shape.

    This class provides methods to calculate the area of a square and the volume
    of a cube.
    """
    side: float = Field(..., gt=0, description="Side of the square")

    @validator('side')
    def check_positive(cls, value):
        """
        Validator to ensure the side length is positive.

        Args:
            value (float): The side length of the square.

        Returns:
            float: The validated side length.

        Raises:
            ValueError: If the side length is not positive.
        """
        if value <= 0:
            raise ValueError("Side must be greater than zero.")
        return value

    def area(self) -> float:
        """
        Calculates the area of a square.

        Returns:
            float: The area of the square.
        """
        return self.side ** 2

    def volume(self) -> float:
        """
        Calculates the volume of a cube.

        Returns:
            float: The volume of the cube.
        """
        return self.side ** 3

class Triangle(Shape):
    """
    Triangle shape class inheriting from Shape.

    This class provides methods to calculate the area of a triangle and the volume
    of a triangular prism.
    """
    base: float = Field(..., gt=0, description="Base of the triangle")
    height: float = Field(..., gt=0, description="Height of the triangle")

    @validator('base', 'height')
    def check_positive(cls, value):
        """
        Validator to ensure base and height are positive.

        Args:
            value (float): The base or height of the triangle.

        Returns:
            float: The validated base or height.

        Raises:
            ValueError: If the base or height is not positive.
        """
        if value <= 0:
            raise ValueError("Base and height must be greater than zero.")
        return value

    def area(self) -> float:
        """
        Calculates the area of a triangle.

        Returns:
            float: The area of the triangle.
        """
        return (self.base * self.height) / 2

    def volume(self) -> float:
        """
        Calculates the volume of a triangular prism.

        Returns:
            float: The volume of the triangular prism.

        Notes:
            This implementation assumes that the prism has a square base.
        """
        return (self.base * self.height) / 2 * self.base

class Cube(Shape):
    """
    Cube shape class inheriting from Shape.

    This class provides methods to calculate the surface area and the volume
    of a cube.
    """
    side: float = Field(..., gt=0, description="Side length of the cube")

    @validator('side')
    def check_positive(cls, value):
        """
        Validator to ensure the side length is positive.

        Args:
            value (float): The side length of the cube.

        Returns:
            float: The validated side length.

        Raises:
            ValueError: If the side length is not positive.
        """
        if value <= 0:
            raise ValueError("Side length must be greater than zero.")
        return value

    def area(self) -> float:
        """
        Calculates the surface area of a cube.

        Returns:
            float: The surface area of the cube.
        """
        return 6 * (self.side ** 2)

    def volume(self) -> float:
        """
        Calculates the volume of a cube.

        Returns:
            float: The volume of the cube.
        """
        return self.side ** 3

# Functions to handle errors and optimize calculations
def calculate_area(shape: Shape) -> float:
    """
    Calculate the area of a given shape.

    Args:
        shape (Shape): An instance of a class inheriting from Shape.

    Returns:
        float: The area of the shape.
    """
    try:
        return shape.area()
    except ValidationError as e:
        print(e.json())
        return 0.0

def calculate_volume(shape: Shape) -> float:
    """
    Calculate the volume of a given shape.

    Args:
        shape (Shape): An instance of a class inheriting from Shape.

    Returns:
        float: The volume of the shape.
    """
    try:
        return shape.volume()
    except ValidationError as e:
        print(e.json())
        return 0.0


def total_area_optimized(shapes: List[Shape]) -> float:
    """
    Calculate the total area of a list of shapes using a list comprehension.

    This method is optimized by avoiding explicit loops.

    Args:
        shapes (List[Shape]): A list of shape instances.

    Returns:
        float: The total area of all shapes in the list.
    """
    return sum(shape.area() for shape in shapes)