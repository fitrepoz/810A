''' Author: Sadie Stokes '''
''' HW: Assignment 7 '''
''' Description: Python Containers '''

import unittest
from collections import defaultdict
from collections import Counter 

# Part 1: Anagrams ##
## p1.1 ##
def anagrams(str1, str2):
    list1 = list(str1) #set str1 to a list
    list1.sort() 
    list2 = list(str2)
    list2.sort()
    return (list1 == list2)

## p1.2 ##
def anagrams_dd(str1, str2):
    dd = defaultdict(int) #create defaultdict of integers
    for char in str1: #go through each character in in string 1
        dd[char] += 1 #increment value by 1
    for char in str2: #go through each character in in string 2
        dd[char] -= 1 #decrement by 1
        if dd[char] < 0: #check that dd is 0
            return False
    return True
    
## p1.3 ##
def anagram_counter(input1, input2): 
    return Counter(input1) == Counter(input2) 

## Part 2 ##
def covers_alphabet(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    formatted_string = set(sentence.lower()) #format to all lowercase
    return formatted_string.issuperset(alphabet) 

## Part 3 ##
def book_index(words):
    d = defaultdict(list) 
    for word, page in words: #go through each word in the dictionary
        d[word].append(page) #append the page number to each word
    print(d)
    return d

class AnagramsTest(unittest.TestCase):
    def test_anagrams_list(self):
        input1 = 'cinema'
        input2 = 'iceman'
        self.assertEqual(anagrams(input1, input2), True)
    
    def test_anagrams_counter(self):
        input1 = 'cinema'
        input2 = 'iceman'
        self.assertEqual(anagram_counter(input1, input2),True)
    
    def test_anagrams_defaultdict(self):
        input1 = 'rat'
        input2 = 'tar'
        self.assertTrue(anagrams_dd(input1,input2))

    def test_covers_alphabet(self):
        sentence1 = 'We promptly judged antique ivory buckles for the next prize'
        sentence2 = 'werwer'
        sentence3 = 'aabbcdefghijklmnopqrstuvwxyzzabc'
        self.assertTrue(covers_alphabet(sentence1))
        self.assertTrue(covers_alphabet(sentence2))
        self.assertTrue(covers_alphabet(sentence3))

if __name__ == '__main__':
    unittest.main()
