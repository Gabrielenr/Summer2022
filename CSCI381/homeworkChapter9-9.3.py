# CSCI 381
# Summer 2022
# Homework Chapter 9 - 9.3
# Gabriel Rubio Alvarado

"""Exercise 9.3
(Class Average: Writing Student Records to a CSV File) An instructor teaches a
class in which each student takes three exams. The instructor would like to store this information
in a file named grades.csv for later use. Write code that enables an instructor
to enter each student’s first name and last name as strings and the student’s three exam
grades as integers. Use the csv module to write each record into the grades.csv file. Each
record should be a single line of text in the following CSV format:
firstname,lastname,exam1grade,exam2grade,exam3grade"""

import csv


def main():
    number_of_stu = int(input("Enter the number of students: "))

    rows = [["First Name", "Last Name", "Ex_am 1 Grade", "Ex_am 2 Grade", "Ex_am 3 Grade"]]

    for i in range(number_of_stu):
        first = input("\nEnter First Name of Student " + str(i + 1) + ": ")
        last = input("Enter Last Name of Student " + str(i + 1) + ": ")
        ex1 = int(input("Enter Exam 1 Grade of Student " + str(i + 1) + ": "))
        ex2 = int(input("Enter Exam 2 Grade of Student " + str(i + 1) + ": "))
        ex3 = int(input("Enter Exam 3 Grade of Student " + str(i + 1) + ": "))

        rows.append([first, last, ex1, ex2, ex3])

    with open("grades.csv", 'w', newline='') as _file:
        file = csv.writer(_file)
        for i in rows:
            file.writerow(i)
    print("\nCompleted writing to file grades.csv.\n")

    with open("grades.csv", 'r') as _file:
        file = csv.reader(_file)
        header = next(file)
        for i in file:
            i[2] = int(i[2])
            i[3] = int(i[3])
            i[4] = int(i[4])
            print(i)


main()
