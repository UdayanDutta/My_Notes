def sum_of_squares(n):
    # Calculate the sum of squares using the formula n*(n+1)*(2n+1)/6
    sum = n * (n + 1) * (2 * n + 1) // 6
    return sum

# Example usage
n = int(input("Enter the value of n: "))

result = sum_of_squares(n)
print("The sum of the squares of the first", n, "natural numbers is:", result)
