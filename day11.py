# import csv

# with open("students.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# import csv

# with open("students.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)


# import csv

# data = [
#     ["name", "mark"],
#     ["John", 90],
#     ["Asha", 95]
# ]

# with open("marks.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)


# import csv

# students = [
#     {"name": "John", "mark": 90},
#     {"name": "Asha", "mark": 95}
# ]

# with open("students.csv", "w", newline="") as file:
#     fields = ["name", "mark"]
#     writer = csv.DictWriter(file, fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(students)





# import json

# student = {
#     "name": "John",
#     "age": 22,
#     "skills": ["Python", "React"]
# }

# with open("student.json", "w") as file:
#     json.dump(student, file, indent=4)


# import json

# with open("student.json", "r") as file:
#     data = json.load(file)

# print(data)


# # pip install openpyxl

# from openpyxl import Workbook

# wb = Workbook()

# sheet = wb.active

# sheet["A1"] = "Name"
# sheet["B1"] = "Mark"

# sheet.append(["John", 90])
# sheet.append(["Asha", 95])

# wb.save("students.xlsx")


# from openpyxl import load_workbook

# wb = load_workbook("students.xlsx")

# sheet = wb.active

# for row in sheet.iter_rows(values_only=True):
#     print(row)



#March and june

# File Handling

# modes

# r - read
# w - write
# a - append
# x - create


# file = open("studentslist.txt", "x")

# file = open("studentslist.txt", "w")
# file = open("student.txt", "w")

# file.write("Rooban")

# file.close()


# with open("studentslist.txt", "w") as file:
#     file.write("Joel")


# students = ["Rooban\n", "Joel\n", "Hari\n"]

# with open("studentslist.txt", "w") as file:
#     file.writelines(students)


# with open("studentslist.txt", "a") as file:
#     file.write("Priya")


# with open("studentslist.txt", "r") as file:
#      print(file.read())
    #  print(file.readline())
    # #  print(file.readline(4))
    #  print(file.readlines())

# with open("studentslist.txt", "r") as file:
#     line = file.readlines()

# print("Before line", line)

# line.insert(3, "Vasanthi\n")

# print("After line", line)

# with open("studentslist.txt", "w") as file:
#     file.writelines(line)


# file pointer

# with open("studentslist.txt", "r") as file:
#     print(file.read(2))
#     file.seek(2)
#     print(file.read())
#     print(file.tell())


# with open("file.txt", "r") as file:
#     file.read(2) 
#     current_pos = file.tell()
#     remaining_content = file.read() 
#     print(f"I am at position: {current_pos}")
#     print(f"Remaining text is: '{remaining_content}'")



with open("studentslist.txt", "w", encoding="utf-8") as file:
    file.write("😂")
