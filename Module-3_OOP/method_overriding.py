class student:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

class app1(student):
    def getdata(self, id, name):
        return super().getdata(id, name)

class app2(student):
    def getdata(self, id, name):
        return super().getdata(id, name)


st=student()
st.getdata(1,'Sanket')

a1=app1()
a1.getdata(2,'Mitesh')

a2=app2()
a2.getdata(3,'Nirav')
    


