from typing import Any


class Employee:
    id : int 
    name : str
    designation : str
    salary : int


    def add_Employee(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.designation=desig
        self.salary=salary

    def get_Employee(self):
        print(self.id,self.name,self.designation,self.salary)

emp1=Employee()

emp1.add_Employee(11,"neenu","manager",120000)
emp1.get_Employee()



print(emp1.__class__ )