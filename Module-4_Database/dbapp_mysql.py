import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='tempdb')
    print("Database connected!")
except Exception as e:
    print(e)


cr=db.cursor()

#Table Created
tbl_created="create table studinfo(id integer primary key auto_increment,name text,city text)"
try:
    cr.execute(tbl_created)
    print("Table created successfully!")
except Exception as e:
    print(e)


#Insert Data
"""n=int(input("Enter number of students:"))

for i in range(n):
    name=input("Enter your name:")
    city=input("Enter your city:")
    
    insert_data=f"insert into studinfo(name,city)values('{name}','{city}')"

    try:
        cr.execute(insert_data)
        db.commit()
        print("Record inserted!")
    except Exception as e:
        print(e)"""


# Update Data

"""update_data="update studinfo set name='nirav' where id=4"
try:
    cr.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""


# Delete Data
"""delete_data="delete from studinfo where id=4"
try:
    cr.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i)

except Exception as e:
    print(e)