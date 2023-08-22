import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="animal"
)

cursor=db.cursor()

#create a table buffalo
#id age weight breed image

# query="""create table buffalo
# (id int auto_increment primary key,
# age int not null,
# weight int not null,
# breed varchar(200) not null,
# image varchar(200)not null)"""

query1="""
create table pets(
id int auto_increment primary key,
age int not null,
gender varchar(200) not null,
breed varchar(200) not null,
location varchar(200),
price int not null
)
"""


cursor.execute(query1)