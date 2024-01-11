import keyword

x=keyword.kwlist
print(x)
print(len(x))


key=input("Enter any keyword:")

if key in x:
    print("Yes...This is keyword!")
else:
    print("Error!This is not keyword....")