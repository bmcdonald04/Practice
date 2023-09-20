# BooleanNot.py
# Author: A. N. Other
# Date: September 2016

is_full_attendance = True
is_mark_below_pass = False

# Test case assertion 1: result should be True
print("The student's success status is....")
print(is_full_attendance and not is_mark_below_pass, "\n")

print("Student failed their exam...")

# Test case assertion 2: result should be False
is_mark_below_pass = True
print("The student's success status is now....")
print(is_full_attendance and not is_mark_below_pass, "\n")
