# lambda arguments: expression

salary = [60000, 45000, 67000, 71000, 96000]

# def hike(amount):
#     return amount+ amount*0.3

# # new_salary = list(map(hike, salary))
# new_salary = list(map(lambda amount: amount+amount*0.3, salary))


# def hike(amount):
#     return amount+ amount*0.3

# salary_hike = lambda amount: amount+amount*0.3


# new_salary = list(map(hike, salary))
# new_salary = list(map(salary_hike,salary))

# print("new salary", new_salary)
# print("hike", hike(10000))
# print("s.hike", salary_hike(10000))



even = [100, 201, 83, 95, 98, 200]

# def even_num(e):
#     if(e % 2 == 0):
#         return "Even"
#     else:
#         return "Odd"


# even_num = lambda e: "Even" if(e%2 == 0) else "Odd"

# odd_or_even = list(map(even_num, even))

# print("Number is", even_num(201))
# print("Odd or even", odd_or_even)


# sorted

# name = ["Logesh", "Rooban", "Yogesh", "Hari", "Joel"]

# price = [89, 7889, 3283, 3, 90, 866]

# student_marks = {
#     "Logesh": 89,
#     "Kani": 88,
#     "Keerthika": 83
# }

# print("Keys", student_marks.keys())
# print("values", student_marks.values())
# print("Items", student_marks.items())

# name = [ "Kani", "Joel", "Logesh", "Sam"]



# print("Sorted", sorted(name, reverse=True))
# print("Sorted", sorted(name, key=len))
# print("Sorted", sorted(student_marks.items(), key=lambda m: m[1]))

# [('Logesh', 89), ('Kani', 88), ('Keerthika', 83)]


# list comprehension

# 1*2 = 2
# 2*2 = 4
# 10*2 = 20

# result = []

# for i in range(1,11):
#     m = i*2
#     result.append(m)

# print("Result", result)

# l = [i*2 for i in range(1,11)]


even = [89, 70, 45, 87, 94]

odd_or_even = []

print("even", even)

for e in even:
    if(e%2 == 0):
        odd_or_even.append("Even")
    else:
        odd_or_even.append("Odd")

even = odd_or_even
print("even 2", even)






# l = ["Even" if(e%2 == 0) else "Odd" for e in even]

# print("list", l)