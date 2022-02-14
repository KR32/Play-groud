class Employee:
    #self=Employee
    #__init__= like constructor of Employee class
    #self.variablename= instance variables
    #Employee.variablename=Class variablename
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
    def fulname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_incerment(self):
        self.pay=int(self.pay*1.04)
# emp=Employee('hello',' sir',15000)
# print(emp.fulname())