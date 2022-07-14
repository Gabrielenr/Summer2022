# CSCI 381
# Summer 2022
# Homework Chapter 5 - 5.9
# Gabriel Rubio Alvarado

"""Exercise 5.9
(Palindrome Tester) A string that’s spelled identically backward and forward, like
'radar', is a palindrome. Write a function is_palindrome that takes a string and returns
True if it’s a palindrome and False otherwise. Use a stack (simulated with a list as we did
in Section 5.11) to help determine whether a string is a palindrome. Your function should
ignore case sensitivity (that is, 'a' and 'A' are the same), spaces and punctuation. """


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


def is_palindrome(string):
    # instantiate Stack class
    stack = Stack()

    # push characters of string to the stack
    string_input = string
    for char in string_input:
        stack.push(char)

    reversed_text = ''
    # construct reversed string by popping from the stack
    while not stack.is_empty():
        reversed_text += stack.pop()

    if string_input == reversed_text:
        return True
    else:
        return False


print(is_palindrome(input('Please enter the string: ').lower().replace(" ", "")))
