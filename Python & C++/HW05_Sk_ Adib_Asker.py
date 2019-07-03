#Sk Adib Asker
#CS 100 2017F Section 103
#HW 05, Oct 4, 2017
#Question 1
#a
def hasFinalLetter(strList,letters):
    listToReturn=[]
    for i in strList:
        for j in letters:
            if i.endswith(j) or i.endswith(j):
                listToReturn.append(i)
    return listToReturn
#b
#test case 1
strList = ["Hello worlD", "hotel", "Howdy"]
letters = "yD"
print(hasFinalLetter(strList, letters))

#test case 2
strList = ["Hello", "hotel", "How"]
letters = "yD"
print(hasFinalLetter(strList, letters))

#test case 3
strList = ["WorlD", "libra", "Bye"]
letters = "aI"
print(hasFinalLetter(strList, letters))

#Question 2
#a
def isDivisible(maxInt, twoInts):
    listToReturn = []
    counter = 0
    for number in range(0,maxInt):
        if number % twoInts[0] == 0 and number % twoInts[1] == 0:
            listToReturn.append(number)

    return listToReturn

#test case 1
twoInts = (3,5)
maxInt = 36
print(isDivisible(maxInt, twoInts))

#test case 2
twoInts = (1,2)
maxInt = 0
print(isDivisible(maxInt, twoInts))

#test case 3
twoInts = (2,4)
maxInt = 36
print(isDivisible(maxInt, twoInts))
