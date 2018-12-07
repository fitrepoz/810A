''' Author: Sadie Stokes '''
''' HW: Assignment 3 '''
''' Description: Fractions Calculator Part 2'''

import unittest

## greatest common divisor method that finds the gcd between the two numbers ##
## this function is to be used later on in the fraction class ##
def gcd(n, d):
    while n != d:
        if n > d:
            n = n - d
        else:
            d = d - n
    return n

class Fraction:
    def __init__(self, n, d):
        self.num = int(n / gcd(abs(n), abs(d)))
        self.denom = int(d / gcd(abs(n), abs(d)))
        if self.denom < 0:
            self.denom = abs(self.denom)
            self.num = -1*self.num
        elif self.denom == 0:
            # raise error if the denominator is 0 #
            raise ZeroDivisionError 

    def __add__(self, other):
        num = (self.num * other.denom) + (self.denom * other.num) 
        denom = self.denom * other.denom
        return Fraction(num, denom)

    def __sub__(self, other):
        return self.num*other.denom - self.denom*other.num, self.denom*other.denom

    def __mul__(self, other):
        return self.num*other.num, self.denom*other.denom

    def __truediv__(self, other):
        return self.num*other.denom, self.denom*other.num

    def __eq__(self, other):
        return (self.num * other.denom) == (self.denom * other.num)

    def __ne__(self, other):
        return (self.num * other.denom) != (self.denom * other.num)
    
    def __lt__(self, other):
        return(self.num * other.denom) < (self.denom * other.num)
    
    def __le__(self, other):
        return not (self.num * other.denom) <= (self.denom * other.num)
    
    def __gt__(self, other):
        return(self.num * other.denom) > (self.denom * other.num)
    
    def __ge__(self, other):
        return not (self.num * other.denom) >= (self.denom * other.num)

    def __str__(self):
        return str(self.num) + '/' + str(self.denom)  

class Test(unittest.TestCase):
    
    def test_add(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 + f1) == Fraction(6, 4))
        self.assertTrue((f1 + f2) == Fraction(5, 4))
        self.assertTrue((f1 + f3) == Fraction(13, 12))

    def test_sub(self):
        f1 = Fraction(1,2)
        f2 = Fraction(3, 4)
        f3 = Fraction(4, 5)
        f12 = Fraction(1, 2)
        self.assertTrue(1/4, f2 - f12)

    def test_mul(self):
        f1 = Fraction(1,2)
        f2 = Fraction(3, 4)
        f3 = Fraction(4, 5)
        self.assertTrue(2/5, f3 * Fraction(1,2))
    
    def test_truediv(self):
        f1 = Fraction(1,3)
        f2 = Fraction(9,12)
        f3 = Fraction(4, 5)
        self.assertEqual((9, 4), f2 / f1)

    def test_ne(self):
        f1 = Fraction(1,2)
        f2 = Fraction(3, 4)
        f3 = Fraction(9, 12)
        self.assertTrue(f3 != Fraction(1,2))
        self.assertFalse(f2 != Fraction(3,4))

    def test_gt(self):
        f1 = Fraction(1,2)
        f2 = Fraction(3, 4)
        f3 = Fraction(9, 12)
        self.assertTrue(f3 > Fraction(1,2))

    def test_ge(self):
        f1 = Fraction(1,2)
        f2 = Fraction(3, 4)
        f3 = Fraction(9, 12)
        self.assertTrue(f1 >= Fraction(3,4))
        self.assertFalse(f2 >= Fraction(3,4))

    def test_lt(self):
        f1 = Fraction(1,2)
        f2 = Fraction(3, 4)
        f3 = Fraction(9, 12)
        f4 = Fraction(1, 4)
        self.assertTrue(f4 < Fraction(1,2))

    def test_le(self):
        f1 = Fraction(1,2)
        f2 = Fraction(3, 4)
        f3 = Fraction(9, 12)
        f4 = Fraction(1, 4)
        self.assertTrue(f4 <= Fraction(1,8))

    def test_eq(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 12)
        self.assertTrue(f1 == f1)
        self.assertTrue(f1 == f2)
        self.assertTrue(f1 == f3)
        self.assertTrue(f2 == f3)
        self.assertFalse(f1 == Fraction(3, 5))

    def test_str(self):
        f = Fraction(4, 9)
        self.assertEqual(str(f), '4/9')

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
