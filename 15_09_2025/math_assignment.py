import math

def multiply(a,b):
    return a * b

def factorial(n):
    val = 1
    for i in range(1, n + 1):
        val *= i

    return val


def prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False 
        
    return True

def area_Of_circle(radius):
    if (radius == 0):
        raise "Zero error"

    area = (22*radius*radius)/7
    return area;