stdata={} #root

n=int(input("Enter number of students:"))

for i in range(n):
    dic=input("Enter your child dict name:") #child dict

    stdata[dic]={}

    name=input("Enter Name:")
    city=input("Enter City:")
    
    stdata[dic]["Name"]=name
    stdata[dic]["City"]=city

print(stdata)



