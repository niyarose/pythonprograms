import mysql.connector 


db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="animal"
)


cursor=db.cursor()


query1="""
insert into pets(age,gender,breed,location,price) values(19,"female","breed5","kollam",25500)
"""


cursor.execute(query1)
db.commit()