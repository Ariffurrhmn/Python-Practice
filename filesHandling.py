# f = open("test.txt") #Opens file

# text = f.read()  #Reads the entire file

# print(type(text)) #Prints type of file

# print(text) #Prints everyrhing inside text

# f.close() #Closes file


# f = open("test.txt")
# txt = f.read(10)
# print(type(txt))
# print(txt)
# f.close()

# f = open("test.txt")
# line = f.readline()
# print(type(line))
# print(line, end = "")
# f.close()


# f = open("test.txt")
# lines = f.readlines()
# print(type(lines))
# print(lines)
# f.close()


# class Open_File():

#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
    
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.file.close()

# with Open_File('test.txt', 'w') as f:
#     f.write("Testing")

# print(f.closed)

# from contextlib import contextmanager

# @contextmanager
# def open_file(file, mode):
#     f = open(file, mode)
#     yield f
#     f.close()

# with open_file('test.txt','w') as f:
#     f.write("Lorem Ipsum")

# print(f.closed)


# with open('test.txt') as f:
#     lines = f.read().splitlines()
#     print(type(lines))
#     print(lines)

# with open('test.txt', 'a') as f:
#     f.write("New line")


# with open("newtest.txt", 'w') as f:
#     f.write("Create a new note and write this")

# with open("example.txt", 'w') as f:
#     f.write("Create a new note and write this")

# import os
# if os.path.exists("example.txt"):
#     os.remove("example.txt")
# else:
#     print("File does not exist")


