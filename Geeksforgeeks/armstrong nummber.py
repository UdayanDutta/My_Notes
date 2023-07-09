def armstrong_number(number):
    # Convert the number to a string to get the number of digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate the sum of the digits raised to the power of the number of digits
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_digits

    # Check if the sum is equal to the original number
    if sum == number:
        return True
    else:
        return False

# Example usage
number = int(input("Enter a number: "))
if armstrong_number(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
