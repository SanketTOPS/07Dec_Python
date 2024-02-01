class grandfather:
    gold=0
    house=0

    def g_getdata(self):
        self.gold=input("Enter details of gold:")
        self.house=input("Enter details of house:")

class father(grandfather):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("Enter Car details:")
        self.bal=input("Enter bank balance details:")

class son(father):
    def printdata(self):
        print("Gold:",self.gold)
        print("House:",self.house)
        print("Car:",self.car)
        print("Balance:",self.bal)

sn=son()
sn.g_getdata()
sn.f_getdata()
sn.printdata()