# A tuple in Python is similar to a list. 
# The difference between the two is
#  that we cannot change the elements of a 
# tuple once it is assigned whereas, in a list, 
# elements can be changed.

#empty tuple
my_Tuple = ()
print(my_Tuple)

#touple hav integer
my_Tuple = (1,2,3)
print(my_Tuple)

#touple have multiple datatypes
my_Tuple = (1, "hello" , 4.5)
print(my_Tuple)

#nested tuple
my_Tuple = (1, "mouse", [1,2,3,4], (4,5,6,7),{"name":"anu"})
print(my_Tuple)

my_Tuple = 3, 4.5, "dog"
print(my_Tuple)

#tuple unpacking also possible
a, b, c = my_Tuple
print(a)
print(b)
print(c)

my_Tuple = ("hello")
print(type(my_Tuple))
my_Tuple = "helllo",
print(type(my_Tuple))
my_Tuple = ("hello",)#buji ne vlo
print(type(my_Tuple))

my_Tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_Tuple[0])
print(my_Tuple[5])

n_tuple = ("mouse", [8,8,9], (1,3,5,6))
print(n_tuple[0][3])
print(n_tuple[1][2])
print(n_tuple[2][2])

my_tuple = ('p','e','r','m','i','t')
print(my_Tuple[-1])
print(my_Tuple[-5])

#slicing
my_Tuple = ('p','r','o','g','r','a','m','i','z')
print(my_Tuple[1:4])
print(my_Tuple[:-7])
print(my_Tuple[7:])


#changging a tuple buji ne

#Tuple Membership Test
my_tuple = ('a','p','p','l','e',)
print('a' in my_tuple)
print('g' in my_tuple)
print('h' not in my_tuple)











































