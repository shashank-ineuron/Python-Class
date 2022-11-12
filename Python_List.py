# Declare empty list
L1 = []
#print(type(L1))
print("Initial length of List : ",len(L1))

# Insert values in list
L1.append(5)
L1.append(7)
L1.append(8)
print(L1)

# Create a list of 1000 numbers start from 1 to 1000
# int_list = []
# for num in range(1,1001):
#     int_list.append(num)

# How to calculate the length of a list?
len_of_list = len(L1)
print("Lenght of a list : ",len_of_list)


# how to check is list are equal to each other?
list1 = [1,"Shashank",20,"Hi"]
list2 = [1,"Shashank",20,"Hi"]
print("Lists are equal ?? ", list1 == list2)

list1 = [1,"Shashank",20,"Hi"]
list2 = [1,"Shashank","Hi",20]
print("Lists are equal ?? ", list1 == list2)

# List concat
list4 = [1,2,3,4,5]
list5 = [80,90,100,110]
result = list4 + list5
print(result)

# how to access list values
list6 = [10,15,20,25,30,35]

# Print all the elements of given list - Option 1
for num in list6:
    print(num)

# Print 3rd elements of given list - Option 2
# syntax = list_name[index]
print(list6[0])
print(list6[1])
print(list6[2])
print(list6[3])
print(list6[4])
print(list6[5])

# What will happen ??
# Answer will be Index out of range
# print(list6[100])

list7 = [1,"Shashank",1000]
print(list7)

# how to update the value of list index item?
# update Shashank to Rahul
list7[1] = "Rahul"
print(list7)


# how to print list elements using length?
for index in range(0, len(list7)): # range(0, 3) -> [0, 1, 2]
    print(list7[index])

list8 = [ 1 , 2 , 50, "Shashank", [6,6,6] , "Rahul"]
print(len(list8)) # What will be the output ???


# Difference between append() and extend()
list9 = [20,30,40]
list10 = ["hi", "hello", "bye"]
list9.append(list10)
print("Output of Append : ",list9)
print("Length after Append : ",len(list9))

list11 = [20,30,40]
list12 = ["hi", "hello", "bye"]
list11.extend(list12)
print("Output of Extend : ",list11)
print("Length after Extend : ",len(list11))

# List slicing 
list13 = [20,30,40,50,60,80,90]
# Syntax -> list_name[start : end]
# end index is exclusive
print(list13[ 0 : ])
print(list13[ 3 : ])
print(list13[ : ])
print(list13[  : 4 ])
print(list13[ 2 : 6 ])
print(list13[ 0 : : 2]) # 3rd value is for step

# How to print the last value of the list?
print(list13[ len(list13) - 1 ])
print(list13[-1]) # negative index -1 means last element of the list

# Print second last element from the list??
print(list13[-2])

# print inout list in reverse direction
print(list13[-1 : : -1])






