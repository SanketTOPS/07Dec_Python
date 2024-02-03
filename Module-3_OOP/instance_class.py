class studinfo:
    stid=12
    stnm="Sanket"


    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#Objcet
"""st=studinfo()
st.getdata()

st.stid=34
st.stnm="Hitesh"

st.getdata()"""


#Instance
studinfo().getdata()
studinfo().stid=1
studinfo().stnm='Harsh'
studinfo().getdata()

