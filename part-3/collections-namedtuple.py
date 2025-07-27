# we need to import the namedtuple from the collections moduel 
from collections import namedtuple 
#anmedtguple to as easy to create light weight object type similar to a struct in c
#syntax is basically - namedtuple('classname', 'field1, field2, field3')
Point = namedtuple('Point' ,'x,y')  # so this will create a class called Point with two string attributes x and y


pt = Point(10 , 20 )
print(pt)
#printing the attributes 
print(pt.x)
print(pt.y)
