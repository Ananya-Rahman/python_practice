

# x = 25
# def myFunc():
#      x = 50
#      return x

# print(x)
# print(myFunc())

#Enclosing function name

# name = 'This is a global name!'

# def greet():
#     name = "Sammy"

#     def hello():
#         print("hello "+name)
#     hello()
# print(name)
# greet()

# x = 50
# def func(x):
#     print("x is: ", x)
#     x= 1000
#     print("Local x is changed to", x)
# print(func(x))

x= 50

def func():
    # global x
    x = 1000
    return x

print("before function call, x is", x)
x = func()
print("After function call x is ", x)



