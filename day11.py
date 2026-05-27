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


import csv

students = [
    {"name": "John", "mark": 90},
    {"name": "Asha", "mark": 95}
]

with open("students.csv", "w", newline="") as file:
    fields = ["name", "mark"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)





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