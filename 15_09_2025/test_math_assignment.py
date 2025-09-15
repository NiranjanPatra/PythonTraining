import math_assignment
import pytest

def test_factorial():
    assert math_assignment.factorial(3) == 6

def test_prime_number():
    assert math_assignment.prime_number(3) == True

def test_area_Of_circle():
    assert math_assignment.area_Of_circle(7) == 154
