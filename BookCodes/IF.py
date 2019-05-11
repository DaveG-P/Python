# Chapter 5
# Example
cars = ['audi', 'bmw', 'mazda', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Conditional tests
# cheching for equalty
car = 'audi'
car == 'audi'  # True
# False
car = 'audi'
car == 'Audi'
car == 'bmwe'  # False

# checking for inequality
bikes = 'schwinn'
if bikes != 'honda':
    print("There is no honda")

# Numerical comparisons
age = 18
age == 18  # True

answer = 17
if answer != 21:
    print("That is not the correct answer")

age = 40
age < 100  # True
age <= 50  # True
age > 50   # False
age >= 50  # False

# Checking multiple conditions
# Using AND
age_0 = 22
age_1 = 18
age_2 = 24
age_0 >= 21 and age_1 >= 21  # False
(age_0 >= 21) and (age_2 >= 21)  # True

# Using OR in conditional tests
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21  # True
age_0 = 18
age_0 >= 21 or age_1 >= 21  # False

# Checking if value is in a list using 'IN'
'ducati' in motorbikes  # True or False if it is in the list
'bmw' in motorbikes  # True or False if its is in the list

# Checking if value is NOT in a list
black_list = ['andrew', 'carolina', 'david']
user = 'maria'

if user not in black_list:
    print(user.title() + ", you arenot in the band list.")

# Boolean Expressions True or False

# IF statements
age = 19
if age >= 18:
    print("you are old enough to vote!")
    print("Have you registred to vote")
# IF else
age = 17
if age >= 18:
    print("You are old enough to vote")
else:
    print("You are too young to vote")
# if elif else chain
age = 12

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10.")
# other way of doing it
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# You can add more elif blocks
# Omitt the else block

# Test multiple conditions usinng if
if 'ducati' in motorbikes:
    print("Ducati is on the list")
if 'triumph' in motorbikes:
    print("triumph is in the list")

# Using if statements with lists
for car in cars:
    if car == 'mazda':
        print("That car is in the list")
    else:
        print(car.title() + " is not in the list")

# Checking that a list is not empty
games = []

if games:
    for game in games:
        print("Adding " + game + ".")
    print("\nAdded a game to the list")
else:
    print("Are you sure you want to add that")

# Using multiple lists
bikes = ["triumph", 'honda', "ducati", "enfield"]
cars = ["bmw", 'mazda', "audi", "mercedes"]

for bike in bikes:
    if bike in cars:
        print("That is in the list already")
    else:
        print("That is not in the list")
    
