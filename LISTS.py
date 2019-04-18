# Chapter 3 Lists
# What a list looks like
motorbikes = ["Harley davidson", "indian", "kawasaki", "bmw", "honda", "suzuki", "ubco", "yamaha", "royal enfield", "can am ryker"]
print(motorbikes)

# Accessing Elements in a list by the index
# First item in a list is 0
print(motorbikes[1])  # Indian
print(motorbikes[7])  # Yamaha
print(motorbikes[4].title())
# Accessing the last item on the list
print(motorbikes[-1])  # can am ryker
print(motorbikes[-2])  # royal enfield

# Using individual values from a List
message = "The motorcycle of my dreams is " + motorbikes[-2] + "."
print(message)

# Modifying elements in a list
# replacing value in index 0 with new value eliminating old one
motorbikes[0] = 'ducati'

# Adding element to the List
motorbikes.append('ducati')  # Adds this to the end of the List

# Other ways of adding to List
motorbikes = []
motorbikes.append("harley davidson")
motorbikes.append("triumph")
motorbikes.append("royal enfield")

# Inserting elements into a List
motorbikes.insert(0, 'bmw')
print(motobikes)

# Removing elements from a List
# del statement
del motorbikes[5]  # deletes it permenantly
# pop()
# Good for keeping track of what is deleted
popped_item = motorbikes.pop()
# popping items from any position in a List
motobikes.pop(4)

# Removing item by a values
motorbikes.remove('ubco')

not_interested = 'ubco'
motorbikes.remove(not_interested)
print("\nNot interest in the " + not_interested.title())

# Organizing a List using the sort()
motorbikes.sort()  # orders in alphabetical order
print(motorbikes)
motorbikes.sort(reverse=True)  # Reverse alphabetical order
print(motorbikes)

# list in reverse order
motorbikes.reverse()  # Reverses the order backwards not alphabetically

# Finding the length of the List
len(motorbikes)

# Chapter 4 Working with lists
# For loop
# dont forget to indent, colon
for bikes in motorbikes:
    print("This is a list of " + bikes.title())  # prints ever item in the list
    print("I love this bike")
# After a for loop
print("One day I will ride all of these")

# Making numerical Lists
for value in range(1, 21):
    print(value)  # prints 1 - 20

# Making a list out the numbers
numbers = list(range(1, 21))
print(numbers)

# Getting the list of even numbers
even_numbers = list(range(2, 27, 2))
print(even_numbers)

# Basic stats
min(numbers)
max(numbers)
sum(numbers)

# Slicing a list
motorbikes[0:4]  # items 0 to 3
motorbikes[2:8]  # Second index to 7
motorbikes[0:6]  # Beginning of list to 5 items
motorbikes[2:]   # Third item to list
motorbikes[-3:]  # The last three items

# Looping through slice
print("Here are the first three items")
for bikes in motorbikes[0:3]:
    print(bikes.title())

# Copying a list [:]
friends_favorite = motorbikes[:]
# This does not Work
friends_favorite = motorbikes

print("My favorite bikes are: ")
print(motorbikes)

print("My friends favorite bikes are: ")
print(friends_favorite)

motorbikes.append('triumph')
friends_favorite.append('scooter')

# Tuples use (), items cannot be modified
