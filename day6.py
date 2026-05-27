# Tuple - () - immutable and ordered

t = ('mon', 'tue', 'wed', 'thurs', 'fri', 'sat', 'sun')

# print("tuple", t[0])
# print("Index", t.index('tue'))
# print("length", len(t))
# print("min", min(t))
# print("max", max(t))
# print("count", t.count("tue"))

# day1, day2, day3, day4, day5, day6, day7 = t

# print("Day1", day1)

# l = [99] or list([99])

# tu = tuple('name')

# print("list", type(l), "tu", type(tu), "t",type(t))






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

s1 = {'a', 'b', 'c', 'd', 'e'}
s2 = {'a', 'e', 'i', 'o', 'u'}

print("Difference1:", s1-s2)
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

