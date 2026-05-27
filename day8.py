# numbs = [1,2,3,4,5]

# cal = list(map(lambda x:x*x, filter(lambda x: x%2 == 0, numbs)))

# print("cal", cal)


# users = [
#     {"name": "A", "marks": 80, "active": True},
#     {"name": "B", "marks":40, "active": False}
# ]

# res = list(filter(lambda u: u["active"] and u["marks"]> 79, users))

# print("res", res)


# products = [
#     {"name": "A", "price": 100},
#     {"name": "B", "price": 500},
#     {"name": "C", "price": 50}
# ]

# # Task:
# # 1. Filter price > 100
# # 2. Apply 10% discount
# # 3. Return final prices

# price = list(filter(lambda p: p["price"] > 100, products))
# dis = list(map(lambda d: d["price"]-(d["price"]*0.1), products))

# lambda expression: condition statements

# def num(x):
#     a = x**2
#     return a

# b = num(3)
# print("Square",b)

square = lambda x,y: (x**2, y**3)
a = square(3, 2)
print("Square", a)