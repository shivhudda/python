# open a file     
f = open('27_myfile.txt', 'rt')
# reading file   
print(f.read(2))  #Here, you will get the first two characters of the file.
print(f.readline())   #its print first line of file
print(f.readline())  #using again readline return next line of file
print(f.readline(20)) #return first twenty characters of the file

for line in f:
    print(line)

f.close()  #closing a file is good habit

x = open("27_myfile2.txt", 'rt')
content = x.read(40)
print('1',content )
content2 =x.read(40)
print('2',content2)

