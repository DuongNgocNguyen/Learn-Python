#Ký tự escape
# \n, \b, \r, \t, \a
# \\, \', \"
# \0x00
name1 = "Nguyen Van A"
name2 = 'Nguyen Van B'
name3 = '''Nguyen Van C'''
name4 = 'I\'m a .NET Developer'
path = "C:\\Users\\Public\\Documents"

""" 
Which is a string or comment in Python?
Yes, it is comment.
"""

def print_info(name, age):
    '''
    This function prints the name and age of a person.
    '''
    print(f"Name: {name}, Age: {age}")



#print_info("Nguyen Van A", 30)

#Index(chỉ mục) tăng từ trái sang phải, giảm từ phải sang trái
greet = "Hello, World!"
#print(greet[0])  # H
#print(greet[-1])  # !

# Loop (vòng lặp): for, while
# for x in greet: #enumerator
#     print(x, end="")
# print("")

# range(len(greet)): 0 -> len(greet):13 - 1
# range(1, len(greet)): 1 -> len(greet):13 - 1
# range(len(greet), 0, -2): 0 -> len(greet):13 - 1 -> i=13 11 9 7 5 3 1
# for i in range(len(greet)): # 0 -> len(greet):13 - 1
#     print(greet[i], end="")

# Kiểm tra chuỗi
# if "Hello" in greet:
#     print("Yes")
# else:
#     print("No")
    
# print("Yes") if "Helloo" in greet else print("No")

# Slicing String(Cắt chuỗi)
greet = "hello World"
# hello = greet[0:5]
# world = greet[-5:]
# print(hello)
# print(world)

# print(greet.lower())
# print(greet.upper())
# print(greet.capitalize())
# print(greet.title())


another_string = "       Hello World          "
# print(another_string.strip()) # loại bỏ khoảng trắng
# print(another_string.lstrip()) # loại bỏ khoảng trắng bên trái
# print(another_string.rstrip()) # loại bỏ khoảng trắng bên phải
# print(another_string.replace('o', 'A', 1))
print(another_string.split(' '))