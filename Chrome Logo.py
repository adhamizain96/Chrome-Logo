#!/usr/bin/env python
# coding: utf-8

# In[1]:


from turtle import *      
import turtle
import random

screen = turtle.Screen()
screen.setup(1000, 1000)
turtle.title('Google Chrome Logo')

#note - chrome logo - red, green, yellow, and blue
#note - RGB-to-Hex Conversion - http://www.javascripter.net/faq/rgbtohex.htm
colormode(255)
#seth() - this method is used to set the orientation of the turtle to to_angle
seth(-150)
up()

#---red---
#note - red 
color(255, 0, 0)
begin_fill()
fd(120)
down()
right(90)
circle(-120, 120)
fd(120*3**.5)
left(120)
circle(2*120, 120)
left(60)
fd(120*3**.5)
end_fill()
#---red---

#---green---
color(0, 128, 0)
left(180)
begin_fill()
fd(120*3**.5)
left(120)
circle(2*120, 120)
left(60)
fd(120*3**.5)
left(180)
circle(-120, 120)
end_fill()
#---green---

#---yellow---
color(255, 255, 0)
left(180)
circle(120,120)
begin_fill()
circle(120, 120)
right(180)
fd(120*3**.5)
right(60)
circle(-2*120, 120)
right(120)
fd(120*3**.5)
end_fill()
#---yellow---

#---blue---
color(0, 0, 255)
up()
left(98)
fd(120/20)
seth(60)
down()
begin_fill()
circle(distance(0, 0))
end_fill()
#note - ht()- makes the turtle invisible
ht()
#---blue---

done()


# In[ ]:




