#arguments
def greet(name,msg):
    print("hello",name+','+msg)
greet("monica","good morning")


#####Function#####
def my_func(param1='default'):
    print("my first python function!!")

my_func()
# Arguments are specified after the function name,
#  inside the parentheses. You can add as many arguments as you want,
#  just separate them with a comma.
#here, two arguments(fname,age)
def my_function(fname,age):
    print(fname+" Refsnes "+age)
my_function("Email","20")
my_function("Tobias",'20')
my_function("Linus",'12')

def myfunc1(*kids):
    print("The youngest child is "+ kids[2])
myfunc1("email","tobias","Linus")

def myfunc2(child1,child2,child3):
    print("The younger child is " + child1)
myfunc2(child1="Email",child2="Tobias",child3="Linus")

def func(**anu):
    print("my name is "+ anu['fname'] )#using dictionary of arguments
func(fname="anonna",lname="Rahman")

###default parameter value####
def myFunc(country='Bangladesh'):
    print("I am from {}".format(country))

myFunc("India")
myFunc()
myFunc("fiji")
myFunc("paris")

##Passing a List as an Argument##
food = ["mango","jam","jery"]
def func(food):
    for x in food:
        print(x)
func(food)

##Return value###
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(30))
print(my_function(10))

####The pass Statement###

#function definitions cannot be empty, 
#but if you for some reason have a function definition with no content,
#put in the pass statement to avoid getting an error.
def my_function():
    pass


######################

def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        print("Sorry i need integers!")
addNum("2","3")
print(addNum) 


#Lamda expression

#filter function
myList = [1,2,3,4,5,6,7,8]


evens = filter(lambda num:num%2 == 0,myList)
print(evens)
print(list(evens))







