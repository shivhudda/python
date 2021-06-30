s = set()
# print(type(s))
# l = [1,2,3,4,5]
# set_from_list = set(l)
# print(type(set_from_list))
s.add(1)   #adding element in set
s.add(2)
s.add(2)
s.add('shivhudda')
s.remove(1)
print(s)
s1 = {1,2,3,674,574}
print(s.isdisjoint(s1))
print(s.intersection(s1))
print(s.union(s1))
print(s1.difference(s))
