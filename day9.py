# def multiply(*numbers):
#     print("numbers", numbers)

# multiply(87, 97, 27)

# def values(**fields):
#     print("fields", fields)

# values(name = "Vj", age = "53")


#map

# l = [1, 2, 3, 4, 5]
# l2 = []
# for i in l:
#     i = i*2
#     l2.append(i)

# print("List", l2)

# map(functions, iterations)

# li = list(map(lambda l:l*2, l))

# def multiply(l):
#     return l*2

# li = list(map(multiply,l))

# print("List", li)



# price = [100, 130, 200, 270]

# def gst(x):
#     return x*0.18 + x

# m = list(map(lambda price:(price*0.18)+price, price))
# m = list(map(gst, price))

# print("m",m)



# filter

# l = [1, 2, 3, 4, 5, 6, 8, 9]

# even = list(filter(lambda x: x%2 == 0 ,l))

# print("Even", even)


# l = [1,2,3,5,10]


# result = list(map(lambda x: x**2, filter(lambda x: x%2 == 0, l)))

# print("res", result)



# l = [10, 20, 30, 40]

# l2 = []

# for i in l:
#     l2.append(i*2)



# l2 = list(map(lambda i:i*2, l))3
# print(l2)



# March and june

# map and filters

# ecom_products = [700, 600, 500, 323, 876, 950]

# map(functions, iterations)

# def discount(amount):
#     return amount-100

# discount_price = list(map(discount, ecom_products))

# print("original price", ecom_products)

# print("discounts", discount_price)


# salary = [50000, 80000, 40000, 67000, 54000]

# def salary_hike(salary_amount):
#    return salary_amount + salary_amount*0.0

# new_salary = list(map(salary_hike, salary))

# print("new salary", new_salary)


# filter

# student_marks = [80, 95, 67, 47, 32, 35, 39]

# def pass_students(marks):
#     return marks >= 35


# def pass_students(marks):
#     if(marks >= 35):
#         return marks


# filter(functions, iterations)

# passed_students = list(filter(pass_students, student_marks))

# print("pass", passed_students)


# s = {'key':[40, 70], 'key2':[40, 70]}

# def cond(c):
#     print("key",s[c])
        

# r = list(map(cond, s))

# print("r", r)

student_name = input("Enter student name: ")

students_marks = { 'Vasanthi': [89, 95, 97, 92, 91],'Joel': [92, 82, 91, 99, 90], 'Logesh': [81, 93, 94, 87, 96]}

def mark_list(name):
    # name = ('Joel', [92, 82, 91, 99, 90])
    key = name[0]
    value = name[1]
    if(key == student_name):
      return True
    # return False

students_marks_list = list(filter(mark_list, students_marks.items()))

print("Mark list: ", students_marks_list[0][1])
# print("Mark list: ", students_marks.items())


# l = [90, 90, (100 , 50, 70), 80]

# print("list", l[::-4])