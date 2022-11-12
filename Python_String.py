# Create a string in Python
str1 = "iNeuron"
print(str1)

str2 = "Shashank's"
print(str2)

str3 = 'He is a "Good" boy'
print(str3)

# use length function
print("length of the string : ",len(str3))

# how to write multiline string
str4 = '''Shashank is
not going
to attend 
the seminar
'''
print(str4)

# string concatenation
str5 = "Shashank"
str6 = "Mishra"
print(str5 + str6)

# string comparsion?
str7 = "Shashank"
str8 = "Shashank"
print(str7 == str8)

# how to print the each character from the string
for char in str8:
    print(char)

print(str7[0])
print(str7[1])
print(str7[2])
print(str7[3])
print(str7[4])
print(str7[5])
print(str7[6])
print(str7[7])

str9 = "Shashank"

# Update the 4th character in the string by M
# str9[3] = 'M'
# print(str9)

# convert string into lower case
print(str9.lower())

# convert string into upper case
print(str9.upper())

# Other functionalities will be same as list like Slicing etc
