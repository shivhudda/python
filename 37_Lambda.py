result = lambda n1,n2,n3: n1+n2+n3
print('sum of three values:',result(10,20,30))

minus = lambda x,y:x-y
print(minus(12,34))

# sort method
l1 = [[1,34,5],[4,5,56],[4342,23,66764],[234,0,3]]  
l1.sort(key=lambda x:x[1])
print(l1)