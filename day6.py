


# Tuple - () - immutable and ordered

# t = ('mon', 'tue', 'wed', 'thurs', 'fri', 'sat', 'sun')

# print("tuple", t[0])
# print("Index", t.index('tue'))
# print("length", len(t))
# print("min", min(t))
# print("max", max(t))
# print("count", t.count("tue"))
# print(type(t))

# day1, day2, day3, day4, day5, day6, day7 = t

# print("Day1", day1)

# l = [99] or list([99])

# tu = tuple('name')

# print("list", type(l), "tu", type(tu), "t",type(t))


# t1 = ('mon',)

# print(type(t1))







# t = ('mon',)

# print("tuple", t)
# print("type", type(t))


# Set - {} - unordered and not allowed duplicates

s = {2, 8, 9, 10, 3, 2, 3, 3}
# s.add(20)

# s = set({2, 8, 9 ,10, 3})

# numbs = [10, 20 ,30]

# print("In or not:",20 not in s)

# print("set", s)
# print("set", len(s))
# print("min", min(s))
# print("max", max(s))
# print("type", type(s))


# membership operators - in, not in

# s1 = {'a', 'b', 'c', 'd', 'e'}
# s2 = {'a', 'e', 'i', 'o', 'u'}

# print("Difference1:", s1-s2)
# print("Difference2:", s2-s1)

# print("Union:", s1 | s2)
# print("Union:", s1.union(s2))

# print("Interection:", s1 & s2)
# print("Interection:", s1.intersection(s2))

                                        # {'a', 'b', 'c', 'd', 'e', 'i', 'o', 'u'} - {'a', 'e'}
# print("Symmetric difference", s1^s2)  #(s1 union s2) - (s1 intersection s2)
# print("Symmetric difference", s1.symmetric_difference(s2))


# Dictionary - key and values

# data = {'name':'yogesh'}

# print("data", data["name"])
# print("data", data.get("name"))


# For loops

# i = 1

# while(i < 11):
#     print("i",i)
#     i+=1

# for i in range(11):
#     print("i", i)

# for i in range(0, 21):
#     print("i",i)

# i=0

# while(i<=20):
#     # i+=2
#     if(i%2 == 0):
#         print("Even numbers: ",i)
#     i+=2


# for i in range(0, 21, 2):
#     print("Even: ", i)

# for i in range(10, 0, -1):
#     print("Count down", i)


#Collection data types:

# list

#ordered, mutable, duplicates allowed

# l = [ "Laptop", "bag", "mouse", "pendrive", "Laptop"]
# l2 = [13,32,86,4,87, 55,76]

# marks = [98, 95, 99, 100, 89]

# print("percentage", (sum(marks)/500)*100)

# print("l", l)
# print("lists", l[0])
# l.append("cable")
# l.insert(1,"tv")
# l[1] = "School bag"
# l.remove("bag")
# l.pop(3)
# print("lenght",len(l))
# print("min", min(l2))
# print("max", max(l2))
# print("sum", sum(l2))
# print("length", len(l2))
# print("Average", sum(l2)/len(l2))

# print("min",min(l))
# print("max",max(l))



# print("lists",l)



#membership operators

# in
# not in

amazon_cart_list = [ "laptop", "bag", "mouse", "pendrive"]

search = input("Enter your search product: ")

if(search not in amazon_cart_list):
    print(f"{search} doesnt exist. Please add the product")
# else:
#     print(f"{search} doesnt exist. Please add the product")

