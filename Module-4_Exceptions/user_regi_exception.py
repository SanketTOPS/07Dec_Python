try:
    name=input("Enter Name:")
    if name.isalpha():
        print("Name:",name)
    else:
        print("Name must be an alpha!")
        raise ValueError

    email=input("Enter email:")
    if email.islower():
        print("Email:",email)
        
    raise ValueError
except:
    print("Error! Enter proper details!")