# CSCI 381
# Summer 2022
# Homework Chapter 5 - 5.5
# Gabriel Rubio Alvarado

""""Exercise 5.5
(List Slicing) Create a list called numbers containing "1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20," then perform slicing operations to obtain the following:
a) The third number,
b) The first five numbers,
c) The first half of the list,
d) The last five numbers,
e) Every other number,
f) The numbers in reverse order, and
g) The third last number. """

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(f'This is the third number: {number[2]}')
print(f'These are the first five numbers: {number[0:5]}')
middle_index = len(number) // 2
print(f'This is half of the numbers list: {number[:middle_index]}')
print(f'These are the last five numbers: {number[-5:]}')
print(f'Every other number from the list: {number[::2]}')
print(f'These are the numbers from the list in reverse order: {number[::-1]}')
last_third = len(number) - 3
print(f'This is the third last number: {number[last_third]}')




