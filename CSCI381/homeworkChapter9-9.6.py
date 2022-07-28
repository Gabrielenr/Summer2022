# CSCI 381
# Summer 2022
# Homework Chapter 9 - 9.6
# Gabriel Rubio Alvarado

"""Exercise 9.6
(Class Average: Writing a Gradebook Dictionary to a JSON File) Reimplement
Exercise 9.3 using the json module to write the student information to the file in JSON
format. For this exercise, create a dictionary of student data in the following format:
gradebook_dict = {'students': [student1dictionary, student2dictionary, ...]}"""

import json

stu_dic_1 = {"first_name": "Gabriel", "last_name": "Rubio", "exam_1": 90, "exam_2": 93, "exam_3": 99};
stu_dic_2 = {"first_name": "Elon", "last_name": "Musk", "exam_1": 98, "exam_2": 99, "exam_3": 50};


class ClassAverage:
    def __init__(self):
        self.grade_dict = {"students": []}

    def addStudentDict(self, studentDictionary):
        self.grade_dict["students"].append(studentDictionary)

    def writeToJSON(self):
        with open("grades.json", "w") as output:
            json.dump(self.grade_dict, output)


avg = ClassAverage()
avg.addStudentDict(stu_dic_1)
avg.addStudentDict(stu_dic_2)
avg.writeToJSON()
