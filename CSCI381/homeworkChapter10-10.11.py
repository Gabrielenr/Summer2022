# CSCI 381
# Summer 2022
# Homework Chapter 10 - 10.11
# Gabriel Rubio Alvarado

"""(Class Fraction) The Python Standard Library module fractions provides a
Fraction class that stores the numerator and denominator of a fraction, such as:
Research Fraction’s capabilities, then demonstrate:
a) Adding two Fractions.
b) Subtracting two Fractions.
c) Multiplying two Fractions.
d) Dividing two Fractions.
e) Printing Fractions in the form a/b, where a is the numerator and b is the denominator.
f) Converting Fractions to floating-point numbers with built-in function float."""


from fractions import Fraction

a = Fraction(2, 4)
b = Fraction(1, 4)
print('Adding two fractions: ', a, '+', b, '=', a + b)
print('Subtracting two fractions: ', a, '-', b, '=', a - b)
print('Multiplying two fractions: ', a, 'x', b, '=', a * b)
print('Fraction in the form a/b: ', a.numerator, '/', a.denominator)
print('Fraction converted to floating-point number', a.__float__())


