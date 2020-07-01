x = lambda y : y + 10 
print(x(3)) 

###multiple function###

x = lambda a, b: a * b
print(x(3,5))

x = lambda a,b,c : a+b+c 
print(x(2,3,7))

tweet = "Go Sports! #Sports"
result = tweet.split('#')
print(result)

def myfunc(n):
    return lambda a: a * n
myDoubler = myfunc(2)
print(myDoubler(11))

def myfunc(n):
    return lambda a : a*n

mydoubler =myfunc(2)
mytripler =myfunc(3)

print(mydoubler(11))
print(mytripler(11))


