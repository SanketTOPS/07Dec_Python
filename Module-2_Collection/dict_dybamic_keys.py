stdata={}

keys=['id','name','sub','city']

for i in range(len(keys)):
    v=input(f"Enter your value for {keys[i]}:")
    stdata[keys[i]]=v

print(stdata)
