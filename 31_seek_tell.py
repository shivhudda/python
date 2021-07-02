f = open("31_myfile.txt",'r+')
f.seek(12)  #change file pointer position
x = f.tell()    #tell file pointer position
f.readline()
print(f.tell())
f.seek(150)
print(f.readline())
print(f.tell())
print(x)
f.close()