# CSCI 381
# Summer 2022
# Homework Chapter 2 - 2.8
# Gabriel Rubio Alvarado

"""Exercise 2.8
(Table with Number of Bacteria) Starting with 200 bacteria, the growth in the number of bacteria after n hours is
calculated as follows: B = 200 × 2^n. Print the number of bacteria after 0, 5, 10, and 15 hours in table format as
shown below. Use the tab escape sequence to achieve the two-column output.
Hour    Number of Bacteria
0       200
5       6400
10      204800
15      6553600 """

hours = [0, 5, 10, 15]
bacteria_amount = 200
i = 0

print(f'{"Hour":8}{"Number of Bacteria"}')
print('-' * 26)

while i < len(hours):
    print(f'{hours[i]:>4}{bacteria_amount * pow(2, hours[i]):>22}')
    i += 1

