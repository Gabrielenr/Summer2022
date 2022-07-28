# CSCI 381
# Summer 2022
# Homework Chapter 8 - 8.20
# Gabriel Rubio Alvarado

"""Exercise 8.20
(Regular Expressions: Munging Dates) Dates are stored and displayed in several
common formats. Three common formats are
042555
04/25/1955
April 25, 1955
Use regular expressions to search a string containing dates, find substrings that match
these formats and munge them into the other formats. The original string should have
one date in each format, so there will be a total of six transformations.
"""

# import re
#
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
#           'August', 'September', 'October', 'November', 'December']
# date_string = ["02252022", "7/21/2021", "October 30, 2020"]

import re

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']
txt = '022522, 07/21/2021, October 30, 2020'
print(txt)

format1 = re.search("[0-9][0-9][0-9][0-9][0-9][0-9]", txt)  # finding 6 digits from text
if format1:  # if date in format 1 is found
    format1 = format1.group()  # grouping the searched format
    f1 = re.findall("[0-9][0-9]", format1)  # making list of all 2 digit numbers
    f1month = f1[0]  # first item of list is month
    f1date = f1[1]  # second item of list is date
    f1year = "20" + f1[2]  # third item of list is year
    format12 = f1month + "/" + f1date + "/" + f1year  # munging into format 2
    format13 = months[int(f1month) - 1] + " " + f1date + ", " + f1year  # munging into format 3
    print(format1)  # printing in format 1
    print(format12)  # printing in format 2
    print(format13)  # printing in format 3
print()

format2 = re.search("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]", txt)  # searching format 2
if format2:  # if date in format 2 is found
    format2 = format2.group()  # grouping the searched format
    f2 = re.findall("[0-9][0-9]", format2)  # making list of all 2 digit numbers
    f2month = f2[0]  # first item of list is month
    f2date = f2[1]  # second item of list is date
    f2year = f2[2] + f2[3]  # third and fourth item of list is year
    format21 = f2month + f2date + f2[3]  # munging into format 1
    format23 = months[int(f2month) - 1] + " " + f2date + ", " + f2year  # munging into format 3
    print(format2)
    print(format21)
    print(format23)
print()

c = 0
for month in months:  # for all item in list months
    c = c + 1  # counting months
    format3 = re.search(month + " [0-9][0-9], [0-9][0-9][0-9][0-9]", txt)  # searching format 3
    if format3:  # if date in format 3 is found
        format3 = format3.group()  # grouping the searched format
        if c < 10:  # if counter of month is less than 10
            f3month = "0" + str(c)  # 0 is added with converted integer
        else:
            f3month = str(c)  # original counter converted to string

        f3 = re.findall("[0-9][0-9]", format3)  # making list of all 2 digit numbers
        f3date = f3[0]  # first item of list is date
        f3year = f3[1] + f3[2]  # second and third item of list is year
        format31 = f3month + f3date + f3[2]  # munging into format 1
        format32 = f3month + "/" + f3date + "/" + f3year  # munging into format 2
        print(format3)
        print(format31)
        print(format32)
        break
