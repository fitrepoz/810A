''' Author: Sadie Stokes '''
''' HW: Assignment 9 '''
''' Description: File Upload '''

from collections import defaultdict
from prettytable import PrettyTable

def file_reader(filepath, fields, sep=',', header=False):
    try:
        line_number = 0
        file = open(filepath, encoding="utf8")
        if header:
            file.readline()
            line_number += 1
        while(True):
            line = file.readline().strip()
            if line == "":
                break
            line_number += 1
            values = line.split(sep)
            if len(values) != fields:
                raise ValueError(filepath + " has " + str(len(values)) + " fields on line " + str(line_number) + " but expected " + str(fields))
            else:
                yield values
    except Exception as e:
        print (e)

class Student:
    def __init__(self):
        self.name = ""
        self.cwid = 0
        self.major = ""
        self.courses = defaultdict(str)

    def setDetails(self, name,cwid,major):
        self.name = name
        self.cwid = cwid
        self.major = major

class Instructor:
    def __init__(self):
        self.name = ""
        self.cwid = 0
        self.deparment = ""
        self.courses = defaultdict(int)

    def setDetails(self, name,cwid,deparment):
        self.name = name
        self.cwid = cwid
        self.deparment = deparment


class Repository:
    def __init__(self):
        self.students = list()
        self.instuctors = list()

    def print(self, type):
        table = PrettyTable()
        if type == "student":
            print("Student Summary")
            table.field_names = ["CWID", "name", "Completed Courses"]
            for student in self.students:
                table.add_row([student.cwid,student.name,sorted(student.courses)])
        else:
            print("Instructor Summary")
            table.field_names = ["CWID", "name", "Dept", "Courses", "Students"]
            for instructor in self.instuctors:
                count = 0
                for val in instructor.courses:
                    count += instructor.courses[val]
                table.add_row([instructor.cwid, instructor.name, instructor.deparment, sorted(instructor.courses), count])

        print(table)


def main():
    rep = Repository()
    students_files_name = "student.txt"
    instructor_files_name = "insturctor.txt"
    grades_file = "grades.txt"

    for cwid,name,major in file_reader(students_files_name,3,"\t"):
        student = Student()
        student.setDetails(name,cwid,major)
        rep.students.append(student)

    for cwid,name,major in file_reader(instructor_files_name,3,"\t"):
        instuctor = Instructor()
        instuctor.setDetails(name,cwid,major)
        rep.instuctors.append(instuctor)

    for studentCWID,course,grade,instructorCWID in file_reader(grades_file,4,"\t"):
        for s in rep.students:
            if s.cwid == studentCWID:
                s.courses[course] = grade

        for i in rep.instuctors:
            if i.cwid == instructorCWID:
                i.courses[course] += 1

    rep.print("student")
    rep.print("instructor")

if __name__ == '__main__':
    main()