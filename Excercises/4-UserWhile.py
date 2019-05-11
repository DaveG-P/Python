# Chapter 7
# ---7.1 ---
car_rental = input("What car would you like to rent today? ")
print("Let me check if we have a " + car_rental + " available for you")

# ---7.2---
message = input("Welcome, how many people are in your part?")
message = int(message)

if message > 8:
    print("The wait time is about 20 minutes")
else:
    print("please follow me this way")
# ---7.3 ---
number = input("Please enter a number")
number = int(number)

if number % 10 == 0:
    print("That number is divisible by 10")
else:
    print("That number is not divisible by 10")

# WHILE LOOPS
# ---7.4 ---
prompt = "\nPlease enter the topping you would like on the pizza"
prompt += "\nenter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("Thanks I'll add" + topping + " to your pizza")
    else:
        break

# ---7.5 ---
prompt = "\nHow old are you?"
prompt += "\nEnter 'quite' when finished: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("Movie is free for children under 3")
    elif number < 13:
        print("Ticket is $10")
    else:
        print("Ticket is $15")

# ---7.8 ---
order = ["black foreest ham", "meatball", "italian", "roasted chiken", "club", "veggie"]
completed = []

while order:
    current = order.pop()
    print("Working on your " + current + " sandwich")
    completed.append(current)
print("\n")
for sandwich in completed:
    print("I made a " + sandwich + " sandwich.")

# ---7.9 ---
orders = ["black foreest ham", "meatball", "italian", "roasted chiken", "club", "veggie", "pastrami"]
completed = []

print("Sorry we're out of pastrami today.")
while 'pastrami' in order:
    order.remove('pastrami')

print("\n")
while orders:
    current = orders.pop()
    print("I'm working on your " + current + " sandwich.")
    completed.append(current)

print("\n")
for sandwich in completed:
    print("I made a " + sandwich + " sandwich")

# ---7.10 ---
name = "\n what is your name? "
place = "Where would you like to visit in the future? "
continue_prompt = "\nWould you like to let anyone else respond? (yes/no) "

# Responses stored in form of {name: place}
responses = {}

while True:
    # Ask user where they want to go
    names = input(continue_prompt)
    places = input(place)

    # Store Responses
    responses[name] = place

    # Ask if theres anyone else
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of survey
print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")
