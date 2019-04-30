# Chapter 8

# ---8.1 ---
def display_message():
    """Prints one sentence telling everyone what what I am learning """
    print("Hello there I am currently learning how to write functions")

display_message()

# ---8.2 ---
def favorite_book(book):
    """Displays favorite book """
    print("One of my favourite books is " + book.title() + "!")

favorite_book("alice in wonderland")

# ---8.3 ---
def make_shirt(size, message):
    """Displays information about the t-shirt"""
    print("\nThe short size is " + size.upper())
    print("The t-shirt says " + message.title())

make_shirt('l', 'interpol')
make_shirt('m', 'yes we can')
make_shirt('s', 'daddy's little princess)

# ---8.4 ---
def make_shirt(message, size='L'):
        """Displays information about the t-shirt"""
        print("\nThe short size is " + size.upper())
        print("The t-shirt says " + message.title())

make_shirt("I love python")
make_shirt(I love python', m)

# ---8.5 ---
def describe_city(city, country):
    """Displays the name of the city and its country """
    print(city.title() + " is located in " + country.title())
    # OR
    # msg = city.title() + " is in " + country.title() + "."
    # print(msq)
describe_city('madrid', spain)
describe_city('london', 'united kingdom')
describe_city('paris', 'france')

# ---8.6 ---
def city_country(city, country):
    """Displays city and country """
    city_country = city + ', ' + country
    return city_country.title()

nation = city_country('bogota', 'colombia')
print(nation)

nation = city_country('caracas', 'venezuela')
print(nation)

nation = city_country('buenos aires', 'argentina')
print(nation)

# ---8.7 ---
def make_album(artist, album, tracks=0):
    """Describes a Music Album """
    rappers_dict = {
        'name': artist.title(),
        'album': album.titke()
        }
    if tracks:
        rappers_dict['tracks'] = tracks
    return rappers

artist = make_album('mf doom', 'madvilliany')
print(artist)

artist = make_album('czarface', "medetal face")
print(artist)

artist = make_album('nas', 'ny state of mind')
print(artist)

# ---8.8 ---
def make_album(artist, title, tracks=0):
    """Build Dictioary containing information about an album"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict
# Prompts
album_prompt = "\nPlease enter an album"
artist_prompt = "Please enter the artist"

# How to quit
print("Enter 'quit' at any time to stop.")

while True:
    title = input(album_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)
print("\nThanks for responding!")

# ---8.9 ---
magicians = ['emma', 'david', 'randy', 'tyler']

def showMagicians(names):
    """Displays names of each magician"""
    for name in names:
        mesg = "Hello, " + n.title() + '!'
        print(msg)

showMagicians(magicians)

# ---8.10 ---
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)

# ---8.11 ---
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)

# ---8.12 ---
ordered_sandwich = ['whole wheat', 'chicken', 'provolone']
def sandwich(*ingredients):
    """Prints a list of items for a sandwich"""
    print("\nMaking a Subway sandwich with the following ingredients")
    for ingredient in ingredients:
        print("- " + ingredient.title())

sandwich('whole wheat', 'provolone cheese', 'chicken', 'spinach')
sandwich('tomatoe', 'onions', 'black olives')
sandwich('black peppers', 'olive oil')

# ---8.13 ---
def build_profile(first, last, **user_info):
    """Build dictionary containing everything we know about a user """
    profile = {}
    profile['first_name'] = first
    profile['las_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('david', 'esteban', 'gonzalez', city='berkeley', field='psychology')
print(user_profile)

# ---8.14 ---
def motorcycle_profile(make, model,  **info):
    motorcycle = {}
    motorcycle['make'] = make
    motorcycle['model'] = model
    for key, value in info.items():
        motorcycle[key] = value
    return motorcycle

motorcycles = motorcycle_profile('vincent', 'black lightning', cylinders=998, bhp=70 )
print(motorcycle_profile)

# Example 2
def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_accord)
