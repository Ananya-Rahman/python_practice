#arrayCheck([1,1,2,3,1]) - true
#arrayCheck([1,1,2,4,1]) - Flase
#arrayCheck([1,1,2,1,2,3]) - true

def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

#stringBits('Hello')- 'Hlo'
#stringBits('Hi')- 'H'
#stringBits('Heeololeo')- 'Hello'

def stringBits(myString):
    result = ""
    for i in range(len(myString)):
        if i%2 == 0:
            result = result+ myString[i]
    return result

