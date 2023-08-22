class Users:
    data=[
        {"id":1,"username":"jhon","email":"jhon@gmail.com","password":"password@123"},
        {"id":2,"username":"hari","email":"hari@gmail.com","password":"password@123"},
        {"id":3,"username":"ravi","email":"ravi@gmail.com","password":"password@123"},
        {"id":4,"username":"vijay","email":"vijay@gmail.com","password":"password@123"},
        {"id":5,"username":"vinu","email":"vinu@gmail.com","password":"password@123"},
        {"id":6,"username":"tom","email":"tom@gmail.com","password":"password@123"},
    ]

    # def getall_users(self):    #getall_users => method 
    #     return self.data
    
    def get(self):    #getall_users => method 
        return self.data
    
    # def user_detail(self,id):
    #     return [u for u in self.data if u.get("id")==id]
    
    def retrieve(self,id):
        return [u for u in self.data if u.get("id")==id]
    
    def post(self,data):
        self.data.append(data)

    def destroy(self,id):
        obj=[u for u in self.data if u.get("id")==id][0]
        self.data.remove(obj)
    
    def put(self,id,value):
        obj=[u for u in self.data if u.get("id")==id]+[0]
       

        pos=self.data.index(obj)
        self.data[pos]=value[0]



obj=Users()
# print(obj.getall_users())
# print(obj.retrieve(2))
# student_data={"id":7,"username":"ram","email":"ram@gmail.com","password":"password123"}
# obj.post(student_data)
# obj.destroy(5)
# print(obj.get())
print(obj.retrieve(5))
data={"id":2,"username":"vinus","email":"vinu@gmail.com","password":"password123"}
obj.put(5,data)
print(obj.retrieve(5))



