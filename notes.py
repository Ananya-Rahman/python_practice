# if 1<2:
#     print("First Block")
#     if 20< 3:
#         print("Second block")

# cars = ["audi","bmw", "subaru", "toyota"]
# for car in cars:
#     if car == "bmw":

#         print(car.upper())
#     else:
#         print(car.title())

# if 1 == 1:
#     if 1 > 2:
#         print("hello")
#     elif 3 == 3:
#         print("elif ran")
#     else:
#         print("last")






#####For Loops#####
seq = [1,2,3,4,5,6]
for item in seq:
    print(item)


d = {"Sam":1,"From":2,"Dan":3}
for k in d:
    print(k)
    print(d[k])

myPairs = [(1,2),(3,4),(5,6)]
for tup1,tup2 in myPairs:
    print(tup2)
    print(tup1)

i = 1
while i < 5:
    print("the number is: {}".format(i))
    i = i +1

##List Comprehension
x = [1,2,3,4]
out = []
for num in x:
    out.append(num*2)
print(out)










