# # import numpy as np

# # marks = np.array([85, 90, 78, 92])

# # print(marks)


# # # Array Properties

# # import numpy as np

# # arr = np.array([
# #     [10, 20, 30],
# #     [40, 50, 60]
# #     ])


# # print(arr.ndim)
# # print(arr.shape)#find rows and columns
# # print(arr.size)
# # print(arr.dtype)


# # # Array Creation Methods
# # np.zeros()
# # a = np.zeros((2,3))


# # np.ones()
# # a = np.ones((2,2))

# # np.arange()
# # a =np.arange(2, 10, 2)


# # np.linspace()
# # a = np.linspace(0, 1, 5)


# # np.random
# # a = np.random.randint(1, 100, 5)
# # print("Arr",a)


# # # Array Indexing and slicing

# # arr = np.array([10, 20, 30])

# # print(arr[0])

# # print(arr[-1])

# # print(arr[0:2])

# # # 2D Indexing
# # data = np.array([
# #     [10,20,30],
# #     [40,50,60]
# # ])

# # print(data[1,2])

# # print(data[0])#rows

# # print(data[:,1])#columns



# # # Array Operations
# # # Arithmetic Operations
# # arr = np.array([1,2,3])

# # print(arr + 5)


# # salaries = np.array([30000, 40000, 50000])

# # updated = salaries * 1.10


# # l = [10, 20, 30]

# # l1 = []

# # for i in l:
# #     i = i*2
# #     l1.append(i)

# # print("list", l1)


# # import numpy as np

# # a = np.array([10, 20, 30])
# # print("arr",a*2)


# # arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# # print(arr[0])

# # print("slice", arr[3:6])
# # print("slice", arr[-6:-3])

# # data = np.array([
# #     [10,20,30],
# #     [40,50,60]
# # ])

# # print(data[1][2])
# # print(data[-1][-2])
# # print(data[1])
# # print(data[:,1])

# # l = np.array([100, 220, 350])
# # print(l*1.18)





# """
# CSV = Comma Separated Values

# student.csv

# Name,Age,Course
# Joel,22,Python
# Hari,21,Java
# Priya,23,AI

# """

# ##########################################################
# # CSV READER
# ##########################################################

# import csv

# print("=" * 50)
# print("READING CSV FILE")
# print("=" * 50)

# """
# students.csv

# Name,Age,Course
# Joel,22,Python
# Hari,21,Java
# Priya,23,AI
# """


# # with open("students.csv", "r") as file:
# #
# #     reader = csv.reader(file)
# #
# #     for row in reader:
# #         print(row)


# ##########################################################
# # ACCESSING COLUMNS
# ##########################################################



# # with open("students.csv") as file:
# #
# #     reader = csv.reader(file)
# #
# #     next(reader)          # Skip header
# #
# #     for row in reader:
# #
# #         print("Name :", row[0])
# #         print("Age  :", row[1])
# #         print("Course:", row[2])
# #         print()


# ##########################################################
# # CSV WRITER
# ##########################################################

# print("=" * 50)
# print("WRITING CSV")
# print("=" * 50)

# # with open("students.csv", "w", newline="") as file:
# #
# #     writer = csv.writer(file)
# #
# #     writer.writerow(["Name", "Age", "Course"])
# #
# #     writer.writerow(["Joel", 22, "Python"])
# #
# #     writer.writerow(["Hari", 21, "Java"])
# #
# #     writer.writerow(["Priya", 23, "AI"])


# ##########################################################
# # WRITING MULTIPLE ROWS
# ##########################################################

# students = [

#     ["Joel",22,"Python"],
#     ["Hari",21,"Java"],
#     ["Priya",23,"AI"],
#     ["Vasanthi",20,"Data Science"]

# ]

# # with open("students.csv","w",newline="") as file:
# #
# #     writer = csv.writer(file)
# #
# #     writer.writerow(["Name","Age","Course"])
# #
# #     writer.writerows(students)


