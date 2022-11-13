# Sets in python
set1 = set()
print(type(set1))

set3 = {1,2,3,4,5,2,1,4}
print(set3)
print(type(set3))

# dictionary
# set4 = {}
# print(type(set4))

list1 = [1,2,3,4,1,2,3,4,5,6,7,8,1]
set2 = set(list1)
print(set2)

# how we can iterate elements in the set
for num in set2:
    print(num)

# Convert output of set into list
list1 = [1,2,3,4,1,2,3,4,5,6,7,8,1]
set5 = list(set(list1))
print(set5)
print(set5[-1])


# how to insert elements in the set
set6 = set()
set6.add(1)
set6.add(1)
set6.add(2)
set6.add(5)
set6.add(2)
set6.add(1)
set6.add(2)
print(set6)

# use of update method
tmp = [1,2,3,4,5,1,2,3,4,5,1,2,3]
set6.update(tmp)
print(set6)

# calculate the length of the set
print(len(set6))

# Set operations
set_a = {1,2,3,4,5,6}
set_b = {3,6,8,9,10}

# union operation
print(set_a | set_b)

# intersection operation
print(set_a & set_b)

# A - B ? 
# B - A ?
# Difference in Sets
print(set_a - set_b)
print(set_b - set_a)


# Comparison in sets
set_x = {1,2,3,4,5}
set_y = {1,2,3,5,4,5,1}
print ( set_x == set_y )

set_x = {1,2,3,4,5,6} # {1,2,3,4,5,6}
set_y = {1,2,3,5,4,5,1} # {1,2,3,4,5}
print ( set_x == set_y )

# set_m = {5,6,7,1,2,4}
# print(set_m)
