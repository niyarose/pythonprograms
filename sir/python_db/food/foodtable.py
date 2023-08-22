import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="food"
)

Cursor=db.cursor()

query="""create table food
(id int auto_increment primary key,name varchar(200) not null,price int not null,category varchar(200) not null)"""

Cursor.execute(query)