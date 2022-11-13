# Functions in python
# What about len() 

# Examples of inbuilt functions
# list1 = [1,2,3,4,5,6]
# print("Maximum number from list : ", max(list1))
# print("Minimum number from list : ", min(list1))
# print("Sum number from list : ", sum(list1))

# How do functions works?
# They may or may not accepts input parameter
# They may or may not return any output


# example of a function which doesn't accept any parameter
# and doesn't return anything
def welcome_message():
    print("Welcome to iNeuron Batch-2 !!!")

welcome_message()

# example of a function which doesn't accept any parameter
# and does return something
def bot_message():
    print("Message from Bot using Print!!")
    return "Message from Bot !!"

print( bot_message() )
result = bot_message()
print("Output from bot_message() ", result)



