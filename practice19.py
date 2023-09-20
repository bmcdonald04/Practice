# Tuple.py
# Author: A. N. Other
# Date: September 2016

# Define a tuple of bank account information
bank_accounts = (("Joe", 33, "234 Great South Road", "022629107"),
                 ("Tama", 6000),
                 ("Suzanne", 21025, "45 Green Lane"),
                 ("Anihera", -75))

# Print the number of bank accounts in the tuple
print("The number of bank accounts is", len(bank_accounts))

# Iterate through the bank account tuples and display names and balances
for i in bank_accounts:
    print("\nThe name is", i[0], "and the balance is $", i[1])

# Iterate through the bank account tuples and display names with addresses (if available)
for i in bank_accounts:
    if len(i) > 2:
        print("\nThe name is", i[0], "and the address is", i[2])
