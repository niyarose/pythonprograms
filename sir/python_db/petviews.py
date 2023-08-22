from get_connect import db_connect


class Petsview:

    def connect(self):
        
        db=db_connect(password="Password@123",database="animal")
        return db


    def get(self):                #retrive all pet details
        db=self.connect()
        cursor=db.cursor()
        query="""select * from pets"""
        cursor.execute(query)
        qs=cursor.fetchall()
        return qs
    


    def retreive(self,id):
        db=self.connect()
        cursor=db.cursor()
        query=f"select * from pets where id={id}"
        cursor.execute(query)
        records=cursor.fetchone()
        return records
    


    def post(self,*args,**kwargs):
        db=self.connect()
        cursor=db.cursor()
        query="insert into pets(age,gender,breed,location,price)""values(%s,%s,%s,%s,%s)"
        data=tuple( v for v in kwargs.values())
        cursor.execute(query,data)
        db.commit()
        return kwargs
    


    def destroy(self,id):
        db=self.connect()
        cursor=db.cursor()
        query=f"delete from pets where id={id}"
        cursor.execute(query)
        db.commit()


    def update(self,id,*args,**kwargs):
        db=self.connect()
        cursor=db.cursor()
        data=list(v for v in kwargs.values())
        data.append(id)
        query="update pets set age=%s,gender=%s,breed=%s,location=%s,price=%s where id=%s"
        cursor.execute(query,data)
        db.commit()
        
    




pv=Petsview()
# print(pv.get())
# print(pv.retreive(9))
# print(pv.post(age=15,gender="male",breed="breed5",location="kollam",price=26000))
# print(pv.destroy(9))

print(pv.update(id=12,age=26,gender="male",breed="breed6",location="tvm",price=45000))