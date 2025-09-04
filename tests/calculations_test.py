# System Modules
import sys
import os
import math

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
 """Test with n=10."""
 # Arrange
 n = 10
def test_area_of_circle_negative_radius():
    """Test with a negative radius should raise ValueError."""
    try:
        area_of_circle(-1)
        assert False, "Expected ValueError for negative radius"
    except ValueError as e:
        assert str(e) == "Radius cannot be negative"

def test_area_of_circle_float_radius():
    """Test with a float radius."""
    radius = 2.5
    result = area_of_circle(radius)
    assert abs(result - (math.pi * radius ** 2)) < 1e-5

def test_get_nth_fibonacci_negative():
    """Test with negative n should raise ValueError."""
    try:
        get_nth_fibonacci(-5)
        assert False, "Expected ValueError for negative n"
    except ValueError as e:
        assert str(e) == "n cannot be negative"

def test_get_nth_fibonacci_two():
    """Test with n=2."""
    n = 2
    result = get_nth_fibonacci(n)
    assert result == 1

def test_get_nth_fibonacci_three():
    """Test with n=3."""
    n = 3
    result = get_nth_fibonacci(n)
    assert result == 2

def test_get_nth_fibonacci_large():
    """Test with a large n."""
    n = 20
    result = get_nth_fibonacci(n)
    assert result == 6765
