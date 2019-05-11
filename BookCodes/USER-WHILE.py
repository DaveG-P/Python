# How the input function works
message = input("Tell me something and I will repeat it back to you: ")
print(message)

name = input("Please tell me your name: ")
print("Hello, " + name + '.')

# Python interprets everything the user enters as a string
height = input("How old are you?")
height = int(height)

if height >= 21:
    print("\nYou are old enough to drink")
else:
    print("\nYou need to go back home")

# The modulo operator %
# When number is divisible by another number the amswer is 0
number = input("entr a number, and i'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 4:
    print("\nThe number" + str(number) + " is even")
else:
    print("\nThe number " + str(number) + " is odd")

# While LOOPS
number = 1
while number <= 5:
    print(number)
    number += 1

# letting the user choose when to quite
# define a quit value
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program> "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# Using a flag
# flag acts as a signal to the prgram to stop
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program "
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Break stament to leave LOOP
prompt = "\nTell me the name of a city you visited: "
prompt += "\nEnter 'quit' when finished. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I would love to go to " + city.title() + " someday")

# Continue statement
# Returns to the beginning of the loop based on the result of the cond tests
# Result is in odd numbers printing
number = 0
while number < 10:
    number == 1
    if number % 2 == 0:
        continue
    print("number")

# While loops with lists and dictionaries

# Moving items from one list to another
unconfirmed = ['alice', 'steve', 'ivan']
confirmed = []

while unconfirmed:
    current = unconfirmed.pop()

    print("Verifying user: " + current.title())
    confirmed.append(current)
print("\nThe following people have been confirmed")
for conf in confirmeds:
    print(confirmed.title())

# Removing instances of specific value from lists
pets = ["dog", "cat", "bird", "snake", "cat", "rabbit", "cat"]
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)


# Filling a dictionary with user input
responses = {}

# Flag  to indicate polling is active
polling_active = True

while polling_active:
    # Ask for the person name and responses
    name = input("\nWhat is your name? ")
    response = input("Which city would you like to see today? ")

    # Store response in a dictionary
    responses[name] = response

    # Find out if anyone else will take polling
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the result
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to visit " + response + ".")
