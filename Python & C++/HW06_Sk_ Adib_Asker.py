#Sk Adib Asker
#CS 100 2017F Section 103
# HW 06, Oct 25, 2017
#1
def twoWords(length, firstLetter):
    result=[]
    while True:
        word=input("Enter a "+ str(length)+ "-letter word please: ")
        if length==len(word):
            result.append(word)
            break
        
        
    while True:
        word2= input("Enter a word begin with "+firstLetter+ " please: ")
        if firstLetter.lower()==word2[0] or firstLetter.upper()==word2[0]:
            result.append(word2)
            break
    print(result)
(twoWords(4,'B'))

#2
def twoWordsV2(length,firstLetter):
    result = []
    w = not False
    while (w):
        word = input('Enter a '+ str(length)+'-letter word please: ')
        if length == len(word):
           result.append(word)
           w = False
           continue
          
    while (not w):
        word2 = input("Enter a word begin with "+firstLetter+ " please: ")
        if firstLetter.lower() == word2[0] or firstLetter.upper() == word2[0]:
           result.append(word2)
           w = True
           continue
    print(result)
twoWordsV2(4,'B')
#3

def enterNewPassword():
 
    while True:
        word = input("Enter a password please: ")
        if 15 < len(word) or 8 > len(word) or sum(str.isdigit(c) for c in word) < 1:
            print("Password must be 8-15 characters long and contain at least one digit:")
        else:
            print("The password is valid.")
            break
 
enterNewPassword()

#4
import random
guessesTaken = 0
number = random.randint(0, 50)
i=1
print('I am thinking of a number between 0 and 50. You have five tries to guess it.')
while guessesTaken < 5:
    print('Guess', i, '?', end=' ')
    guess = int(input())
    guessesTaken = guessesTaken + 1
    i +=1

    if guess < number:
        print(guess, 'is too low.') 

    if guess > number:
        print(guess, 'too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('You are right! I was thinking of', number)

if guess != number:
    number = str(number)
    print('You are wrong! The number I was thinking of was ' + number)
