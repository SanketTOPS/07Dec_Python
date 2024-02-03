class studinfo:
    def getdata(self,stid,stnm):
        print("ID:",stid)
        print("Name:",stnm)


st=studinfo()
#st.getdata(12,'Nirav') #static value

id=input("Enter ID:")
name=input("Enter Name:")
st.getdata(id,name) #dynamic value
