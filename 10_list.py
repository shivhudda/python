list1 = ['ram', 23,True,3+4j , 'shivhudda' ,45.3]

# swapping two numbers
a = 10
b = 34
a,b = b,a
print(a,b)

l1 = ['ram', 23,True,3+4j , 'shivhudda' ,45.3]
print(l1[3])   #finding index characters

l1.remove('ram')  #remove an element

l1.pop(-1)  #pop a item using index numbers

l2 = []   #creating a blank list
l2.append('mukesh')      #adding one element end of list
l2.append(34)    #adding one element end of list
l2.append(True)    #adding one element end of list

l2.insert(2, "shivhudda")  #adding a element using index value

l2[2] = 'shiv'   #updating a elements

l3 = [1,34,56,78,6,4,3455,43,4]
l3.sort()  #sorting a list

l3.reverse()  #reerse a list

# list slicing
print(l3[0:10:2])
print(l3[3:7:3])
print(l3[::2])
print (l3)