######### tuples #"''''''"
## '( )' are used for creating tuple
## creating tuple

#### one-way
tpl1 = tuple()

### another way
tpl2 = (2,4,5,2,6,8,2)


print(type(tpl1))
print(type(tpl2))

print(tpl2)

print(tpl2.count(2))## this will count the total occurences of the 2
print(tpl2.index(2))##this will give the index of the 2 (first occurence)

## no assignment after declared once to exiting element
## e.g ----- tpl2[3] = 45 --it will give the error


## accessing tuple element
print(tpl2[1])



### can be converted into list and set using type casting
l1 = list(tpl2)
print(type(l1))
print(tpl2)



