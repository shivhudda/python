# write mode    
f = open('29_myfile.txt', 'w')
a = f.write('lorem ipsum  dollar sit amet.\n')
f.write('shivhudda')
'''There is a certain limitation to the write mode of the opening file that it overrides the existing data into the file.'''
print (a)  #its return number of written characters
f.close()

# append mode   
f = open('29_myfile2.txt','a')
a = f.write('shivhudda is a programmer.\n')
print (a)   #its return number of written characters
f.close()

# read and write mode combo
f = open('29_myfile3.txt','r+')
print(f.read())
f.write('\n so let\'s starting to learn file io.')

f.close()