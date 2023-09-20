# Timer.py
# Author: A. N. Other
# Date: September 2016

from datetime import datetime, timedelta

# Set the duration for the timer in seconds
duration = 5

# Prompt the user to enter 's' to begin the timer
run = input("Enter 's' to begin...")

# Define the time period for one second
period = timedelta(seconds=1)

# Calculate the time when the next second will be reached
next_time = datetime.now() + period

counter = 0

# Run the timer as long as 's' is entered and the counter is less than the duration
while run == 's' and counter < duration:
    if next_time <= datetime.now():
        print("..", counter)
        counter += 1
        # Reevaluate the next_time variable for the next second
        next_time += period
