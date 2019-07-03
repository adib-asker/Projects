#Sk Adib Asker
#CS 100 2017F Section 103
#HW 00, Sept 27, 2017
import turtle
s =turtle.Screen()
t=turtle.Turtle()

#1.(suqare)
for i in range(4):
    t.forward(100)
    t.left(90)
    
t.clear()
#(equilateral triangle)
numSide = 3
sideLen = 100
angle = 360.0 / numSide 

for i in range(numSide):
    t.forward(sideLen)
    t.left(angle)
t.clear()

#(pentagon)
numSide = 5
sideLen = 100
angle = 360.0 / numSide 

for i in range(numSide):
    t.forward(sideLen)
    t.left(angle)
    
t.clear()

#2
for i in range(1, 250, 50):
    t.right(90)
    t.forward(i)
    t.right(270)
    t.pendown()    
    t.circle(i)    
    t.penup()  
    t.home() 
s.bye()
'''
#or
t.circle(50)
t.penup()
t.rt(90)
t.fd(50)
t.left(90)
t.pendown()
t.circle(100)
t.penup()
t.rt(90)
t.fd(50)
t.left(90)
t.pendown()
t.circle(150)
t.penup()
t.rt(90)
t.fd(50)
t.left(90)
t.pendown()
t.circle(200)
'''

#3 (a)
import math
print(math.factorial(100))
#(b)
print(math.log2(1000000))
#c
print(math.gcd(63,49))

