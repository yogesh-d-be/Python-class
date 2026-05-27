# import numpy as np

# marks = np.array([85, 90, 78, 92])

# print(marks)


# # Array Properties

import numpy as np

# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
#     ])


# print(arr.ndim)
# print(arr.shape)#find rows and columns
# print(arr.size)
# print(arr.dtype)


# # Array Creation Methods
# np.zeros()
# a = np.zeros((2,3))


# np.ones()
# a = np.ones((2,2))

# np.arange()
# a =np.arange(2, 10, 2)


# np.linspace()
# a = np.linspace(0, 1, 5)


# np.random
# a = np.random.randint(1, 100, 5)
# print("Arr",a)


# # Array Indexing and slicing

# arr = np.array([10, 20, 30])

# print(arr[0])

# print(arr[-1])

# print(arr[0:2])

# # 2D Indexing
# data = np.array([
#     [10,20,30],
#     [40,50,60]
# ])

# print(data[1,2])

# print(data[0])#rows

# print(data[:,1])#columns



# # Array Operations
# # Arithmetic Operations
# arr = np.array([1,2,3])

# print(arr + 5)


# salaries = np.array([30000, 40000, 50000])

# updated = salaries * 1.10


# l = [10, 20, 30]

# l1 = []

# for i in l:
#     i = i*2
#     l1.append(i)

# print("list", l1)


# import numpy as np

# a = np.array([10, 20, 30])
# print("arr",a*2)


# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# print(arr[0])

# print("slice", arr[3:6])
# print("slice", arr[-6:-3])

# data = np.array([
#     [10,20,30],
#     [40,50,60]
# ])

# print(data[1][2])
# print(data[-1][-2])
# print(data[1])
# print(data[:,1])

l = np.array([100, 220, 350])
print(l*1.18)
