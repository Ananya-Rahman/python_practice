# print('hello anu')

# myInput = input("what is your name?")
# print('my name is', myInput)

# inputAge = input("Give ur age: ")
# print('i am', inputAge , 'years old')

# inputNum = int(input("number: "))
# inputNum1 = float(input("number: "))
# sum = inputNum+inputNum1
# print('total number is: '+ str(sum))


# tuple update hyna
languageT = ("French", "French", "German", "English", "Polish")
print(languageT)

# list
languageList = ["French", "German", "English", 1,2,2, "Polish"]
languageList[0] = "Bangladesh"
print(languageList)

# set duplicate value nei na

myset = {3,  2,languageT,1}
# print(myset)

print("Set print")
for x in myset:
   print(x) 


print('\nset print with tuple : ')
for s in myset:
    if(isinstance(s, tuple)):
        for i in s:
            print(i)
    else:print(s) 


