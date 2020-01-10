
# for i in range(10,-1,-1):  # range(start_point,ag_porjonto,step_increase or decrease)
#     print(i)

# for i in range(0,11):  # range(start_point,ag_porjonto,step_increase or decrease)
#     print(i)


# jdi 1 theke 10 prjonto print krte chau,,thle eta hbe ,, i=1 ; i<11 ; i++

# while True:
#     n = int( input("Enter Number "))

#     if n < 0:
#         break

#     else: print(n)

# anu swe

names = ("anu",'simu','shubro','j')
# print(len(names))

# for i in range(len(names)):
#     print(names[i] + ' swe ')


# for i in names:
#     print(i)

#informations = {'name':'anu','age':22 , 'dept':'swe'}

# print(informations['name'])
# print(informations['age'])
# print(informations['dept'])



# for key in informations:
#     print( informations[key])


# for val in informations.values():
#     print(val)

# print()
# for k in informations.keys():
#     print(k)

# numbers = [6, 51]
# sum = 0
# for val in numbers:
#     sum = sum+val
# print("sum is: ",sum)

#print(list(range(2, 20, 3)))#buji ne

# genre = ['pop', 'rock', 'jazz']

# for i in range(len(genre)):
#     print("i like", genre[i])

#fruits = ["APPLE","banana","chery","graps"]
# # # for x in fruits:
# # #     print(x)
# # for x in fruits:
# #     print(x)
# #     if(x == "banana"):
# #         break

#continue group
# for x in fruits:
#     if x == "chery":
#         continue
#     print(x)

# for x in range(6):
#     print(x)
# else:
#     print("finally finished:")
    
#adj
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#     #print(x)
#     for y in fruits:
#         print(x,y)

# for x in range(3,8,2):
#     print(x)

# count = 0
# while count < 5:
     
#      print(count)
#      count = count+1

#count = 0
# while True:
#      print(count)
#      count = count +1
#      if count>=5:
#           break

# for x in range(10):
#      if x % 2 == 0:
#           continue
#      print(x)

count = 0
while(count<5):
    print(count)
    count = count + 1
else:
    print("count value reached %d" %(count))#buji ne

for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")#buji ne

  