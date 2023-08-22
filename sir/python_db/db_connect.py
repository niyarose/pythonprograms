from get_connect import db_connect


db=db_connect(password="Password@123",database="animal")
Cursor=db.cursor()



query="select * from pets"


Cursor.execute(query)
records=Cursor.fetchall()


for rec in records:
    print(rec)


db.close()