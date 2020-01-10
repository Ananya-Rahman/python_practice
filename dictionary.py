my_dict = {'name':'jack','age':26}
print(my_dict['name'])
print(my_dict.get(26))

#update
my_dict1 = {'name':'jack', 'age' : 26}
my_dict1['age'] = 27
print(my_dict1)

my_dict1['address'] = 'downtown'
print(my_dict1)

#del
squeares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squeares.pop(4))
print(squeares)

print(squeares.popitem())
print(squeares)
del squeares[1]
print(squeares)

squeares.clear()
print(squeares)

#operational
original = {1:'one', 2:'two'}
new = original.copy()

new.clear()
print('new',new)
print('original',original)

#formKeysSequence
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
print(vowels)

#sequenceVowel
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'
vowels = dict.fromkeys(keys,value)
print(vowels)

#valueAppend
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]
vowels = dict.fromkeys(keys,value)
value.append(2)
print(vowels)






























































