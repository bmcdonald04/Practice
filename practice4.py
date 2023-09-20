# DateTest.py
# Author: A. N. Other
# Date: September 2016

from datetime import datetime, timedelta

date_input = input("Please enter your DOB in the format DD MM YYYY (e.g., 20 12 1978): \n")

# Cast the input to a datetime object
date_object = datetime.strptime(date_input, '%d %m %Y')

# Output some confirmation
print("The year entered is", date_object.year, "\n")

# Calculate age
my_age = datetime.today() - date_object

# Show the result in different formats
print("My exact age is", my_age.days, "days, ", my_age, "\n")
print("My exact age just in days is", my_age.days, "days\n")
print("My exact age just in years is", int(my_age.days / 365), "years\n")

# Add 10 days to my current age
ten_days_later = datetime.today() + timedelta(days=10)
print("In 10 days time, my age will be", ten_days_later, ".\n")

# Add my current age to today's date
double_age_date = datetime.today() + my_age
print("I will be double my age in", double_age_date, ".")

