# # file = open("file.txt", "r")
# # c = file.read()
# # # file.close()
# # print("data",c)


# with open("file.txt", "r") as file:
#     c = file.read()
#     print("c", c)


# file = open("file.txt", "w")

# file.write("\n Programming")

# file.close()

# file = open("file.txt", "a")

# file.write("\n New added data")

# file.close()

# with open("newfile.txt", "x") as file:
#     print("file", file)

# source = open("image.png", "rb")
# data = source.read()
# source.close()


# copy = open("copy.jpg", "wb")
# copy.write(data)
# copy.close()


# with open("file.txt", "r") as file:
#     print(file.readline())
#     print(file.readline())

# with open("file.txt", "r") as file:
#     lines = file.readlines()
# print(lines)

# with open("file.txt", "r") as file:
#     for line in file:
#         print(line.strip())


# file pointer

# with open("file.txt", "r") as file:
#     file.read(2)
#     file.seek(0)
#     print(file.tell())


# with open("file.txt", "r") as file:
#     file.read(2) 
#     current_pos = file.tell()
#     remaining_content = file.read() 
#     print(f"I am at position: {current_pos}")
#     print(f"Remaining text is: '{remaining_content}'")


try:
    with open("abc.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")


# file = open("file.txt", "r")
# for i in file:
#     print(i)