import re

#Sanket2020
unm=input("Enter Username:")

unm_pattren="[A-Z]+[a-z]+[0-9]"

x=re.findall(unm_pattren,unm)
if x:
    print("Valid Username!")
else:
    print("Error!Invalid Username...")
