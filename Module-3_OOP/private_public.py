class student:
    __stid=12 #private
    __stnm="Sanket" #private

    def __getdata(self):
        print("This is getdata!")
        print("ID:",self.__stid)
        print("Name:",self.__stnm)

    def printdata(self):
        self.__getdata()

st=student()
#st.getdata()
st.printdata()