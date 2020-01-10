# # int,float,double,string,char,boolean,complex

# a = 5
# print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))
print(a,"is float numbrt",isinstance(a,int))

a = 1+2j
print(a,"is of type",type(a))

print(a, "is int number?", isinstance(a,int))


import anu_constant as const

print(const.PI)
print(const.GRAVITY)

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

print(a, b, c, d)

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

print(float_1, float_2)

j = aa = u"I ♥ U" 

k = u"\U0001f638"
print(j)
print(k)

flag = u"\u2691"

print(flag)



a = [5,10,15,20,25,30,35,40]

print(a[1:9:2])


