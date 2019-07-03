#Sk Adib Asker
#CS 100 2017F Section 103
#HW 00, Sept 27, 2017
#Question 1
a=3
b=4
c=5
if a<b:
    print("Ok")
if c<b:
    print('Ok')
    
if (a+b)==c:
    print('OK')
    
if (a**2 + b**2)==c**2:
    print('OK')
#Question 2   
a=3
b=4
c=5
if a<b:
    print('OK')
else:
    print('NOT OK')
if c<b:
    print('OK')
else:
    print('NOT OK')
if (a+b)==c:
    print('OK')
else:
    print('NOT OK')
if (a**2+b**2)==c**2:
    print('OK')
else:
    print('NOT OK')

#Question 3
import turtle
s = turtle.Screen()
t = turtle.Turtle()
color = str(input('What color?'))
width = int(input('What line width?'))
length =int(input('What line length?'))
select = str(input('line , triangle or square? '))

if select == 'square':
    
    t.color(color)
    t.width(width)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    
if select == 'triangle':
    
    t.color(color)
    t.width(width)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
    
if select == 'line':
    t.color(color)
    t.width(width)
    t.forward(length)
    
    
    


   


