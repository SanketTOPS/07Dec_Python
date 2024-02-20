import sqlite3

try:
    dbcon=sqlite3.connect('mydb.db')
    print("Database created/connected!")
except Exception as e:
    print(e)

#Table Created
tbl_create="create table studinfo(id integer primary key autoincrement,name text,sub text)"
try:
    dbcon.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)


#Insert Data
"""insert_data="insert into studinfo(name,sub)values('sanket','python'),('harsh','android'),('ashok','java'),('hitesh','python'),('pratik','php')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

#Update Data
"""update_data="update studinfo set name='prasiddh',sub='kotlin' where id=7"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where id=10"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""


cr=dbcon.cursor()

#Show data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)

    n=1
    for i in data:
        #print(i)
        print(f"Record[{n}] = {i}")
        n+=1
except Exception as e:
    print(e)
    