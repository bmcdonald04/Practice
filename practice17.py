# ListIterate.py
# Author: A. N. Other
# Date: September 2016

# Sample list
sample_list = [1, 4, 5, 2, 9, 12]

# Iterating through the list and printing each item
for item in sample_list:
    print("An item in the sample list is", item)

# If you need both the index and the item, use the enumerate function
for index, item in enumerate(sample_list):
    print("The element index is", index, "and the value is", item)

# If you need only the index, use range and len
for index in range(len(sample_list)):
    print("The element index is", index)

# Creating an iterator explicitly using the iter function
i = iter(sample_list)
item = next(i)  # Fetch the first value
print("An item in the sample list is", item)
item = next(i)  # Fetch the second value
print("An item in the sample list is", item)

# Calculating the sum of list items
list_sum = sum(sample_list)
print("\nThe sum of the items in the list is", list_sum)

subtotal = 23
total = sum(sample_list, subtotal)
print("The sum of the items in the list and another number is", total)

average = float(sum(sample_list)) / len(sample_list)
print("The average of the items in the list is", average)

# Joining string elements in a list into a single string
haka_list = ["Taringa", "whakarongo!", "Kia", "rite!", "Kia", "rite!"]
joined_list = " ".join(haka_list)
print("\nThe joined list is", joined_list)
