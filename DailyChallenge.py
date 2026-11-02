#Instructions:
#1. Ask for User Input:
#The string must be exactly 10 characters long.

#2. Check the Length of the String:
#If the string is less than 10 characters, print: "String not long enough."
#If the string is more than 10 characters, print: "String too long."
#If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.

#3. Print the First and Last Characters:
#Once the string is validated, print the first and last characters.

#4. Build the String Character by Character:
#Using a for loop, construct and print the string character by character. Start with the first character, then the first two characters, and so on, until the entire string is printed.

user_string = input('Enter a string with exactly 10 characters: ')
if len(user_string) < 10:
    print('String not long enough')

elif len(user_string) > 10:
    print('String too long')

else:
    print('Perfect string')

print('First character:', user_string[0]) 
print('Last character:', user_string[-1])

progress = ""

for character in user_string:
    progress += character
    print(progress)

import random

characters = list(user_string)
random.shuffle(characters)
jumbled_string = "" .join(characters)
print("Jumbled string", jumbled_string)