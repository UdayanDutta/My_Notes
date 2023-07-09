def fibonacci_multiple(n, multiple):
    # Check if n is 1 (base case)
    if n == 1:
        return multiple

    # Initialize variables for the first two Fibonacci numbers
    fib_0 = 0
    fib_1 = 1

    # Iterate until we find the nth multiple
    count = 0
    while count < n:
        fib_n = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = fib_n

        # Check if the current Fibonacci number is a multiple
        if fib_n % multiple == 0:
            count += 1

    return fib_n

# Example usage
n = int(input("Enter the value of n: "))
multiple = int(input("Enter the value of the multiple: "))

result = fibonacci_multiple(n, multiple)
print("The", n, "th multiple of", multiple, "in the Fibonacci series is:", result)
