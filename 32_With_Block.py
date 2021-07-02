with open('31_myfile.txt') as f:
    print(f.read(10))
#opening multiple files
with open('31_myfile.txt') as f,open('27_myfile.txt') as g:
    print(f.read(12))
    print(g.read(20))

with open('31_myfile.txt') as f:
    print('1',f.readlines())

f = open('31_myfile.txt') 
print('2',f.readlines())

