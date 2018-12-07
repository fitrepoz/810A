''' Author: Sadie Stokes '''
''' HW: Assignment 8 '''
''' Description: File Upload '''

import datetime
from datetime import date
import os
from prettytable import PrettyTable

## Part 1: Dat Arithmetic ##
date1 = "2/27/2000"
date2 = "02/27/2017"
date3 = date(2017, 1, 1)
date4 = date(2017, 10, 31)

print('What is the date three days after Feb 27, 2000?')
# set formatted date and get the day count after specified date
d = datetime.datetime.strptime(date1, '%m/%d/%Y') + datetime.timedelta(days=3)
print(d.strftime('%m/%d/%Y'))
print("")

print('What is the date three days after Feb 27, 2017?')
# set formatted date and get the day count after specified date
d = datetime.datetime.strptime(date2, '%m/%d/%Y') + datetime.timedelta(days=3)
print(d.strftime('%m/%d/%Y'))
print("")

print('How many days passed between Jan 1, 2017 and Oct 31, 2017?')
# calculate diffeence between two dates
difference = date4 - date3
print(difference.days)
print("")

## Part 2: Field separated file reader ##
def file_reader(filepath, fields, sep=',', header=False): # set parameters #
    try:
        line_number = 0 # set initial line num #
        file = open(filepath, encoding="utf8") # read/open the file #
        if header:
            file.readline() # read each line in the file #
            line_number += 1 # append to line number variable #
        while(True):
            line = file.readline().strip() # strip the characters #
            if line == "":
                break
            line_number += 1
            values = line.split(sep)
            if len(values) != fields: # raise error #
                raise ValueError(filepath + " has " + str(len(values)) + " fields on line " + str(line_number) + " but expected " + str(fields))
            else:
                yield values
    except Exception as e:
        print (e)

## Part 3: Scanning directories files ##
def scan(dir):
    try:
        print("Summary for " + dir)
        # listing the whole dir
        files = os.listdir(dir)
        x = PrettyTable() # set pretty table areas #
        x.field_names = ["File Name", "Classes", "Functions", "Lines","Characters"]

        files_count = 0
        for file in files: # loop through each file that ends with .py #
            if file.endswith(".py"):
                files_count += 1
                # set initial variables #
                functions = 0
                classes = 0
                charactors = 0
                try:
                    # open the file and read each line #
                    lines = open(file, encoding="utf8").readlines()

                    for line in lines:
                        line_contents = line.strip().split(" ") # split and strip each line #
                        # separate and add those lines to the correct area in the table #
                        if line_contents[0] == "def":
                            functions += 1
                        if line_contents[0] == "class":
                            classes += 1
                        charactors += len(line)
                    x.add_row([dir+ "\\" + file, classes, functions, len(lines),charactors])

                except Exception as e:
                    print (e)

        # displaying the table
        print (x)

    except WindowsError as e:
        print (e)

if __name__ == '__main__':
    file_name = "student.txt"
    for cwid, name, major in file_reader(file_name, 3, sep='\t'):
        print("name: {} cwid: {} major: {}".format(name, cwid, major))
    print("")
    dir_path = "C:\\Users\sasto\Desktop\Desktop\SchoolWork\810A"
    scan(dir_path)
