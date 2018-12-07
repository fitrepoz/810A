''' Author: Sadie Stokes '''
''' HW: Assignment 5 '''
''' Description: File Upload '''

import unittest

def reverse(str):
    # stores the reversed string #
    reverse = ""

    # for loop to add each element one by one from the end in reverse string #
    for i in range(len(str)):
        reverse += str[-(i+1)]

    return reverse

# custom enumation function #
def rev_enumerate(seq):
    i = len(seq) - 1
    while i >= 0:
        yield i, seq[i]
        i -= 1

def find_second(s1, s2):
    # find the index of first occurrence of s1 in s2 #
    i = s2.find(s1)
    j = -1

    # if is -1 that s2 does not contain s1 at all so -1 will be returned #
    if(i != -1):
        j = s2[i+1:].find(s1)

    # j equal to -1 means that the string s1 has not occured twice in string s2 #
    if(j == -1):
        return j
    else:
        return i + j + 1

def get_lines(path):
    file = open(path, encoding="utf8")
    lines = file.readlines();

    line_to_return = ""
    # reading each line #
    for line in lines:
        line = line.strip() # strip extra characters #

        # if line doesn't contain a \ then return otherwise just add to the line_to_return #
        if not line.__contains__("\\"):
            line_to_return += line
            if line_to_return[0] == "#":
                line_to_return = ""
                continue
            # If line contains # remove the line after the # from the line #
            elif (line_to_return.__contains__("#")):
                line_to_return = line_to_return[:line_to_return.find("#")]

            # return the current line and reset the line_to_return variable #
            yield line_to_return
            line_to_return = ""
        else:
            line_to_return += line.replace("\\","")

class GetProgram1(unittest.TestCase):
    def test_get_lines(self):
        file_name = 'input.txt' # the file to test the data #

        test = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>', '<line5>', '<line6>']
        result = list(get_lines(file_name))
        self.assertEqual(result, test)

    def test_reverse(self):
        test = "cba"
        result = reverse("abc")
        self.assertEqual(result, test)

    def test_find_second(self):
        test = 4
        result = find_second("iss","Mississippi")
        self.assertEqual(result, test)

        test = 3
        result = find_second('abba', 'abbabba')
        self.assertEqual(result,test)

    def test_rev_enemurate(self):
        test = [(5, 'n'), (4, 'o'), (3, 'h'), (2, 't'), (1, 'y'), (0, 'P')]
        result = list(rev_enumerate("Python"))
        self.assertEqual(result,test)


if __name__ == '__main__':
    unittest.main()