# Lists.py
# Author: A. N. Other
# Date: September 2016

# Creating an empty list
my_list = []

# Creating a list of integers
my_list = [1, 2, 3]

# Creating a list with mixed datatypes
my_list = [1, "Hello", 3.4]

# Creating a nested list
my_list = ["mouse", [8, 4, 6]]

# Accessing elements from a list
my_list = ['p', 'r', 'o', 'b', 'e']

# Accessing elements by index
# Output: p
print(my_list[0])
# Output: o
print(my_list[2])
# Output: e
print(my_list[4])

# Nested list
n_list = ["Happy", [2, 0, 1, 6]]

# Accessing elements from a nested list
# Output: a
print(n_list[0][1])
# Output: 5
print(n_list[1][3])

# Using negative indexing
# Output: e
print(my_list[-1])
# Output: p
print(my_list[-5])
