''' Author: Sadie Stokes '''
''' HW: Assignment 2 '''
''' Description: Fractions Calculator '''

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

    def Plus(self, other):
        return self.num*other.denom + self.denom*other.num, self.denom*other.denom

    def Minus(self, other):
        return self.num*other.denom - self.denom*other.num, self.denom*other.denom

    def Times(self, other):
        return self.num*other.num, self.denom*other.denom

    def Divide(self, other):
        return self.num*other.denom, self.denom*other.num

    def Equal(self, other):
        return (self.num * other.denom) == (self.denom * other.num)

    def __str__(self):
        return str(self.num) + '/' + str(self.denom)  

## Get first set of fraction values ##

class FractionTest(unittest.TestCase): 
    def test_init(self):
        f = Fraction(3, 4)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.denom, 4)
        
    def test_str(self):
        f = Fraction(3, 4)
        self.assertEqual(str(f), '3/4')
        
    def test_equal(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 12)
        self.assertTrue(f1 == f1)
        self.assertTrue(f1 == f2)
        self.assertTrue(f1 == f3)
        self.assertTrue(f2 ==f3)
        self.assertFalse(f1 == Fraction(3, 5))

    def test_plus(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 + f1) == Fraction(6, 4))
        self.assertTrue((f1 + f2) == Fraction(5, 4))
        self.assertTrue((f1 + f3) == Fraction(13, 12))
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)


    #f1 = Fraction(num1, den1)
    #f2 = Fraction(num2, den2)
    f12 = Fraction(1, 2)
    f44 = Fraction(4, 4)
    f128 = Fraction(12, 8)
    f32 = Fraction(3, 2)

  
    print()
    print(f12, '+', f12, '=', f12.Plus(f12), '[4/4]')
    print()
    print(f12, '+', f44, '=', f12.Plus(f44), '[12/8]')
    print()
    print(f128, "==", f32, "is", f128.Equal(f32), '[True]')
