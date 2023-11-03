##in sets data is stored in the sorted manner
###unordered collection, iterable, mutable , no duplication
#####no assignment after set is defined once , i.e. s1[8] = 20
s1 = {1,2,3,4,6,43,7}
s2 = {1,2,3,4,5}
# intersection operation 
print(s1.intersection(s2))

# difference operation 
print(s1.difference(s2))

print(s1.issubset(s2))
print(s1.issuperset(s2))
