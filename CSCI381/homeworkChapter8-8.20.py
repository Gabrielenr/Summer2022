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

string_format1 = re.search("[0-9][0-9][0-9][0-9][0-9][0-9]", txt)  # finding 6 digits from text
if string_format1:  # if date in format 1 is found
    string_format1 = string_format1.group()  # grouping the searched format
    f1 = re.findall("[0-9][0-9]", string_format1)  # making list of all 2 digit numbers
    f1month = f1[0]  # first item of list is month
    f1date = f1[1]  # second item of list is date
    f1year = "20" + f1[2]  # third item of list is year
    format2 = f1month + "/" + f1date + "/" + f1year  # munging into format 2
    format3 = months[int(f1month) - 1] + " " + f1date + ", " + f1year  # munging into format 3
    print(string_format1)  # printing in format 1
    print(format2)  # printing in format 2
    print(format3)  # printing in format 3
print()

string_format_2 = re.search("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]", txt)  # searching format 2
if string_format_2:  # if date in format 2 is found
    string_format_2 = string_format_2.group()  # grouping the searched format
    f2 = re.findall("[0-9][0-9]", string_format_2)  # making list of all 2 digit numbers
    f2month = f2[0]  # first item of list is month
    f2date = f2[1]  # second item of list is date
    f2year = f2[2] + f2[3]  # third and fourth item of list is year
    format2 = f2month + f2date + f2[3]  # munging into format 1
    format3 = months[int(f2month) - 1] + " " + f2date + ", " + f2year  # munging into format 3
    print(string_format_2)
    print(format2)
    print(format3)
print()

c = 0
for month in months:  # for all item in list months
    c = c + 1  # counting months
    string_format_3 = re.search(month + " [0-9][0-9], [0-9][0-9][0-9][0-9]", txt)  # searching format 3
    if string_format_3:  # if date in format 3 is found
        string_format_3 = string_format_3.group()  # grouping the searched format
        if c < 10:  # if counter of month is less than 10
            f3month = "0" + str(c)  # 0 is added with converted integer
        else:
            f3month = str(c)  # original counter converted to string

        f3 = re.findall("[0-9][0-9]", string_format_3)  # making list of all 2 digit numbers
        f3date = f3[0]  # first item of list is date
        f3year = f3[1] + f3[2]  # second and third item of list is year
        format1 = f3month + f3date + f3[2]  # munging into format 1
        format2 = f3month + "/" + f3date + "/" + f3year  # munging into format 2
        print(string_format_3)
        print(format1)
        print(format2)
        break
