# Chapter III
# --- 3.1 ---
# creating a list and accessing each element in the list
names = ["Maria", "John", "Rafaeil", "Aly", "Stella"]
print(names[2])
print(names[1])

# --- 3.2 ---
message = "The first name on my list of friends is " + name[0]
print(message)
# --- 3.3 ---
transport = ['prius', 'triumph', 'mazda', 'subaru', 'vincent']
wish = "I would love to own a " + transport[1].title() + " someday."
wish1 = "I want to test drive " + transport[2].title() + " it looks fun to drive"
wish3 = "I want to take a roadtrip with " + transport[3].title()

print(wish)
print(wish1)
print(wish3)
# --- 3.4 ---
guests = []
guests.append('voltaire')
guests.append('van gogh')
guests.append('hume')
guests.append('galilaeo')
guests.append('turing')
guests.append('vigee')
guests.append('da vinci')

print(guests)
print("Hello " + guests[0] + " I am honored to have you at my dinner party")
# --- 3.5 ---
print("I am sad to say but " + guests[4].title() + " cannot make it to the party")

canceled = guests.pop(4)
print(canceled.title() + " cannot make it to the party")

guests.insert(4, "einstein")
print("Every body I would like you all to welcome " + guests[4].title() + " to the party")
# --- 3.6 ---
print("Good news I found a bigger table and have invited more people to the party")

len(guests)
guests.insert(0, "locke")
guests.insert(6, 'buddha')
guests.append("rembrandt")
print("Hello " + guests[0].title() + ',' + guests[5].title() + ',' + guests[13].title() + ' welcome to the party.')
# --- 3.7 ---
print('Guys I have really bad news but the table shrunk and can only invite two people')
guests.pop()
message = "Good news " + guests[0].title() + ", " + guests[1].title() + " you guys are still invited"
print(message)
# --- 3.8 ---
del guests[0]
del guests[1]
print(guests)
# --- 3.9 ---
world = ["mongolia", "azerbaijan", "russia", "uk", "croatia"]
world

print(sorted(world))
print(world)

print(sorted(world, reverse=True))
print(world)

world.reverse()
print(world)

world.reverse()
print(world)

world.sort()

world.sort(reverse=True)
# --- 3.10 ---
len(guests)

# Chapter IV
# --- 4.1 --
pizza = ["margarita", "chicken", "truffle mushrooms"]
for p in pizza:
    print(p)

for p in pizza:
    print(i.title + " is my favourite pizza at Whole Foods.")
print("These are my favourite pizza")

# --- 4.3 ---
for x in range(1, 21):
    print(x)

# --- 4.4 ---
numbers = []
for value in range(1, 10000001):
    numbers.append(value)

print(numbers)

# --- 4.5 ---
min(numbers)
max(numbers)
sum(numbers)

# --- 4.6 ---
for x in range(1, 21, 2):
    print(x)

# --- 4.7 ---
three = []
for value in range(1, 31):
    three.append(value*3)
print(three)

# --- 4.8 ---
cubes = []
for x in range(1, 11):
    cubes.append(x**3)
print(cubes)

# --- 4.9 --
cubes = [x**3 for x in range(1, 11)]
print(cubes)

# --- 4.10 --
players = ["oblak", "felipe luis", "godin", "gimenez", "arias", "lemar", "partey", "saul", "koke", "griezmann", "morata"]
print("The first three players on the team are")
for p in players[:3]:
    print(p.title())

print("The next players on the lineup are:")
for p in players[3:8]:
    print(p.title())

print("The remaining players for the lineup are")
for p in players[-3:]:
    print(p.title())

# --- 4.11 --
pizza = ['margarita', 'chicken', 'truffle mushrooms']
gfs_pizzas = pizza[:]
pizza.append("hawaiian")
gfs_pizzas.append("four cheese")

print("These are my favourite pizzas")
for p in pizza:
    print(p)

print("These are my girlfriends favourite pizzas")
for p in gfs_pizzas:
    print(p)
# --- 4.12 --
buffet = ("pizza", "lobster", "chef salad", "macaroni and cheese", "tomatoe soup")
for b in buffet:
    print(b)

buffet[0] = crab

# --- 4.13 --
buffet = ("pizza", "lobster", "chef salad", "macaroni and cheese", "tomatoe soup")
for b in buffet:
    print(b)

buffet[0] = crab

buffet = ('pizza', 'clams', 'cesear salad', 'macaroni and cheese', 'tomatoe soup')
for b in buffet:
    print(b)
