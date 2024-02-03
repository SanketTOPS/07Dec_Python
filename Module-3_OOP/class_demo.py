class studinfo:
    stid=12
    stnm='Mitesh'


    def getdata(self):
        print("This is getdata!")
    
    def getsum(self,a,b):
        print("Sum:",a+b)


st=studinfo() #object of class
print(st.stid)
print(st.stnm)
st.getdata()
st.getsum(23,56)