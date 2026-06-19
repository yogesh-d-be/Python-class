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



# l2 = list(map(lambda i:i*2, l))
# print(l2)