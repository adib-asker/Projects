#Sk Adib Asker
#CS 100 2017F Section 103
#HW 09, Nov 1, 2017
#1
def initialLetterCount(wordList ):
    dictionary = {}
    for word in wordList:
        if word[0] not in dictionary:
            dictionary[word[0]] = 1
        else:
            dictionary[word[0]] += 1
    return dictionary

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
w_list = ['I', 'i', 'Sorry', 'sorry', 'say', 'Say', 'I', 'i', 'Matthew', 'mean', 'Meat']
test_list = ['what', 'What', 'hello', 'Hello', 'Zero', 'zero', 'Z', 'z', 'Zebra','Animal']
print('Initial Letter Count Programs Tests: ')
print(initialLetterCount(horton))
print(initialLetterCount(w_list))
print(initialLetterCount(test_list))

#2
def initialLetters(wordList):

    dictionary={}

    for word in wordList:
        #letter=word[0]
        if word[0] not in dictionary:

            dictionary[word[0]]=[word]

        elif word not in dictionary[word[0]]:

            dictionary[word[0]].append(word)

    return dictionary
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
w_list = ['I', 'i', 'Sorry', 'sorry', 'say', 'Say', 'I', 'i', 'Matthew', 'mean', 'Meat']
test_list = ['what', 'What', 'hello', 'Hello', 'Zero', 'zero', 'Z', 'z', 'Zebra','Animal']
print('Initial Letter Count Programs Tests: ')
print(initialLetters(horton))
print(initialLetters(w_list))
print(initialLetters(test_list))


#3
def shareALetter(wordlist):
    dictionary = {}
    for word in wordlist:
        if word not in dictionary:
            d_list = []
            for i in word:
                for n in wordlist:
                    if i in n: 
                        if n not in d_list:
                            d_list.append(n)

            dictionary[word] = d_list
    return dictionary

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
w_list = ['I', 'i', 'Sorry', 'sorry', 'say', 'Say', 'I', 'i', 'Matthew', 'mean', 'Meat']
test_list = ['what', 'What', 'hello', 'Hello', 'Zero', 'zero', 'Z', 'z', 'Zebra','Animal']
print('Share Letter Programs Tests: ')
print(shareALetter(horton))
print('\n')
print(shareALetter(w_list))
print('\n')
print(shareALetter(test_list))


