# CSCI 381
# Summer 2022
# Homework Chapter 6 - 6.8
# Gabriel Rubio Alvarado

"""Exercise 6.8
(Challenge: Writing the Word Equivalent of a Check Amount) In check-writing
systems, it’s crucial to prevent alteration of check amounts. One common security method
requires that the amount be written in numbers and spelled out in words as well. Even if
someone can alter the numerical amount of the check, it’s tough to change the amount in
words. Create a dictionary that maps numbers to their corresponding word equivalents.
Write a script that inputs a numeric check amount that’s less than 1000 and uses the
dictionary to write the word equivalent of the amount.
For example, the amount 112.43 should be written as
ONE HUNDRED TWELVE AND 43/100"""

num2words = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
             19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
             50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
             90: 'Ninety', 100: 'Hundred'}


def check_number(number):
    # checking if number is a decimal to then split dollars and cents
    if '.' in number:
        amount = number.split('.')
        dollars = int(amount[0])
        cents = int(amount[1])
        if dollars < 100:
            key = num2words.keys()
            if dollars in key and (dollars <= 20):
                combined_numbers = str(num2words[dollars]).upper() + " AND " + str(cents) + "/100"
                print(combined_numbers)
            elif dollars < 100:
                digit_number = dollars % 10
                tens_number = dollars - digit_number
                combined_numbers = str(num2words[tens_number]).upper() + " " \
                                   + str(num2words[digit_number]).upper() \
                                   + " AND " + str(cents) + "/100"
                print(combined_numbers)
        else:
            print("Invalid amount")
    # if number is not a decimal, check that it is under 100
    elif int(number) < 100:
        amount = int(number)
        key = num2words.keys()
        if amount in key and (amount <= 20):
            combined_numbers = str(num2words[amount]).upper()
            print(combined_numbers)
        else:
            digit_number = amount % 10
            tens_number = amount - digit_number
            combined_numbers = str(num2words[tens_number]).upper() + " " \
                               + str(num2words[digit_number]).upper()
            print(combined_numbers)
    else:
        print("Invalid amount")


num = input("Enter your dollar amount: ")
check_number(num)
