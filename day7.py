# v = [10, 30, 40, 50, 30, 70]

# s = set(v)  

# l = list(s)

# print("set", s)
# print("list", l)

# def da_class():
#     print("Ready")
#     print("Travel")
#     print("Data analytics class")



# da_class()
# da_class()


# def Attendanance(name):
#     print(f"Present {name}")

# Attendanance("Naslin")
# Attendanance("Prakash")
# Attendanance("Sathya")

# def add(a):
#     print("A",a)

# def add2(b):
#     return b

# x = add(2)
# y = add2(6)

# print("x",x)
# print("y",y)
# def welcome():
#     print("Welcome to python")

# welcome()

# def DA_Class():
#     print("Ready")
#     print("Travel")
#     print("Data analytics class")

# DA_Class()
# DA_Class()

# def Attendance(name):
#     print("Present", name)

# Attendance("Moorthi")
# Attendance("Prakash")
# Attendance("Sanjay")


# def func1(a):
#     print(a)

# def func2(b):
#     return b

# a = func1(5)
# b = func2(7)

# print("A", a)
# print("B", b)

# With argument with return

# def add(a,b):
#     return a+b


# a = add(5,7)
# b = add(25,17)

# print("a",a)
# print("b",b)

# without argument with return

# def num():
#     a = 2
#     b = 3

#     return a+b

# n = num()

# print("n",n)
    
# without argument without return

# def num():
#     a = 2
#     print("a",a)

# x=num()
# print("x",x)







# a = 4
# b = 8

# def add():
#     print("Addition", a+b)

# print("add",add())

# with argument without return

# def attendanance(summaname):
#     print(f"Present {summaname}")

# attendanance("Naslin")



#March and June

# Tuple - ()

# Ordered, duplicates allowed, indexed, Not mutable

# weeks = ("Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "sun")


# l = ["FSD", "DM", "DA", "DS"]
# l2 = list(["FSD", "DM", "DA", "DS"])

# dob = ("Jan",)
# d1 = tuple([1])


# print("type", type(d1))
# print("Month", dob[1])
# dob[1] = "Feb"
# print("min", min(weeks))
# print("max", max(weeks))
# print("Len", len(weeks))
# print("dob", dob)

# date,month,year = dob

# print("Date", date)
# print("Month", month)
# print("Year", year)


#Set

# s = {}
# unordered, duplicate values not allowed, mutable

# l = [12, 22, 32, 42, 52]

s = {12, 22, 32, 42, 52, 52, 22, 42}

# s.add(62)
# s.remove(52)
# print("l", l)
# print("s", s)

# attendance = {"Rooban", "Vasanthi", "Hari", "Absent", "Joel", "Keerthika", "Vasanthi", "Rooban", "Absent"}

# present_list = []

# # print("Attendanance", attendance)

# for a in attendance:
#     if(a == "Absent"):
#         continue
#     else:
#         present_list.append(a)

# print("Present students list", present_list)

# s1 = {"FSD", "DA", "DM", "AIFSD", "AIDA"}
# s2 = {"FSD", "AIDA", "DS", "DEVOPS", "TESTING"}

# print("Diff-s1", s1-s2)
# print("Diff-s2", s2-s1)

#print("Union", s1 | s2) #s1.union(s2)
# print("Intersection", s1 & s2) #s1.intersection(s2)
#print("Symmetric difference", s1^s2) # (s1.union(s2)) - (s1.intersection(s2))

#  {'DEVOPS', 'AIDA', 'TESTING', 'FSD', 'DM', 'AIFSD', 'DA', 'DS'} - {"FSD", "AIDA"} =  {'DEVOPS', 'TESTING', 'DM', 'AIFSD', 'DA', 'DS'}



password = input("Enter your password: ")
is_numeric = 0
is_upper = 0

if(len(password) > 8):
    for p in password:
        if p >= "A" and p <= "Z":
            is_upper +=1
        if p >= "0" and p<= "9":
            is_numeric+=1


if(is_upper > 0 and is_numeric > 0):
    print("Password strong")
else:
    print("Password weak")