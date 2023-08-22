class student:

    rollno : int 
    name : str 
    course : str


    def add_student(self,roll,name,course):    #sft points to the class object 
        self.rollno = roll
        self.name = name
        self.course = course 

    def get_student(self):
        print(self.rollno,self.name,self.course)


# reference_name=className()
obj1=student()
obj2=student()
obj1.add_student(1,"niya","python")
obj2.add_student(2,"nikku","django")
obj1.get_student()






