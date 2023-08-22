# def create_person(*args):
#     print(args)


# create_person("hari",35,"pkd","ekm") # tuple


# def create_person(**kwargs):
#     print(kwargs)


# create_person(name="hari",age=35,native_place="pkd",working_place="ekm") #dictionary 


class Student:
        rollno: int 
        name: str
        course: str
        def __init__(self,**kwargs):
            self.rollno=kwargs.get("rollno")
            self.name=kwargs.get("name")
            self.course=kwargs.get("course")
            
        def get_student(self):
            print(self.rollno,self.name,self.course)

        def __str__(self):    #to print the specified parameter only 
             return self.name

obj=Student(rollno=18,name="niya",course="django")
print(obj)
obj.get_student()