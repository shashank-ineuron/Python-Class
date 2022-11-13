# Dictionary in Python
dict1 = {}
print(type(dict1))

# How to insert values in Dictionary
dict2 = {}
dict2['name'] = 'Shashank'
dict2['age'] = 22
dict2['skills'] = ['Python', 'Java']
dict2['states_visited'] = ('UP', 'Goa')
dict2[45] = 'Random Key'
dict2['other_details'] = {'color' : 'Black', 'nationality' : 'Indian'}
print(dict2)

# Check the length of dictionary
print(len(dict2))

# how to access value of a particular key
print(dict2['name'])
print(dict2['skills'][0])
print(dict2['other_details']['nationality'])


# how to update value on a particular key
dict2['age'] = 30
print(dict2)

# How to get the keys from a dictionary
total_keys = list(dict2.keys())
print("Total Keys in dictionary : ",total_keys)

# How to get the values from a dictionary
total_values = list(dict2.values())
print("Total Values in dictionary : ",total_values)

# How to iterate on dictionary?
for k,v in dict2.items():
    print("Keys is = ",k,' and Value is = ',v)


# Compare dictionary ??

dict3 = {'a' : 1, 'b' : 2, 'c' : 3}
dict4 = {'b' : 2, 'c' : 3, 'a' : 1}
print(dict3 == dict4)

dict3 = {'a' : 1, 'b' : 2, 'c' : 3}
dict4 = {'b' : 2, 'c' : 3, 'a' : 5}
print(dict3 == dict4)


# how to delete specific key value pair from dictionary
print(dict2)

del dict2['age']
del dict2[45]

print(dict2)

# how to check if key exists in dictionary or not??
keys_in_dict = list(dict2.keys())
if 'skills' in keys_in_dict:
    print(True)
else:
    print(False)






