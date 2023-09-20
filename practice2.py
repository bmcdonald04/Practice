# Baby.py
# Author: A. N. Other
# Date: September 2016

import random

# Generate a random boolean value to represent gender (True for male, False for female)
is_male = random.choice([True, False])

# Determine and print the name based on gender
name = "Rangi" if is_male else "Anihera"
print(f"We will use the name {name}")
