'''
Created on Jul 19, 2018

@author: Yan
'''
from builtins import int
print('Enter birth Year')
birthYear = int(input('It must be an integer\n'))


def ageCalculator(birthYear):
    age = 2018 - birthYear
    print('your age is: ', age)
    return age


def test_correct_age_is_calculated(calculatedAge):
    assert currentAge == calculatedAge
    print('\nAssertion made for: ', currentAge, ' years old!')
    return True


currentAge = ageCalculator(birthYear)
testAge = test_correct_age_is_calculated(currentAge)
