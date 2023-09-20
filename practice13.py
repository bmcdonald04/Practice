# WhileLoops.py
# Author: A. N. Other
# Date: September 2016

is_running = True

while is_running:
    answer = input("What is the meaning of life?...\n")
    if answer == "42":
        print("Correct! Well done!\n")
        # Correct answer, so exit loop - reset is_running
        is_running = False
    else:
        print("Sorry, that is the wrong answer. Try again!\n")

print("Thank you for playing. You can now exit the program.")
input("Press Enter to exit.")
