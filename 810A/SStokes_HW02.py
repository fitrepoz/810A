''' Author: Sadie Stokes '''
''' HW: Assignment 2 '''
''' Description: Fractions Calculator '''

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
        return(self.num * other.denom) == (self.denom * other.num)

    def __str__(self):
        return str(self.num) + '/' + str(self.denom)  

def sampleTests():
    f12 = Fraction(1, 2)
    f44 = Fraction(4, 4)
    f128 = Fraction(12, 8)
    f32 = Fraction(3, 2)
    f44 = Fraction(4, 4)

    print()
    print("Here are forced test cases: ")
    print(f12, '+', f12, '=', f12.Plus(f12), '[4/4]')
    print()
    print(f12, '+', f44, '=', f12.Plus(f44), '[12/8]')
    print()
    print(f128, "==", f32, "is", f128.Equal(f32), '[True]')
    print()
    print(f44, '-', f12, '=', f44.Minus(f12), '[4/8]')

def getUserInput(prompt):
## Get first set of fraction values ##
    while True:
        inp = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print('Error:', inp, 'is not a number. Please try again...')

def runCalculator():
    ## get first set of fractions ##
    num1 = getUserInput("Please enter numerator 1: ")
    denom1 = getUserInput("Please enter denominator 1: ")
    
    ## get second set of fractions ##
    num2 = getUserInput("Please enter numerator 2: ")
    denom2 = getUserInput("Please enter denominator 2: ")

    print()
    print("Now Select an operation!")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiple (*)")
    print("4. Divide (/)")
    print()

    while True:
        choice = input("Please enter your choice of operation: ")
        try:
            val = int(choice)
            if val < 0:  # if not a positive int print message and ask for input again #
                print("Ooops! We can only accept integers, try again")
                continue
            break
        except ValueError:
            print("That's not an int!")    
    print("Thanks, got your selected operation!")
    print()
    print("Here are your created test cases...")

    f1 = Fraction(num1, denom1)
    f2 = Fraction(num2, denom2)

    if choice == '1':
        print(f1, '+', f2, f1.Plus(f2))
    elif choice == '2':
        print(f1, '-', f2, f1.Minus(f2))
    elif choice == '3':
        print(f1, '*', f2, f1.Times(f2))
    elif choice == '4':
        print(f1, '/', f2, f1.Divide(f2))

sampleTests()
runCalculator()