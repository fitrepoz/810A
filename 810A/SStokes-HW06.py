''' Author: Sadie Stokes '''
''' HW: Assignment 6 '''
''' Description: Four Part HW '''

import unittest

def remove_vowels(str):
    vowels = ['a','e','i','o','u'] # define vowels #
    result = ""
    for i in range(len(str)): # for each character in the string #
        if str[i] not in vowels: # if it doesn't exist in the vowels list #
            result += str[i] # add to result #

    return result

def check_pwd(pwd):
    # if the password has an uppcase, lowecase an digit its good #
    return any(x.isupper() for x in pwd) and any(x.islower() for x in pwd) and pwd[-1].isdigit()

def insertion_sort(l):
    sorted_list = list() # define empty list #

    # iterate through each item  #
    for value in l:
        if(len(sorted_list) == 0): # if not 0 append to list #
            sorted_list.append(value)
        else:
            i = 0
            added = False
            for value2 in sorted_list:
                if(value < value2):
                    sorted_list.insert(i, value)
                    added = True
                    break
                i += 1
            if not added:
                sorted_list.append(value)
    return sorted_list


class BTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    # insert value as a new terminal node in the appropriate spot in self if value is not already in the BTree. #
    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data != self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = BTree(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = BTree(data)
                    else:
                        self.right.insert(data)
        else:
            self.data = data

    # Traverse all of the nodes in BTree from smallest to largest and return a list of values from each node. #
    def traverse(self):
        if self.left:
            self.left.traverse()

        print(self.data)
        if self.right:
            self.right.traverse()


class VowelRemoverTest(unittest.TestCase):
    def test_remove_vowels(self):
        expect = 'hll wrld'
        result = remove_vowels('hello world')
        self.assertEqual(result, expect)

    def test_check_pwd(self):
        # First test check for check_pwd
        expect = False
        result = check_pwd("sdfali4")
        self.assertEqual(result, expect)

        # second test check for check_pwd
        expect = False
        result = check_pwd("Ali4ds")
        self.assertEqual(result, expect)

        # third test chech for check_pwd
        expect = True
        result = check_pwd("Fdali4")
        self.assertEqual(result, expect)

    def test_insertion_sort(self):
        expect = [1, 3, 3, 5]
        result = insertion_sort([1, 5, 3, 3])
        self.assertEqual(result, expect)

    def test_BTree(self):
        bt = BTree(27)
        bt.insert(1)
        bt.insert(15)
        bt.insert(5)
        print("\n\n\n Results of binary tree:  ")
        bt.traverse()

if __name__ == '__main__':
    unittest.main()