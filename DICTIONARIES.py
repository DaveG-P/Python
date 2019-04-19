# Chapter 6
# A simple dictionary
person = {'name': 'david', 'eyes': 'brown', 'age': 28}
print(person['name'])
print(person['eyes'])
# Accessing values in a dictionary
print(person['name'])
# If there is a number in value  use str()
print(person['age'])

# Adding new key-valu pairs
person['dominate side'] = 'left'
person['city'] = 'bogota'

# Starting with an empty list
countries = {}

countries['country'] = 'france'
countries['capital'] = 'paris'

# Modifying values in dictionary
countries['capital'] = 'nice'
print("The new capital of France is " + countries['capital'])

# another example
France = {
    'capital': 'paris',
    'idioma': 'frances',
    'presidente': 'emmanuel macron',
    'moneda': 'euro',
    }

# Removing key value pairs
del France['moneda']

# A dictionary of similar objects
languages = {
    'jen': 'python',
    'david': 'python',
    'andre': 'C ++',
    'felipe': 'javascript',
    }
print("David's favorite language is " + languages['david'].title() + ".")

# Looping through a dictionary
# Looping through all key values
for k, v in France.items():
    print("\nKey: " + k)
    print("\nValue: " + v)

# Looping though all the keys
for key in France.keys():
    print(key.title())

friends = ['jen', 'andre']
for name in languages.keys():
    print(name.title())

    if name in firends:
        print("HI " + name.title()

# Looping though keys in order
for key in sorted(France.keys()):
    print(name.title() + ".")

# Looping through all values
print("Here are the following facts about France")
for value in France.values():
    print(value.title())

# Using set pulls out uniquge values
for language in set(languages.values()):
    print(language.title())

# Nesting
# List of dictioaries
France = {'capital': 'paris', 'idioma': 'frances'}
Spain = {'capital': 'madrid', 'idioma': 'catellano'}
UK = {'capital': 'londres', 'idioma':'ingles'}

countries = [France, Spain, UK]
for country in countries:
    print(country)

# A list in a dictionary
UK = {'capital': 'londres', 'idioma':['ingles', 'gales', 'escoses']}
France = {'capital': 'paris', 'idioma': ['frances', 'breton', 'gascon']}
Spain = {'capital': 'madrid', 'idioma': ['catellano', 'catalan', 'aragones']}

# dictionary inside a dictionary
countries = {
    UK = {
        'capital': 'londres',
        'idioms':['ingles','gales', 'escoses'],
        'monarcha': 'isabel II',
        },
    France = {
        'capital': 'paris',
        'idioma': ['frances', 'breton', 'gascon'],
        'monarcha': 'depuso'
        },
    Spain = {
        'capital': 'madrid',
        'idioma': ['catellano', 'catalan', 'aragones'],
        'monarcha': 'felipe vi'
        },
}

for country, facts in countries.items():
    print("\nCountry: " + country.title)
    
