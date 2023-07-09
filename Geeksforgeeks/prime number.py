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
start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))

print("Prime numbers in the interval [" + str(start) + ", " + str(end) + "]:")
for number in range(start, end + 1):
    if is_prime(number):
        print(number)
