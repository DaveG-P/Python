# Chapter 6 Dictionaries
# --- 6.1 ---
person = {
    'first': 'Francois - Marie',
    'last': 'Arouet',
    'Born': 1694,
    'died': 1778,
    'city': 'paris',
    }

# Print each piece of information
print(person)
print("My favourite enlightment philospher is " + person['first'] + ".")
print("He was born in " + person['city'].title())


# --- 6.2 ---
# Create dictionary with peoples favourite numbers
people = {
    'Volaire': 1694,
    'Hume': 1711,
    'Locke': 1632,
    'Rousseau': 1712,
    'Spinoza': 1632,
    }

print(people)
print("Volaire's favourite number is " + str(people['Voltaire']))
print("Hume's favourite number is " + str(people['Hume']))
print("Lockes' favourite number is " + str(people['Locke']))
print("Rousseau's favourite number is " + str(people['Rousseau']))
print("Spinoza's favourite number is " + str(people['Spinoza']))

# --- 6.3 ---
# Creating a glossary of list of terms I hae learned so far
python_glossary = {
    "variables": "a value associated with variable",
    "strings": "A series of characters inside qoutes",
    "Numbers": "Integers or floats(numbers with decimals)",
    "Comments": "Allows use to write notes about the code using #",
    "method": "an action that python can perform on a piece of data",
    "title()": "Methods turns forst lower case letter to capital",
    "upper()": "Method turns all lowercase letters yp upper case",
    "lower()": "Method turns all uppercase letters to lowercase",
    "str()": "Turns a numerical value into a string",
    "concatenation": "Combining strings and variables with a plus sign",
    "white space": "Any nonprinting character (spaces)",
    "strip()": "stripes white space on either side",
    "syntax error": "Python does not recognize a section of a program",
    "type error": "Python can't recognize the kind of inforrmation you're using",
}

# Printing each term and its meaning
print("A variable is: " + python_glossary['variables'])
print("Strings are" + python_glossary['strings'])
print("The syntax error is when: " + python_glossary["syntax error"])
print("Concatenation: " + python_glossary["concatenation"])
print("Methods are: " + python_glossary['methods'])
print("White space is: " + python_glossary['white space'])
# --- 6.4 ---
# Looping through dictionary
for k, v in python_glossary.items():
    print("Keys " + k)
    print("Value: " + v)
print("Here is my current glossary")

# Adding new terms to the python_glossary
python_glossary["list"] = "A collection of items"
python_glossary["index"] = "Location of items starting from 0"
python_glossary["append()"] = "Adds an element to the list"
python_glossary["insert()"] = "Adds an element to list by spefifying the index"
python_glossary["del statement"] = "permantly removes items"
python_glossary["pop()"] = "removes last item on the list"
python_glossary["remove()"] = "Removes item by value"
python_glossary["sort()"] = "orders list in alphabetical order"
python_glossary["reverse()"] = "reverses the order of the list"
python_glossary["len()"] = "tells the length if the list"

# --- 6.5 ---
# Making a dictionary  about rivers
rivers = {
    'nile': 'africa',
    'amazon': 'south america',
    'yangtze': 'asia',
    'mississippi': 'north america',
    'yenisei': 'europe',
}
# using a loop to print out something about each ruver
for river, continent in rivers.items():
    print("The " + river.title() + " river is the longes river in " + continent.title())
# Loop to print out the key value
for river in rivers.keys():
    print(river.title())
# Loop to print out key values
for continent in rivers.values():
    print(continent.title())
# --- 6.6 ---
# Creating a poll
favorite_languages = {
    'jen': 'python',
    'jonathan': 'c',
    'jimmy': 'ruby',
    'susie': 'java',
}

for name in favorite_languages.keys():
    print("Hi " + name.title() + " thanks for taking the poll")

people = ['sean', 'rachael']
for p in people:
    if p in favorite_languages.keys():
        print("Thank you for taking the poll, " + p.title())
    else:
        print(p.title() + ", what is your favourite language?")

# --- 6.7 ---
# creating two new dictionaries and adding them to a list
philosophers = []
person = {
    'first': 'Francois - Marie',
    'last': 'Arouet',
    'Born': 1694,
    'died': 1778,
    'city': 'paris',
    }
philosophers.append(person)
person = {
    'first': 'David',
    'last': "Hume",
    'born': 1711,
    'died': 1776,
    'city': 'edinburg',
}
philosophers.append(person)
person = {
    'first': 'john',
    'last': 'locke',
    'born': 1732,
    'died': 1704,
    'city': 'wrington',
}
philosophers.append(person)

print("Total number of philosphers in list: " + str(len(philosophers)))

for person in philosophers:
    name = person['first'].title() + person['last'].title()
    birth = str(person['born'])
    dead = str(person['died'])
    city = person['city'].title()

    print(name + " born on" + birth + ", in the city of " + city)
# --- 6.8 ---
# creating several dictionaries on pets
teams = []

team = {
    'name': 'barcelona',
    'estadio': 'camp nou',
    'ubicacion': 'cataluna',
    'entrenador': 'valverde',
}
teams.append(team)
team = {
    'name': 'atletico madrid',
    'estadio': 'metropolitano',
    'ubicacion': 'madrid',
    'entrenador': 'simeone',
}
teams.append(team)
team = {
    'name': 'real madrid',
    'estadio': 'bernabeu',
    'ubicacion': 'madrid',
    'entrenador': 'zidane',
}
teams.append(team)

# Displaying information about each team
for k, v in teams.items():
    print(k)
    print(v)
# --- 6.9 ---
places = {
    'david': ['miami', 'zona cafetera', 'bay area'],
    'john': ['los angeles', 'yosemite', 'berkeley'],
    'raphael': ['rio', 'miami', 'oakland'],
}
for name, place in places.items():
    print("\n" + name.title() + " likes the to visit these places: ")
    for place in places:
        print("\t" + place.title())
# --- 6.10 ---
favorite_numbers = {
    'david': ['415', '513', '607'],
    'felipe': ['754', '246', '214'],
    'sandra': ['954', '465', '760'],
    'ricardo': ['305', '316', '936'],
}
# Printing each person name along with their favorite numbers
for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favourite numbers are: ")
    for number in numbers:
        print("\t" + str((numbers))
# --- 6.11 ---
cities = {
    'bogota': {
        'country': 'colombia',
        'population': 8081000,
    },
    'cuidad de mexico': {
        'country': 'mexico',
        'population': 8851000
    },
    'sao paulo': {
        'country': 'brazil',
        'population': 14710000,
    },
}
