#Exercise 1: Favorite Numbers
#Instructions:
#Create a set called my_fav_numbers and populate it with your favorite numbers.
#Add two new numbers to the set.
#Remove the last number you added to the set.
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.

favorite_numbers = {3, 6, 9}
favorite_numbers.add(13)
favorite_numbers.add(69)

print(favorite_numbers)
# Sets have no order

favorite_numbers.remove(69)
print(favorite_numbers)
#Removed last number

friend_fav_numbers = {10, 11, 12}

our_fav_numbers = favorite_numbers .union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 2: Tuple
#Instructions: Given a tuple of integers, try to add more integers to the tuple.

my_numbers = (10, 20, 30)
my_numbers = my_numbers + ( 40, 50)
print(my_numbers)

#Exercise 3
#instructions: You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
#Remove "Blueberries" from the list.
#Add "Kiwi" to the end of the list.
#Add "Apples" to the beginning of the list.
#Count how many times "Apples" appear in the list.
#Empty the list.
#Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
basket.clear()
print(basket)

#Exercise 4: Floats
#Instructions:
#Create a list containing the following sequence of mixed types: floats and integers:
#1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
#Avoid hard-coding each number manually.

mix_types = []
current_number = 1.5

while current_number <= 5:
    mix_types.append(current_number)
    current_number += 0.5
print(mix_types)

#Exercise 5: For Loop
#Instructions:
#Write a for loop to print all numbers from 1 to 20, inclusive.
#Write another for loop that prints every number from 1 to 20 where the index is even.

for number in range(1, 21):
    print(number)

for index, number in enumerate(range(1, 21)):
    if index % 2 == 0:
        print(number)

#Exercise 6: While Loop
#Instructions:
#Use an input to ask the user to enter their name.
#Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
#if the input is incorrect, keep asking for the correct input until it is correct
#if the input is correct print “thank you” and break the loop

while True:
    name = input(('Enter your name: '))

    if not name.isalpha() or len(name) <3:
        print("Invalid name")
    else:
        print('Thank you')
        break

#Exercise 7: Favorite Fruits
#Instructions:
#Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
#Store these fruits in a list.
#Ask the user to input the name of any fruit.
#If the fruit is in their list of favorite fruits, print:
#"You chose one of your favorite fruits! Enjoy!"
#If not, print:
#"You chose a new fruit. I hope you enjoy it!"

favorite_fruits = input("Enter your favorite fruits: ").lower().split()

chosen_fruit = input("Choose a fruit: ").lower()

if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#Exercise 8: Pizza Toppings
#Instructions:
#Write a loop that asks the user to enter pizza toppings one by one.
#Stop the loop when the user types 'quit'.
#For each topping entered, print:
#"Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.

toppings = []

while True:
    topping = input("Enter a pizza topping: ")

    if topping == "quit":
        break

    toppings.append(topping)
    print(f"{topping} has been added to your pizza!")

total_price = 10 + (len(toppings) * 2.50)

print(f"Your total price is ${total_price:.2f}")

#Exercise 9
#Instructions:
#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
#Free for people under 3.
#$10 for people aged 3 to 12.
#$15 for anyone over 12.
#Print the total ticket cost.

family_ages = []

while True:
    answer = input("Enter an age or quit: ")

    if answer == "quit":
        break

    family_ages.append(int(answer))

total_price = 0

for age in family_ages:
    if age < 3:
        total_price += 0
    elif age <= 12:
        total_price += 10
    else:
        total_price += 15

print(f"Total ticket price: ${total_price}")

#Bonus
#Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
#Write a program to:
#Ask for each person’s age.
#Remove anyone who isn’t allowed to watch.
#Print the final list of attendees.

attendees = []

while True:
    answer = input("Enter your age or type quit: ")

    if answer == "quit":
        break

    attendees.append(int(answer))

for age in attendees.copy():
    if age < 16 or age > 21:
        attendees.remove(age)

print("Final attendees:", attendees)
