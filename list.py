# bicycle = ['trek', 'cannadible', 'redline', 'specialized']
# print(bicycle[0].title())                    

#insert
# motorcycle = ['honda', 'yamaha', 'suzuki']
# motorcycle.insert(0,'ducati')
# print(motorcycle)

#List_remove

motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)
del motorcycle[0]
print(motorcycle)


# mylist = ['jasdfoeifheoif', 1,2,311.1, True , 'adafj', [1,2,34]]
# print(len(mylist))

# myList = ['anu','anu2 ', 'anu', 'g', 'T', 'o']
# print(myList[:-2])


# myList = ['a','b','c','d','e']
# print('Before reassignment')
# print(myList)
# myList[0]= 'New Item'
# print('After reaassignment')
# print(myList)

# myList = ['a','b','c','d','e']
# listtwo = ['a','n','o','n','n','a']
# # myList.append()
# myList.extend(listtwo)
# print(myList)

#pop up msg
myList = ['a','b','c','d','e']
# item = myList.pop(0)
# print(myList)
# print(item)
#revwrse
# myList = ['1','2','3','4','5']
# myList.reverse()
# print(myList)

#sort
# myList = ['0', '880', '56','45','32','16','50','10','4']
# myList.sort()
# print(myList)

#nestedList
# myList = [1,2,['x','y','z']]
# print(myList[2][2])

#List comprehensive
matrix = [[1,2,3],[3,4,5],[5,6,7]]
first_col =[row[0] for row in matrix]
print(first_col)

#how to add two list
list1 = ['a','b', 'c']
list2 = [1,2,3]
for x in list2:
     list1.append(x)
print(list1)

list1 = ['a','b', 'c']
list2 = [1,2,3]

list1.extend(list2)
print(list1)

thislist = list(("apple","banana","cherry"))
print(thislist)
















































 




