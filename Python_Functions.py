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


# # example of a function which doesn't accept any parameter
# # and doesn't return anything
# def welcome_message():
#     print("Welcome to iNeuron Batch-2 !!!")

# welcome_message()

# # example of a function which doesn't accept any parameter
# # and does return something
# def bot_message():
#     print("Message from Bot using Print!!")
#     return "Message from Bot !!"

# print( bot_message() )
# result = bot_message()
# print("Output from bot_message() ", result)


# example of a function which accepts some parameter
# and return the values
def avg_of_two_nums( a , b):
    count = 2
    print("First Value : ", a)
    print("Last Value : ", b)
    avg_result = (a+b)/2
    return avg_result

num1 = 10
num2 = 15
# output = avg_of_two_nums( num1, num2 )
# print("Result of avg_of_two_nums functions : ", output)

# output1 = avg_of_two_nums( num1 )
# print("Result of avg_of_two_nums functions : ", output1)


# Write a function to calculate the factorial of a num ?
def factorial(n):

    if n == 0 or n == 1:
        return 1

    result = 1
    for num in range(1, n+1):
        result = result * num
    
    return result

x = 5
ans = factorial(x)
print("Factorial of number ",x, " = ", ans)

x = 0
ans = factorial(x)
print("Factorial of number ",x, " = ", ans)


# how to return multiple values from function

a , b , c = 2 , 3, 5
print("Value of a is : ",a)
print("Value of b is : ",b)
print("Value of c is : ",c)

def square_and_cube(n):
    sqr = n*n
    cube = n*n*n
    return sqr,cube

num = 3
sqr_ans , cube_ans = square_and_cube(num)
print("Square of ",num," is : ",sqr_ans)
print("Cube of ",num," is : ",cube_ans)


# How to create optional arguments in python fucntions
def multiply(a , b=3):
    result = a * b
    return result

num1 = 5
num2 = 10
print( multiply(num1 , num2) )
print( multiply(num1) )
print( multiply(num2) )

# What if we reverse this part
# Not possible
# def multiply(a=3 , b):
#     result = a * b
#     return result

def multiply(a , b=3, c=10):
    result = a * b * c
    return result

# What if we have more than 2
num1 = 5
num2 = 10
num3 = 2
print( multiply(num1 , num2, num3) )
print( multiply(num1, num2) )
print( multiply(num2, num3) )
print( multiply(num3) )
# print( multiply(num2) )


# Non-Key Valued arguments
def example_nonkeyed_args( *argv ):
    for param in argv:
        print(param)

example_nonkeyed_args( 'Hello' , 'Welcome', 'To', 'iNeuron' )


# Key Value type of arguments in Python
def example_of_kwargs( **kwargs ):

    print("Value of host : ", kwargs['host'])
    print("Value of port : ", kwargs['port'])
    print("Value of password : ", kwargs['pswd'])

    for k,v in kwargs.items():
        print("Key is ",k,' and Value is ',v)


example_of_kwargs( host='170.80.80.80' , port=9021, pswd='XXFGH' )

example_of_kwargs( port=9021, pswd='XXFGH' , host='170.80.80.80')
