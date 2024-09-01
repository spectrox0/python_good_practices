# Unit Tests
import unittest

from pydantic import ValidationError

from calculator import Circle, Cube, Square, Triangle, total_area_optimized


class TestGeometryCalculations(unittest.TestCase):
    """
    A test case class for testing the geometry calculations.

    Methods:
    - test_circle_area: Test the calculation of the area of a circle.
    - test_square_area: Test the calculation of the area of a square.
    - test_triangle_area: Test the calculation of the area of a triangle.
    - test_circle_volume: Test the calculation of the volume of a circle.
    - test_square_volume: Test the calculation of the volume of a square.
    - test_invalid_circle: Test the validation of a circle with invalid radius.
    - test_invalid_square: Test the validation of a square with invalid side length.
    - test_invalid_triangle: Test the validation of a triangle with invalid base and height.
    """

    def test_circle_area(self):
        """
        Test the calculation of the area of a circle.

        This test creates a Circle object with a radius of 5 and calculates its area.
        The expected result is approximately 78.5398, with a precision of 4 decimal places.
        The test checks if the calculated area matches the expected result using the `assertAlmostEqual` method.

        """
        circle = Circle(radius=5)
        area = circle.area()
        self.assertAlmostEqual(area, 78.5398, places=4)

    def test_square_area(self):
        """
        Test case for calculating the area of a square.

        This test case creates a square object with a side length of 4.
        It then calculates the area of the square using the `area()` method.
        The expected result is 16, so the test asserts that the calculated area is equal to 16.
        """
        square = Square(side=4)
        area = square.area()
        self.assertEqual(area, 16)

    def test_triangle_area(self):
        """
        Test case for calculating the area of a triangle.

        This test case creates a triangle object with a base of 3 and a height of 4.
        It then calls the `area()` method of the triangle object and compares the result
        with the expected area of 6. The test passes if the calculated area matches the expected area.

        """
        triangle = Triangle(base=3, height=4)
        area = triangle.area()
        self.assertEqual(area, 6)
    
    def test_cube_area(self):
        """Test the surface area calculation of a cube."""
        cube = Cube(side=3)
        self.assertEqual(cube.area(), 54)

    def test_circle_volume(self):
        """
        Test the volume calculation of a circle.

        This test creates a circle object with a radius of 5 and calculates its volume.
        The calculated volume is then compared to the expected value with a tolerance of 4 decimal places.

        """
        circle = Circle(radius=5)
        volume = circle.volume()
        self.assertAlmostEqual(volume, 523.5988, places=4)

    def test_square_volume(self):
        """
        Test case for the `volume` method of the `Square` class.

        This test case verifies that the `volume` method of the `Square` class correctly calculates the volume of a square.

        Steps:
        1. Create a `Square` object with a side length of 3.
        2. Call the `volume` method on the `Square` object.
        3. Assert that the calculated volume is equal to 27.

        """
        square = Square(side=3)
        volume = square.volume()
        self.assertEqual(volume, 27)

    def test_cube_volume(self):
        """Test the volume calculation of a cube."""
        cube = Cube(side=3)
        self.assertEqual(cube.volume(), 27)

    def test_invalid_circle(self):
        """
        Test case for creating an invalid circle with negative radius.

        This test case verifies that a `ValidationError` is raised when trying to create a circle with a negative radius.
        """
        with self.assertRaises(ValidationError):
            Circle(radius=-5)

    def test_invalid_square(self):
        """
        Test case to verify that a Square with a negative side length raises a ValidationError.
        """
        with self.assertRaises(ValidationError):
            Square(side=-4)

    def test_invalid_triangle(self):
        """
        Test case to verify that a Triangle with invalid dimensions raises a ValidationError.
        """
        with self.assertRaises(ValidationError):
            Triangle(base=-3, height=4)

    def test_invalid_cube(self):
        """Test validation for invalid cube side length."""
        with self.assertRaises(ValidationError):
            Cube(side=-3)    

    def test_total_area_optimized(self):
        """Test total area calculation using the optimized function."""
        shapes = [
            Circle(radius=5),
            Square(side=4),
            Triangle(base=3, height=4),
            Cube(side=2)
        ]
        total_area = total_area_optimized(shapes)
        expected_area = (
            Circle(radius=5).area() +
            Square(side=4).area() +
            Triangle(base=3, height=4).area() +
            Cube(side=2).area()
        )
        self.assertAlmostEqual(total_area, expected_area, places=4)


if __name__ == "__main__":
    unittest.main()