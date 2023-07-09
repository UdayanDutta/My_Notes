import math

def is_perfect_square(n):
    # Check if the square root of n is an integer
    return math.isqrt(n)**2 == n

def is_fibonacci(number):
    # Check if the number is a perfect square of a Fibonacci number
    return is_perfect_square(5 * number**2 + 4) or is_perfect_square(5 * number**2 - 4)

# Example usage
number = int(input("Enter a number: "))

if is_fibonacci(number):
    print(number, "is a Fibonacci number")
else:
    print(number, "is not a Fibonacci number")
