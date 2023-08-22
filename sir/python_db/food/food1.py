from get_connect import db_connect




class food:


    def connect(self):
        db=db_connect(password="Password@123",database="food")
        return db




    def post(self,*args,**kwargs):
        db=self.connect()
        cursor=db.cursor()
        query="insert into food(name,price,category)" "values=(%s,%s,%s)"
        data=tuple(v for v in kwargs.values())
        cursor.execute(query,data)
        db.commit()
        return kwargs
    


fd=food()
print(fd.post(name="ghee-roast",price=70,category="veg"))