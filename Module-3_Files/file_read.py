fl=open('demo.txt','r')

#print(fl.read())
#print(fl.readline())
#print(fl.readlines())
#print(fl.readlines()[1])
#print(fl.readlines()[0:3])

"""n=1
for i in fl:
    #print(i)
    print(f"Line:[{n}] = {i}")
    n+=1"""


if fl.readable():
    print("Yes...file is readable")
else:
    print("Error!")
