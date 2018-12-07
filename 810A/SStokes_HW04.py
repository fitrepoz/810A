''' Author: Sadie Stokes '''
''' HW: Assignment 4 '''
''' Description: Vowel Counter '''

import unittest

# vowel list #
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U']

print("Hello! Welcome to vowel counter!")
def count_vowels(str):
    count = 0
    for letter in str.lower(): #loop to go through each letter in user input#
        if letter in vowels: #if letter is a vowel add 1 to 'count'
            count += 1
    print(count) #print out number of vowels#
    return count


sentence = input("Please enter a random phrase: ")
count_vowels(sentence)

def item_search(item,sampleList):
    for offset, x in enumerate(sampleList):
        if x == item:
            print(offset)
            return offset
    return None   

def custom_gcd(num, denom): 
    while num != denom:
        if num > denom:
            num = num - denom
        else:
            denom = denom - num
    return num

#custom gcd functions $
def simplify(n, d):
    # get the abs of num and denom
    num = int(n / custom_gcd(abs(n), abs(d)))
    denom = int(d / custom_gcd(abs(n), abs(d)))
    if denom < 0:
        denom = abs(denom)
        num = -1*num
    elif denom == 0: #check if denom is 0
            # raise error if the denominator is 0 #
        raise ZeroDivisionError
    print(num ,"/",denom)
    return num, denom
        
## my custom enumerate function ##
def my_enumerate(seq):
    for item in seq: #loop through each item in the word
        print(seq.index(item)+0,item)

## test enumeration function ##
def test_enumerate(seq):
    for offset, value in enumerate(seq):
        print(offset, value)


## unit test ##
class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self):
        print("Part 1 Tests:")
        self.assertEqual(count_vowels("Sadie Sample Test"), 6)
        self.assertEqual(count_vowels("hello world"), 3)
        self.assertEqual(count_vowels('hEllO wrld'), 2)
        self.assertEqual(count_vowels('hll wrld'), 0)

    def test_item_search(self):
        foods = ['jello', 'turkey', 'cranberry', 'ham', 'mac', 'stuffing']
        nums = [ 42, 33, 21, 33 ]
        print("Part 2 Tests:")
        self.assertEqual(item_search('turkey', foods), 1)
        self.assertEqual(item_search('p', 'apple'), 1)
        self.assertEqual(item_search(33, nums), 1)
    
    def test_reduce_fraction(self):
        print('Part 3 Tests:')
        self.assertEqual(simplify(9,27), (1, 3))
        self.assertEqual(simplify(2,4), (1, 2))

    def test_enumerate_sequence(self):
        print('Part 4 Tests:')
        self.assertEqual(my_enumerate('Sadie'), test_enumerate('Sadie'))
    

if __name__ == "__main__":    
    unittest.main(exit=False, verbosity=2)
