#Exercise 1: Converting Lists into Dictionaries
#Instructions: You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

# keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)

#Exercise 2: Cinemax #2
#Instructions:

#Write a program that calculates the total cost of movie tickets for a family based on their ages.
#Family members’ ages are stored in a dictionary.
#The ticket pricing rules are as follows:
#Under 3 years old: Free
#3 to 12 years old: $10
#Over 12 years old: $15
#Family Data:
#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#Loop through the family dictionary to calculate the total cost.
#Print the ticket price for each family member.
#Print the total cost at the end.
#Bonus: Allow the user to input family members’ names and ages, then calculate the total ticket cost.

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    total += price
    print(name, price)
print('Total:', total)
#Bonus: Allow the user to input family members’ names and ages, then calculate the total ticket cost.

family = {}
family_size = int(input('How many family members?: '))

for i in range(family_size):
    name = input("What is the family member's name? ")
    age = int(input("What is your age? "))
    family[name] = age

print(family)

total = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    total += price
    print(name, price)
print('Total:', total)

#Exercise 3: Zara
#Instructions:

#Create and manipulate a dictionary that contains information about the Zara brand.
#Brand Information:

#name: Zara
#creation_date: 1975
#creator_name: Amancio Ortega Gaona
#type_of_clothes: men, women, children, home
#international_competitors: Gap, H&M, Benetton
#number_stores: 7000
#major_color: 
#    France: blue, 
#    Spain: red, 
#    US: pink, green

#Create a dictionary called brand with the provided data.
#Modify and access the dictionary as follows:
#Change the value of number_stores to 2.
#Print a sentence describing Zara’s clients using the type_of_clothes key.
#Add a new key country_creation with the value Spain.
#Check if international_competitors exists and, if so, add “Desigual” to the list.
#Delete the creation_date key.
#Print the last item in international_competitors.
#Print the major colors in the US.
#Print the number of keys in the dictionary.
#Print all keys of the dictionary.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Alterar a quantidade de lojas
brand["number_stores"] = 2
print(brand["number_stores"])

# Descrever os clientes e produtos
print("Zara offers clothes and products for:", brand["type_of_clothes"])

# Adicionar o país de criação
brand["country_creation"] = "Spain"

# Adicionar um concorrente, se a chave existir
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Remover a data de criação
brand.pop("creation_date")

# Mostrar o último concorrente
print(brand["international_competitors"][-1])

# Mostrar as cores nos EUA
print(brand["major_color"]["US"])

# Mostrar a quantidade de chaves
print(len(brand))

# Mostrar todas as chaves
print(brand.keys())

#Bonus
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 7000
}

brand.update(more_on_zara)

print(brand)

#Exercise 4: Disney Characters
#Instructions
#You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
#Character List:
#users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#Expected Results:
#1. Create a dictionary that maps characters to their indices:
#{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#2. Create a dictionary that maps indices to characters:
#{0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
#{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

characters = {}

for index, name in enumerate(users):
    characters[name] = index
print(characters)

characters_by_index = {}

for index, name in enumerate(users):
    characters_by_index[index] = name

print(characters_by_index)

characters_sorted = {}

for index, name in enumerate(sorted(users)):
    characters_sorted[name] = index

print(characters_sorted)