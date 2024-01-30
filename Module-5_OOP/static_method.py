class studinfo:
    @staticmethod
    def getdata(stid,stnm):
        print("ID:",stid)
        print("Name:",stnm)


st=studinfo()
id=input("Enter ID:")
name=input("Enter Name:")
st.getdata(id,name)