# ##########################################################
# # CSV DICT READER
# ##########################################################

# print("=" * 50)
# print("DICT READER")
# print("=" * 50)

# """


# {

# 'Name':'Joel',
# 'Age':'22',
# 'Course':'Python'

# }
# """

# # with open("students.csv") as file:
# #
# #     reader = csv.DictReader(file)
# #
# #     for row in reader:
# #
# #         print(row)
# #
# #         print(row["Name"])
# #
# #         print(row["Course"])
# #
# #         print()


# ##########################################################
# # CSV DICT WRITER
# ##########################################################

# # with open("students.csv","w",newline="") as file:
# #
# #     writer = csv.DictWriter(
# #         file,
# #         fieldnames=["Name","Age","Course"]
# #     )
# #
# #     writer.writeheader()
# #
# #     writer.writerow({
# #
# #         "Name":"Joel",
# #         "Age":22,
# #         "Course":"Python"
# #
# #     })
# #
# #     writer.writerow({
# #
# #         "Name":"Hari",
# #         "Age":21,
# #         "Course":"Java"
# #
# #     })


# ##########################################################
# # JSON FILES
# ##########################################################

# """
# JSON

# JavaScript Object Notation

# Looks like Dictionary

# {
#     "name":"Joel",
#     "age":22
# }
# """

# import json

# student = {

#     "name":"Joel",
#     "age":22,
#     "course":"Python",
#     "city":"Chennai"

# }

# ##########################################################
# # WRITE JSON
# ##########################################################

# # with open("student.json","w") as file:
# #
# #     json.dump(student,file,indent=4)


# ##########################################################
# # READ JSON
# ##########################################################

# # with open("student.json") as file:
# #
# #     data = json.load(file)
# #
# #     print(data)
# #
# #     print(data["name"])
# #
# #     print(data["course"])


# ##########################################################
# # OTHER FILE TYPES
# ##########################################################

# """
# TXT

# open("student.txt")

# CSV

# csv module

# JSON

# json module

# Excel

# openpyxl

# PDF

# PyPDF2

# Images

# rb mode

# Videos

# rb mode

# Audio

# rb mode
# """


# ##########################################################
# # EXCEL
# ##########################################################

# """
# Install

# pip install openpyxl
# """

# # from openpyxl import load_workbook
# #
# # workbook = load_workbook("students.xlsx")
# #
# # sheet = workbook.active
# #
# # print(sheet["A1"].value)


# ##########################################################
# # IMAGE
# ##########################################################

# """
# rb = Read Binary

# Images contain bytes.

# Not normal text.
# """

# # with open("photo.jpg","rb") as file:
# #
# #     image = file.read()
# #
# #     print(image[:100])


# ##########################################################
# # EXCEPTION HANDLING
# ##########################################################

# print("=" * 50)
# print("EXCEPTION HANDLING")
# print("=" * 50)

# """
# Without Exception

# Program crashes.

# With Exception

# Program handles errors gracefully.
# """

# ##########################################################
# # SIMPLE TRY EXCEPT
# ##########################################################

# # try:
# #
# #     number = int(input("Enter Number : "))
# #
# #     print(100 / number)
# #
# # except:
# #
# #     print("Something went wrong")


# ##########################################################
# # SPECIFIC EXCEPTION
# ##########################################################

# # try:
# #
# #     number = int(input("Enter Number : "))
# #
# #     print(100 / number)
# #
# # except ValueError:
# #
# #     print("Please enter only numbers.")
# #
# # except ZeroDivisionError:
# #
# #     print("Number cannot be zero.")


# ##########################################################
# # ELSE
# ##########################################################

# # try:
# #
# #     age = int(input("Enter Age : "))
# #
# # except ValueError:
# #
# #     print("Invalid Age")
# #
# # else:
# #
# #     print("Age Saved Successfully")


# ##########################################################
# # FINALLY
# ##########################################################

