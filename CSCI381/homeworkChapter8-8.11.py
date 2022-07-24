# CSCI 381
# Summer 2022
# Homework Chapter 8 - 8.11
# Gabriel Rubio Alvarado

"""Exercise 8.11
(Project: Evaluate Word Problems) Write a script that enables the user to enter
mathematical word problems like “two times three” and “seven minus five”, then use
string processing to break apart the string into the numbers and the operation and return
the result. So “two times three” would return 6 and “seven minus five” would return 2. To
keep things simple, assume the user enters only the words for the numbers 0 through 9
and only the operations 'plus', 'minus', 'times' and 'divided by'."""

num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}


def perform_operation(first_num, op, second_num):
    first_numb = first_num
    second_numb = second_num
    oper = op
    if first_numb and second_numb in num_dict:
        first_number_int = num_dict[first_numb]
        second_number_int = num_dict[second_numb]
        if oper == "times":
            result = int(first_number_int) * int(second_number_int)
            print(result)
        elif oper == "plus":
            result = int(first_number_int) + int(second_number_int)
            print(result)
        elif oper == "minus":
            result = int(first_number_int) - int(second_number_int)
            print(result)
        elif (oper == "divided by") or (oper == "divided") or (oper == "divide"):
            result = int(first_number_int) / int(second_number_int)
            print(result)


user_input = input("Enter operation here: ")

if len(user_input.strip().split(" ")) < 4:
    first_number, operation, second_number = user_input.split()
    perform_operation(first_number, operation, second_number)

else:
    first_number, divided, divided_by, second_number = user_input.split()
    operation = divided + ' ' + divided_by
    perform_operation(first_number, operation, second_number)
