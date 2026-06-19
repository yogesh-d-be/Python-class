# i = 0

# while i < 10:
#     print(i)
#     i+=1 # i = i+1
#     if(i==5):
#         break

# i = 0

# while i < 10:
#     i+=1 # i = i+1
#     if(i==5):
#         continue
#     print(i)


# collection data types
# lists - mutable, duplicate values allowed, ordered

l = [65, 87, 97, 37, 87, 27, 87]

# print("Index", l[-4])

# l[0] = 67

# l.append(27)

# l.insert(1, 17)

# l.remove(87)

# l.pop()
# l.pop(-2)
# print("Slice",l[-3:])
# del l[2:]
# l.extend([57, 47, 27])
# print("length",len(l))

# print("Count", l.count(87))

# print("Min",min(l))
# print("Max",max(l))
# print("Sum", sum(l))

# print("Average", sum(l)/len(l))

# print("l",l)



# a = int(input("Enter your marks in tamil: "))
# b = int(input("Enter your marks in english: "))
# c = int(input("Enter your marks in maths: "))
# d = int(input("Enter your marks in science: "))
# e = int(input("Enter your marks in social: "))

# marks = []

# for i in range(5):
#     score = int(input(f"Enter marks {i+1}: "))
#     marks.append(score)
# print("Marks", marks)



# print("marks", marks)
# print("total", sum(marks))
# l.pop(0)





# print("Average", sum(l)/len(l))
# l.reverse()
# print("reverse", l)

# print("Lists", l)

# for i in l:
#     print(i)

# l1 = int(input("Enter a number1:"))
# l2 = int(input("Enter a number2:"))
# l3 = int(input("Enter a number3:"))
# l4 = int(input("Enter a number4:"))
# l5 = int(input("Enter a number5:"))

# l = [l1, l2, l3, l4, l5]

# print("List", l)

# inputCount = int(input("Enter a input count:"))

# i = 1
# li = []

# for i in range(inputCount):
#     val=int(input(f"Enter a number{i}:"))
#     li.append(val)

# print("Lists",li)



# age is below 18 Not eligible for vote
# age is above 18 Eligible
#     18-59 eligible but second priority
#     above 60 eligible but first priority

# count of below 18, 18-59, above 60 and total members


# ages = [12, 17, 18, 25, 40, 59, 60, 75, 16, 22, 61]

# i = 0

# while i<5:
#     print("value:",i)
#     i+=1

# for i in range(1,7):
#     print(i)


#March and June

# if(condition):
#     statements

# remote_signal = input("Is remoted triggered or not: (y/n): ")

# if(remote_signal.lower() == "y" or remote_signal.capitalize() == "Yes"):
#     print("Door open. Students get in")
# else:
#     print("Remote signal is not detected. You cant get in")


# remote_signal = input("Is remote signal triggered or not? (Y/N): ")

# if(remote_signal.lower() == "y" or remote_signal.lower() == "yes"):
#     print("Door open")
# elif(remote_signal.lower() == "n" or remote_signal.lower() == "no"):
#     print("Door not open")
# else:
#     print("Remote may be missed.")




    # 16 -22 ---> cool
    # 23 - 28 ---> normal
    # 29 - 31 ---> warm
    # 32 , above 32 ---> hot


    # Loops

    # while(condition):
    #     statements


# i = 1

# while(i < 11):
#     print("Number: ",i)
#     i += 1



# attempt = 0
# max_attempts = 3

# while(True):
#     password = input("Enter your password: ")
#     if(attempt != max_attempts and password == "123"):
#         print("Login successful")
#         break
#     elif(attempt == max_attempts):
#         print("You are reach maximum attempts")
#         break
#     else:
#         attempt += 1
#         print("Try again")




# attempt = 0
# max_attempts = 3
# loop_status = True

# while(True):
#     password = input("Enter your password: ")
#     if(attempt != max_attempts and password == "123"):
#         print("Login successful")
#         break
#     elif(attempt == max_attempts):
#         print("You are reach maximum attempts")
#         break
#     else:
#         attempt += 1
#         print("Try again")