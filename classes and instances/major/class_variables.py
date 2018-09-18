'''
Created on Jun 26, 2018

@author: Yan
'''
''''the following piece of code shows how to instantiate a
a variable and even keep track of the variable in the ]class. 
it shows how to pass assignments and retrieve data from methods'''


class employee:
    num_of_employee = 0
    raiseammount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + '@company.com'
        employee.num_of_employee += 1
             
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def applyraise(self):
        self.pay = int(self.pay * self.raiseammount)
        
        
emp1= employee('ian', 'kean', 23043)
emp2=employee('moto', 'sana', 23435)

print(employee.num_of_employee)

emp1.raiseammount = 1.05

'''to check the the variable assignment'''
print(employee.__dict__)

'''various methods of accessing functions in a class'''
print(employee.raiseammount)
print(emp1.raiseammount)
print(emp2.raiseammount)