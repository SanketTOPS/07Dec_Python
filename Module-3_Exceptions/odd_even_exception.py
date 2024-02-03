try:
    n=int(input("Enter any number:"))
    if n%2!=0:
        print("Number is:",n)
    
    else:
        raise ValueError
except:
   print("Error")


