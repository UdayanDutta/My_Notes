def is_prime(number):
    # Check if the number is less than 2 (not prime)
    if number < 2:
        return False

    # Check if the number is divisible by any integer from 2 to number-1
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

# Example usage
number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
