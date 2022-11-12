# Syntax
# while exp:
#     statements

# write a program to print the table of 9
num = 9
counter = 1

while counter<=10: # Either True or False
    ans = num * counter
    print(num,' * ',counter,' = ',ans)
    counter = counter + 1

# What will happen if counter not incremented??
while counter<=10: # Either True or False
    ans = num * counter
    print(num,' * ',counter,' = ',ans)
    #counter = counter + 1

# 9  *  1  =  9 -> 

# What will happen?
while True:
    print("iNeuron")
