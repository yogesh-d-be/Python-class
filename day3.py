"""" #comparison operator

# == 
# !=
# >
# <
# >=
# <=
"""
"""a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
# a= 50 b =37
print("Equal to", a==b)
print("Not Equal to", a!=b)
print("Greater than", a>b)
print("less than", a<b)
print("Greater than or equal to", a>=b)
print("less than or equal to", a<=b)"""

#Logical operator

# and
# or
# not

"""a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

x = a != b
y = a>b

print("Logical and", x and y)
print("Logical or", x or y)
print("Logical not", not(x or y))"""

#Assignment operator
# +=
# -=
# *=
# /=
# %=
# //=

"""a = int(input("Enter a value: "))#25
b = int(input("Enter b value: "))#15
print("before a value is: ",a)
a+=b #a = a+b
print("a value is: ",a)
print("b value is: ",b)"""


# Decision making 

# if
# if else
# if elif else
# nested if

"""mark = int(input("Enter a mark value: "))

if(mark>35):
    print("Pass")"""

"""mark = int(input("Enter a mark value: "))

if(mark>=35):
    print("Pass")
else:
    print("Fail")"""

"""age = int(input("Enter age: "))


if(age>=18):
    voter = input("Do you have voterId (True/False): ").strip().lower()
    voterId = (voter == "true")#False
    if(age >= 18 and voterId):
        print("You are eligible for voting and age is", age, voterId)
    elif(age >= 18 and not voterId):
        print("You got voter age but need to take voterId: ", age, voterId)
    else:
        print("You are not eligible for voting and age is", age)
else:
    print("You are not eligible")"""




#######Feb batch


# Arithmetic operators

# + - addition
# - - subtraction
# * - multiplication
# / - division
# % - modulo division
# // - floor division
# ** - exponentation

# a = int(input("Enter a number 1:"))
# b = int(input("Enter a number 2:"))

# # print("Type", type(a), type(b))

# print("Addition", a+b)
# print("Subtraction", a-b)
# print("Multiplication", a*b)
# print("Divison:", a/b)
# print("Modulo division", a%b) #Reminder
# print("Floor division", a//b) #Quotient
# print("Exponentation", a**b)  # a power of b



# Comparison Operators


"""" #comparison operator

# == 
# !=
# >
# <
# >=
# <=
"""

# a = int(input("Enter a number 1:"))
# b = int(input("Enter a number 2:"))


# print("Equal to", a ==b)
# print("Not Equal to", a !=b)
# print("Greater than", a >b)
# print("Less than", a <b)
# print("Greater than or Equal to", a >=b)
# print("Less than orEqual to", a <=b)


# Logical operator

# and
# or
# not

# a = 6
# b = 5

# x = a != b 
# y = a >= b 

# print("logical and", x and y)
# print("logical or", x or y)
# print("logical not", not(x and y))


#Assignment operator
# +=
# -=
# *=
# /=
# %=
# **=
# //=

# a = 7
# a+=2 

# a*=5
# a//=5
# print("Add", a)

# Decision making

# if(condition):
#     statement



# if(a!=b):
#     print(a,"and",b ,"values are not not equal")


# if(a>b):
#     print(f"{a} is greater")
# else:
#     print(f"{b} is greater")

# a = int(input("Enter a value:")) #10
# b = int(input("Enter b value:")) #8
# c = int(input("Enter c value:")) #20

# if((a>b) and (a>c)):
#     print(a,"is greater") 
# elif((b>a) and (b>c)):
#     print(b,"is greater") 
# else:
#     print(c,"is greater") 



# Arithmetic operators

# +
# -
# *
# /
# %
# //
# **

# a = 2
# b=4

# print("Add", a+b)
# print("Sub", a-b)
# print("Mul", a*b)
# print("Division", a/b)
# print("Modulo division", a%b)
# print("Floor division", a//b)
# print("Exponentation", a**b)


# Comparison operators

# ==
# !=
# >
# <
# >=
# <=


# a = 7
# b = 10

# print("Equal to", a == b) 
# print("Not Equal to", a != b)
# print("Greater than", a > b)
# print("Less than", a < b)
# print("Greater than or equal to", a >= b)
# print("Less than or equal to", a <= b)


# Logical Operators
# and 
# or
# not

# a = 7
# b = 10

# print("Logical and", (a < b) and (b > a))
# print("Logical or", (a == b) or ( a != b))
# print("Logical not", not(a==b))


# Assignment Operators

# +=
# -=
# *=
# /=
# %=
# //=
# **=

# a =5

# a += 5 #-->  a = a+5
# a-=2
# a*=4
# a//=2
# a/=2
# a%=3
# a**=3
# print("Result:",a)


#conditional statements
# if(condition):
#     statements

# city = input("Enter your tourist place: ")

# if(city == "chennai"):
#     print("Welcome to chennai")


# attendanance = int(input("Enter your attendance in percentage: "))

# if(attendanance > 70):
#     print("You are eligible to write a semester exam")
# else:
#     print("You are not eligible to write a semester exam")



# age = int(input("Enter your age: "))
# has_license = input("Do you have license(y/n): ")

# if(age>18 and has_license == "y"):
#     print("You can drive")
# elif(age>18 and has_license == "n"):
#     print("You can't drive")
# else:
#     print("You are under age. You cannot drive")


# age = int(input("Enter your age: "))

# if(age>=18):
#     has_license = input("Do you have license(y/n): ")
#     if(has_license == "y"):
#         print("You can drive")
#     elif(has_license == "n"):
#         print("You can't drive")
# else:
#     print("You are under age. You cannot drive")


#March and June
#Comparison or relational operators
# ==
# !=
# >
# <
# >=
# <=


# a = int(input("Enter a value: "))
# b = int(input("Enter b value: "))

# print("Equal to", a==b)
# print("Not Equal to", a!=b)
# print("Greater than", a>b)
# print("Less than", a<b)
# print("Greater than or Equal to", a>=b)
# print("Less than or Equal to", a<=b)