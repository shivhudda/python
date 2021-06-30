d1 = {}  #blank Dictionary
d2 = {
    'name':'shivhudda',
    'age':16,
    'work':'learning',
    'address':'xyz',
    'email':'abc@gmail.com'
}
d2['phone'] = 'xxx-xxx-xxxx'  #updating keys and values
d2[234] = 's.n.o.'  #updating keys and values
d2.update({'languages':'python,html,css,javascript'})  #updating using update method

del d2[234]    #delete a key-value pair using del with key
print(d2['email'])  #return a value of key

d3 = d2.copy() #copy dic. to a new dic.  its not effect on old dict. when using it
del d3['age']  

print(d2.keys())   #printing keys using keys method
print(d2.values()) #printing values using values method
print(d2.items()) #printing items using items method
print(d2)