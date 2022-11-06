# Numerical operators in Python

# + for addition
# - for substractions
# * for multiplication
# / for float division
# // for integer division
# ** for power calculation
# % for Modulus

x = 5
y = 3

print("Addition of x + y = ", x+y)
print("Substraction of x - y = ", x-y)
print("Multiplication of x * y = ", x*y)
print("Float Division of x / y = ", x/y)
print("Integer Divison of x // y = ", x//y)
print("Modulus of x % y = ", x%y)
print("Power of y on x i.e; x ** y = ", x**y)

# concat operation for string
full_name = str_data + " " + "mishra"
print("Full name = ", full_name)

# if we can use - as well ? IT will not work
minus_str = "shashank" - "mishra"
print("Minus str = ", minus_str)

multiply_str = "shashank"*"mishra"
print("Multiply str = ", multiply_str)

power_str = "shashank"**"mishra"
print("Power str = ", power_str)

power_str = "shashank" ** 3
print("Power str = ", power_str)

multiply_numeric_str = "shashank"*5
print("Multiply numeric str = ", multiply_numeric_str)

# Assignment operators
# =  , x = 5
# += , x += 5 -> x = x + 5
# -= , x -= 5 -> x = x - 5
# *= , x *= 5 -> x = x * 5
# /= , x /= 5 -> x = x / 5
# //= , x //= 5 -> x = x // 5
# %= , x %= 5 -> x = x % 5


# Comparison Operators ( we compare operand values)
# == , Equals to condition , x == y
# != , Not Equals to condition , x != y
# > , Greater than condition , x > y
# < , Less than condition , x < y
# >= , Greater than and Equals to condition , x >= y
# <= , Less than and Equals to condition , x <= y

a = 10
b = 5
print("Result of a == b , ", a == b)
print("Result of a != b , ", a != b)
print("Result of a > b , ", a > b)
print("Result of a < b , ", a < b)
print("Result of a >= b , ", a >= b)
print("Result of a <= b , ", a <= b)


# logical operators in Python ( Logical check will happen for expression result)
# and -> Returns true if both statements are true 
# or -> Returns true if one of statements are true
# not -> Reverse the result, returns false if the result is true

m = 10
n = 8
print("m>10 and n<10 Result " , m>10 and n<10) # False and True -> False
print("m>20 or n<10 Result " , m>10 or n<10) # False or True -> 
print("not(m>20 and n<10) Result " , not(m>10 and n<10)) 
# not(False and True) -> not(False) -> True
