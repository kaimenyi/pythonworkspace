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
    
    def __repr__(self):
        return "employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)  
    
    def __add__(self, other):
        return self.pay + other.pay 
    
    def __len__(self):
        return len(self.fullname()) 
        
emp1= employee('ian', 'kean', 20000)
emp2=employee('moto', 'sana', 30000)

print(len(emp1))

print(emp1 + emp2)


print(repr(emp1))
print(str(emp1))