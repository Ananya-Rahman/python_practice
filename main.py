

num_int = 123
num_str = "456"

num_str = int(num_str)

print(num_int+num_str)

print(type(5))

print(type(5.0))

language = ["French", "Italian", "German", "English"]

print(language[0])

print(language[3])

my_string = 'hello'
print(my_string)

my_string = "hello"
print(my_string)

my_string = '''hello world''' 
print(my_string)

my_string = """hello, welcome
            the worls of python"""
print(my_string)

vowels = ['a', 'e', 'i', 'o', 'u']

index = vowels.index('e')

print("the index of e:", index)

index = vowels.index('i')
print('The index of i:', index)

#randomList

random = ['a', ('a', 'b'), [3,4]]

index = random.index(('a', 'b')) 
print("the index of ('a', 'b'):", index)

index = random.index([3, 4])
print("the index no of [3, 4]:", index)

#upadte

animal = ['cat', 'dog', 'rabbit']

animal.append('guinea pie')

print('update animal list: ', animal)

#append

animal = ['cat', 'dog', 'ribbit']

wild_man = ['tiger', 'fox']

animal.append(wild_man)
print("upadte animals list:", animal)

#extend
language = ['french', 'spanish', 'belgium']
language_tuple = ('chinees', 'portugess')
language_set = {'japanees', 'english'}

language.extend(language_tuple)
print('New language list: ', language)

language.extend(language_set)
print('Newest language', language)

vowel = ['a', 'e', 'i', 'u']

vowel.insert(3, 'o')
print('update List:', vowel)

mixed_list = [{1,2}, [5,6,7]]

num_tuple = (3, 4)

#remove
animal = ['cat', 'dog', 'rabit', 'gennie pig']
animal.remove('dog')
print("Update animal list: ", animal)

# count
vowels = ['a', 'e', 'i', 'o', 'u']
count= vowels.count('i')
print('The count of num i is: ', count)

count = vowels.count('p')
print('The count of p is:', count)

#randomCount
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
count = random.count(('a','b'))
print("the count of ('a','b'):", count)
count = random.count([3,4])
print("The count of [3,4] is", count)

#list_Pop
language = ['python', 'java', 'c++', 'french', 'c']
return_value = language.pop(3)
print("return_value is: ", return_value)

print('update language:', language)

#negIndicate

language = ['python', 'java', 'C++', 'Ruby', 'C']
print('when index is not passed:')
print('return value: ', language.pop())
print('update list', language)

#when -1 is passed
#pops last element

print('when -1 is passed:')
print('return value:', language.pop(-1))
print("update language", language)
#also can use remove method

#List_inverse
os = ['windows', 'macOs', 'linux', 'xp']
print('original list:', os)

reverse_list = os[::-3]
print('update List:', reverse_list)

os = ['Windows', 'macOS', 'Linux']

for o in reversed(os):
    print(o)

#List_sort

vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort()
print('sorted list:', vowels) 
#vowels.sort(reverse=True)
#print('sorted list decending order:', vowels)  

def takeSecond(elem):
    return elem[1]  

random = [(2,2), (3,4), (4,1), (1,3)]

random.sort(key=takeSecond)
print('random list:', random)

#copying list
list = ['cat', 0, 6.7]
new_list = list.copy()
new_list.append('dog')
print('old list: ', list)
print('New list: ', new_list)

list = ['cat', 0, 6.7]
new_list = list[:]
del list[:]
new_list.append('dog')
print('Old List', list)
print('New list', new_list)

#clear
vowels = {'a', 'e', 'i', 'o', 'u'}
print('vowels(before clear):', vowels)

vowels.clear()
print('vowels(after clear):', vowels)

#ascii
normalText = 'python is interesting'
print(ascii(normalText))
otherText = 'python is interesting'
print(ascii(otherText))
print('pyth\xf6n is intersteing')











































 


















































































    