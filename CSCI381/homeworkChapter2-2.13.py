# CSCI 381
# Summer 2022
# Homework Chapter 2 - 2.13
# Gabriel Rubio Alvarado

"""Exercise 2.13
(How Big Can Python Integers Be?) We’ll answer this question later in the book.
For now, use the exponentiation operator ** with large and very large exponents to produce some huge integers and assign
those to the variable number to see if Python accepts them.
Did you find any integer value that Python won’t accept? """

number = 10000 ** 10000000000

print(type(number))

# No max limit for int compiled in Python 3 or higher.
# It all depends on the memory available to compute the exponentiation.
