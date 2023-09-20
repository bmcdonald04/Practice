# CompoundShape2.py
# Author: A. N. Other
# Date: September 2016

# Getting user inputs
a = int(input("Please enter the length of a:\n"))
b = int(input("Please enter the length of b:\n"))

# Calculate the areas of the two parts
area_a = a ** 2
area_b = b * a

# Calculate the total area
total_area = area_a + area_b

# Print the result
print("The area of your shape is", total_area)
