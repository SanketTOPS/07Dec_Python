n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
print("1: for Add")
print("2: for Sub")
print("3: for Mul")
print("4: for Div")
ch=int(input("Enter your choice:"))


def add():
    print("Sum:",n1+n2)

def sub():
    print("Sub:",n1-n2)

def mul():
    print("Mul:",n1*n2)

def div():
    print("Div:",n1/n2)


if ch==1:
    add()
elif ch==2:
    sub()
elif ch==3:
    mul()
elif ch==4:
    div()
else:
    print("Error!Invalid choice...Plz try again!")





