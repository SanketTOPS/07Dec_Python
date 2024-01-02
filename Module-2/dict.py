stdata={'id':101,'name':'Sanket','city':'Rajkot'}

#print(stdata)
"""print(stdata['city'])
print(stdata.get('id'))
print(stdata.keys())
print(stdata.values())
print(len(stdata))
"""

#stdata['id']=102
#print(stdata)

# ---------------------------------------------- #

#print(stdata)
#stdata['sub']='Python'
#stdata.pop('city')
#del stdata['name']
#stdata.clear()
print(stdata)

newdict=stdata.copy()
print(newdict)


"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} and Values={j}")"""


"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""


"""if 'Sanket' in stdata.values():
    print("Yes...")
else:
    print("Nooo")
"""