# # try:
# #
# #     file = open("students.txt")
# #
# # except FileNotFoundError:
# #
# #     print("File Not Found")
# #
# # finally:
# #
# #     print("Program Finished")


# ##########################################################
# # EXCEPTION OBJECT
# ##########################################################

# # try:
# #
# #     open("abc.txt")
# #
# # except FileNotFoundError as error:
# #
# #     print(error)


# ##########################################################
# # RAISE EXCEPTION
# ##########################################################

# # age = int(input("Enter Age : "))
# #
# # if age < 18:
# #
# #     raise ValueError("Age must be above 18")
# #
# # print("Registration Successful")



# """



# March and June

# csv

# with open("students.csv") as file:
#     print("file", file.read())


# import csv

# with open("students.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print(row)
        # print("Mark column", row[1])
        # print("City column", row[2])



# with open("da-students.csv", "w", newline="") as file:
#     writer = csv.writer(file)

    # writer.writerow(["Name", "Age", "City"])
    # writer.writerows([["Name", "Age", "City"], ["Yo", "18", "Chennai"]])


# with open("students.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row)
        # print("Name", row['Name'])
        # print("Name", row.get('Name'))
        # print("Mark", row[])
        # print("City", row[])

# students = [
#     {'Name': 'John', 'Mark': '90', 'City': 'Chennai'},
# {'Name': 'Asha', 'Mark': '95', 'City': 'Madurai'},
# {'Name': 'Rahul', 'Mark': '85', 'City': 'Coimbatore'}
# ]

# with open("da-students.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["Name", "Mark", "City"])
    # writer.writerow({'Name': 'John', 'Mark': '90', 'City': 'Chennai'})
    # writer.writerows(students)
    


# json

# student = {
#     "Name": "Yogesh",
#     "Mark":90,
#     "Comment":{
#         "account" : "Keerthika",
#         "Comment": {
#             "message":  "Class is boring 😴",
#              "Like" : "Joel",
#         "Reply":"Yes sir. class is sleepy"
#         }
       
       
#     } 
# }

# import json

#write
# with open("students.json", "w", encoding="utf-8") as file:
#     json.dump(student,file,indent=4)

#read
# with open("students.json", "r") as file:
#     print(json.load(file))


# l = [89, 77, 55, 88, 65, 60]

# s = sorted(l, reverse="True")

# # print("s", s)

# # i = len(l) - 2

# print("Second largest", s[""])
# s = [8, 9, 7]
# if(s):
# print("*"*10)
# else:
#     print("Bye")
# a = "50"
# b = 10
# print(a+b)

# a = input("Enter: ")
# b = input("Enter")

# c = a+b

# print("c", c)

# print("-"*10)

# def fun():
#     return 10

# a = fun()

# print("a value is ", a)


# text = "python programming"

# print(text.title())
# print(text.count("m"))


# for i in range(1,10):
#     if(i == 5):
#         continue
#     print(i)

# a = int(input("Enter a value: "))
# b = int(input("Enter b value: "))

# def add(x,y):
#     return x+y

# print(add(a, b))


# a = int(input("Enter a value: "))

# if(a%2 != 0):
#     print("Odd")
# else:
#     print("Even")


# student_name = input("Student name: ")
# total_subject = int(input("Enter subject count: "))
# end_range = total_subject+1

# marks = []

# for i in range(1, end_range):
#     marks_input = int(input(f"Enter {i}st mark value: "))
#     marks.append(marks_input)

# total = sum(marks)
# average = total/total_subject

# print("average", average)

# if(average >= 90):
#     print("A Grade")
# elif(average >= 80 and average <= 89):
#     print("B Grade")
# elif(average >= 70 and average <= 79):
#     print("C Grade")
# elif(average < 70):
#     print("Fail")
# else:
#     print("Invalid")


# sentence = "Data analytics"

# ch_c = len(sentence)
# w_c = len(sentence.split(" "))

