import re


#sanketchauhan2020@gmail.com
email=input("Enter an email:")

email_pattern="^[a-z0-9_]+[@]+[a-z]+[./]+[a-z]{2,}$"


x=re.findall(email_pattern,email)

if x:
    print("Valid Email!")
else:
    print("Error!Invalid Email...")