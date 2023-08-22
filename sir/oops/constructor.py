class student:

    rollno : int 
    name : str 
    course : str


    def __init__(self,roll,name,course):    #sft points to the class object 
        self.rollno = roll
        self.name = name
        self.course = course 

    def get_student(self):
        print(self.rollno,self.name,self.course)

obj=student(17,"niya","django")
obj.get_student()

obj2=student(18,"neenu","mearn")
obj2.get_student()

