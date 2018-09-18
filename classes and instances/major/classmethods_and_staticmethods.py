'''
Created on Jun 26, 2018

@author: Yan
'''
from builtins import classmethod
''''the following piece of code shows how to instantiate a
a variable and even keep track of the variable in the ]class. 
it shows how to pass assignments and retrieve data from methods'''


class employee:
    num_of_employee = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + '@company.com'
        employee.num_of_employee += 1
             
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def applyraise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    #this class method adjusts the raise amount whenever summoned    
    #eg employee.set_raise_amt(1.45)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    #the following class method takes a string and gives its values as a
    #variables defined by the programmer    
    @classmethod
    def fromstr(cls, empstr):
        first, last, pay = empstr.split('-')
        return cls(first, last, pay)
        
           
emp1= employee('ian', 'kean', 23043)
emp2=employee('moto', 'sana', 23435)

empstr1 = 'kaime-kaime-204555'

newemp1 = employee.fromstr(empstr1)

'''various methods of accessing functions in a class'''
print(newemp1.email)