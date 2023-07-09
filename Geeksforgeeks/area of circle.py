def calculate_area(radius):
    # Calculate the area using the formula
    pi=3.142
    area = pi * radius**2
    return area

# Example usage
radius = float(input("Enter the radius of the circle: "))

area = calculate_area(radius)
print("The area of the circle is:", area)
