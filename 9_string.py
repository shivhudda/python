str1 = 'i am Spartaaaaa' #single qoute string
str2 = "i am john."      #double qoute string
str3 = '''i am matt'''  #triple qoute string

x = str1.endswith('a')
print(x)        #return true or false

x = str2.count('a')
print(x)   #counts the total no. of occurrence of any character in the string.

x = str3.capitalize()
print(x)   #capitalizes the first character of any string. It doesn’t take any argument.

print(str1.upper()) #copy of the string converted to uppercase

print(str1.lower()) #copy of the string converted to lowercase

print(str1.find('s'))
'''
This function finds any given character or word in the entire string.
 It returns the index of first character from that word.
'''

x = str3.replace('matt', 'shivhudda')
print(x)
'''
This function replaces 
the old word or character with a new word or character from the entire string.'''

print(len(str1)) #finding the length of any string.

# string slicing
foo = 'using slicing in python strings'
print(foo[0:])         #print full string      
print(foo[0:10000])    #print full string 
print(foo[0:4])
print(foo[2:4])
print(foo[-7:-2])

print(foo[:4])

print(foo[1:8:2])
print(foo[-9:-2:3])
print(foo[::-2])
print(foo[::-1])
           