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


class developer(employee):
    raiseammount = 1.10

    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language


class manager(employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev1 = developer('ian', 'kean', 20000, 'python')
dev2 = developer('moto', 'sana', 30000, 'java')

mgr1 = manager('sue', 'smith', 90000, [dev1])
