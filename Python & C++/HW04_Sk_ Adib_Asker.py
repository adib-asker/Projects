#Sk Adib Asker
#CS 100 2017F Section 103
#HW 04, Oct 4, 2017

#Question 1
months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
for i in months:
    if i[0] == 'J':
        print(i)

#Question 2
for i in range(100):
    if i%2==0 and i%5==0:
        print(i)
        
#Question 3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
for i in horton:
    if i in vowels:
        print(i)

