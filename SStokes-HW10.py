''' Author: Sadie Stokes '''
''' HW: Assignment 10 '''
''' Description: File Upload '''

import os
from prettytable import PrettyTable
from collections import defaultdict

# reuse from hw09 #
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

class Repository:
    
    def __init__(self, directory, prettytable = False):
        # change to dict #
        self.students = dict() 
        self.instructors = dict() 
        self.majors = dict() 

        try:
            os.chdir(directory)
        except FileNotFoundError:
            raise NotADirectoryError("Not a valid directory. Please try again.".format(directory))
        else:

            # get files #
            student_path = os.path.join(directory, "students.txt")
            instructor_path = os.path.join(directory, "instructors.txt")
            grades_path = os.path.join(directory, "grades.txt")
            majors_path = os.path.join(directory, "majors.txt")

            # open files #
            self.major_table(majors_path, '\t')
            self.student_table(student_path, '\t')
            self.instructor_table(instructor_path, '\t')
            self.grade_table(grades_path, '\t')

        if prettytable == True:
            print('Majors Summary')
            self.print_major_table()
            print('\nStudents Summary')
            self.print_student_table()
            print('\nInstructors Summary')
            self.print_instructor_table()
                    
    # student table #
    def student_table(self, file, split_type):
        expected_tokens = 3
        for cwid, name, department in file_reader(file, expected_tokens,  '\t'):
            if department in self.majors: 
                self.students[cwid] = Student(cwid, name, department)
                self.students[cwid].add_major(self.majors[department])    
            else:
                raise ValueError("The major {} is not offered at Stevens.".format(department))  

    # instructor table #
    def instructor_table(self, file, split_type):
        expected_tokens = 3
        for cwid, name, department in file_reader(file, expected_tokens, '\t'):
            self.instructors[cwid] = Instructor(cwid, name, department)

    # grade table #
    def grade_table(self, file, split_type):
        expected_tokens = 4
        for cwid, course, grade, teacher in file_reader(file, expected_tokens, '\t'):
            if cwid in self.students:                   
                self.students[cwid].add_course(course, grade)
            else:
                raise ValueError("Student with CWID: {} is not a student".format(cwid))
            if teacher in self.instructors:            
                self.instructors[teacher].add_course(course)
            else:
                raise ValueError("Instructor with CWID: {} is not an instructor".format(teacher))

    # major table #
    def major_table(self, file, split_type):
        expected_tokens = 3
        for major, flag, course_code in file_reader(file, expected_tokens, '\t'):
            if major not in self.majors:
                self.majors[major] = Major(major)
            self.majors[major].add_course(course_code, flag)    
    
    def print_student_table(self):
        pt = PrettyTable(field_names = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives'])
        for cwid in self.students:                    
            pt.add_row(self.students[cwid].pretty_table_info())
        print(pt)

    def print_instructor_table(self):
        pt = PrettyTable(field_names = ['CWID', 'Name', 'Department', 'Course', 'Students'])
        for cwid in self.instructors:                     
            for course in self.instructors[cwid].pretty_table_info():
                pt.add_row(course)
        print(pt)

    def print_major_table(self):
        pt = PrettyTable(field_names = ['Dept.', 'Required', 'Electives'])
        for department in self.majors:                     
            pt.add_row(self.majors[department].pretty_table_info())
        print(pt)


class Major:
    
    def __init__(self, department):
        self.department = department
        self.required_courses = set()   
        self.elective_courses = set()   

    def add_course(self, course_code, flag):
        if flag.upper() == 'R':
            self.required_courses.add(course_code)
        elif flag.upper() == 'E':
            self.elective_courses.add(course_code)
        else:
            raise ValueError("The course {} is not an elective or college credit".format(course_code))
    
    def pretty_table_info(self):
        return [self.department, sorted(self.required_courses), sorted(self.elective_courses)]
        

class Student:
    
    def __init__(self, cwid, name, major):
        self.cwid = cwid    
        self.name = name
        self.major = major 
        self.taken_courses = defaultdict(str) 
        self.completed_courses = set()  
        self.remaining_required = set()   
        self.remaining_elective = set()   

    def add_course(self, course_code, grade):
        self.taken_courses[course_code] = grade
        if grade in ['A+','A','A-','B+','B','B-','C+','C']:
            self.completed_courses.add(course_code)    
            self.remaining_required = self.remaining_required.difference(self.completed_courses)
            if len(self.remaining_elective.intersection(self.completed_courses)) > 0:
                self.remaining_elective = {None}
    
    def add_major(self, major):
 
        self.remaining_required = major.required_courses
        self.remaining_elective = major.elective_courses
        
    def pretty_table_info(self):
        return [self.cwid, self.name, self.major, sorted(self.completed_courses), self.remaining_required, self.remaining_elective]


class Instructor:
    
    def __init__(self, cwid, name, department):
        self.cwid = cwid    
        self.name = name
        self.department = department
        self.courses = defaultdict(int) 

    def add_course(self, course):
        self.courses[course] += 1

    def pretty_table_info(self):
        for course, num_stud in self.courses.items():
            yield [self.cwid, self.name, self.department, course, num_stud]


def main():
    directory = r'\Users\sasto\Desktop\810A'
    rep = Repository(directory, prettytable = True)

if __name__ == '__main__':
    main()
    