def cube_sum(n):
    # Calculate the sum of cubes using the formula (n * (n + 1) / 2)^2
    sum = (n * (n + 1) // 2) ** 2
    return sum

# Example usage
n = int(input("Enter the value of n: "))

result = cube_sum(n)
print("The cube sum of the first", n, "natural numbers is:", result)
