try:
    name=input("Enter your name:")
    if name.isalpha():
        print("Your Name:",name)
        mob=input("Enter your mobile number:")
    if mob.isdigit() and len(mob)==10:
        print("Mobile Number:",mob)    
except:
    print("Error!")

