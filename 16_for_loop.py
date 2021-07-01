l1 = [
    ["shiv",1],
    ['matt',2],
    ['john',23],
    ['spartaaa',12]
    ]
dict1 = dict(l1)
for item in dict1:
    print (item)
for item,val in dict1.items():
    print (item,'value is',val)

items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]
for item in items:
    if str(item).isnumeric() and item>5:
        print (item)

for i in range(1,23,2):
    print (i)

for i in range(1,14):
    print (i)
