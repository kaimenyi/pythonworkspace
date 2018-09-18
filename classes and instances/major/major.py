'''
Created on Jun 26, 2018

@author: Yan
'''

class employee:
    num_of_employee = 0
    raiseammount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '.' + '@company.com'
    
    num_of_employee
             
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def applyraise(self):
        self.pay = int(self.pay * self.raiseammount)
        
        
emp1= employee('ian', 'kean', 23043)
emp2=employee('moto', 'sana', 23435)

print(emp1.first)
print(emp1.email)