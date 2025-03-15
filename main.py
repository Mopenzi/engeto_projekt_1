"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Černý
email: merny.cichal@seznam.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }

separator = 40 * "-"

user_name = input("username:")
user_password = input("password:")

if user_name in users and user_password == users[user_name]:
    print(separator)
    print("Welcome to the app,", user_name)
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print(separator)
    user_choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
    print(separator)
    if user_choice.isdecimal():
        user_choice = int(user_choice)
        if user_choice in range(1, len(TEXTS) + 1):
            words = TEXTS[user_choice - 1].split()
            count_of_words = len(words)
            count_of_titlecase = 0
            count_of_uppercase = 0
            count_of_lowercase = 0
            count_of_numbers = 0
            sum_of_numbers = 0
            occurences = {}

            for word in words:
                if word.isupper():
                    count_of_uppercase += 1
                if word.istitle():
                    count_of_titlecase += 1
                if word.islower():
                    count_of_lowercase += 1
                if word.isdecimal():
                    count_of_numbers += 1
                    sum_of_numbers += int(word) 

            print(f"There are {count_of_words} words in the selected text.")
            print(f"There are {count_of_titlecase} titlecase words.")
            print(f"There are {count_of_uppercase} uppercase words.")
            print(f"There are {count_of_lowercase} lowercase words.")
            print(f"There are {count_of_numbers} numeric strings.")
            print(f"The sum of all the numbers {sum_of_numbers}")
            print(separator)

        else:
            print("you entered a number out of range, terminating the program..")
        
    else:
        print("you did not input a whole number, terminating the program..")

else:
    print("unregistered user, terminating the program..")