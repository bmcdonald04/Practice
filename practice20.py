# Dictionary.py
# Author: A. N. Other
# Date: September 2016

# Define a dictionary of car values with registration numbers as keys
dictionary_1 = {"V344LDA": 2000, "J245DWE": 6350, "K265QWS": 500}

# Retrieve a value from the dictionary using a key
print("The car with registration V344LDA is worth $", dictionary_1["V344LDA"])

# Create dictionaries for state abbreviations and cities
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add more cities to the cities dictionary
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities
print('-' * 10)
print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])

# Print some state abbreviations
print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

# Access cities using the state abbreviations
print('-' * 10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

# Print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print("{0} is abbreviated {1}".format(state, abbrev))

# Print every city in each state
print('-' * 10)
for abbrev, city in cities.items():
    print("{0} has the city {1}".format(abbrev, city))

# Print both state abbreviation and city
print('-' * 10)
for state, abbrev in states.items():
    print("{0} state is abbreviated {1} and has city {2}".format(
        state, abbrev, cities[abbrev]))

# Safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: {0}".format(city))
