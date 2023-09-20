# Baby.py
# Author: A. N. Other
# Date: September 2016

import random

# Generate a random boolean value to represent gender (True for male, False for female)
is_male = bool(random.randint(0, 1))

# Determine and print the name based on gender
if is_male:
   print("We will use the name Rangi")
else:
   print("We will use the name Anihera")

