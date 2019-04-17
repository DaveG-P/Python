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
