# CSCI 381
# Summer 2022
# Homework Chapter 6 - 6.9
# Gabriel Rubio Alvarado

"""Exercise 6.9
(Dictionary Manipulations) Using the following dictionary, which maps country
names to abbreviations:
tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
Write a script that shows the user a list of dictionary manipulation options to choose
from. Based on the choice, the corresponding manipulation is performed, and the result
is shown on the screen. The following choices can be made by the user:
a) Show the abbreviation of a country chosen by the user.
b) Display all key-value pairs in a two-column format.
c) Add a new key-value pair to the dictionary or change the value of an existing
key-value pair.
d) Create a new dictionary with the values of the first dictionary as keys and the
keys of the first dictionary as values.
e) Convert all the abbreviations in the dictionary to uppercase letters"""

tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}


def display_menu():
    print(f'Enter your selection.', "\n",
          '1: Show the abbreviation of a country.', "\n",
          '2: Display all key-value pairs.', "\n",
          '3: Add a new key-value pair to the dictionary or change existing key-value pair.', "\n",
          '4: Create a new dictionary and flip values and keys.', "\n",
          '5: Convert all the abbreviations in the dictionary to uppercase.')
    answer = input(f'Selection: ')
    return answer


def menu(choice):
    if choice == "1":
        selection = input("Select your country: " + "\n" + str(list(tlds.keys())) + "\n")
        if selection in tlds:
            print(str(tlds[selection]).upper())
    elif choice == "2":
        for key in tlds:
            print(key, ':', tlds[key])
    elif choice == "3":
        print(f' 1: Add new key-value pair to the dictionary.', "\n", '2: Change existing key-value pair.')
        selection = input(f'Selection: ')
        if selection == '1':
            country = input(f'Enter the country name: ')
            country_abb = input(f'Enter the country abbreviation: ')
            tlds.update({country: country_abb})
            for key in tlds:
                print(key, ':', tlds[key])

        if selection == '2':
            print(f'Current Dictionary: ')
            for key in tlds:
                print(key, ':', tlds[key])
            print(f' 1: Update Country Name: ', "\n", '2: Update Country Abbreviation')
            selection = input(f'Selection: ')
            if selection == '1':
                country = input(f'Enter Country to update: ')
                if country in tlds:
                    new_country = input(f'Enter new country name: ')
                    tlds[new_country] = tlds.pop(country)
                    for key in tlds:
                        print(key, ':', tlds[key])
            elif selection == '2':
                country_abbr = input(f'Enter Abbreviation to update: ')
                if country_abbr in tlds.values():
                    new_country_abb = input(f'Enter new Abbreviation: ')
                    country_ley = tlds[]
                    tlds[country_abbr] =
                    for key in tlds:
                        print(key, ':', tlds[key])


menu(display_menu())
