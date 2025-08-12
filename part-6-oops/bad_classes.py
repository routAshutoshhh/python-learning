#classes 
#constructor and attributes and method

#creating class in python

#crude way of defining of a class
class Car:
    pass




#building instances and object for the car class /blueprint
car1 = Car()
car2 = Car()

print(car1)

#adding attributes for the car1 and car2

car1.engine = "petrol"
car2.engine = "diesel"


car1.color = "red"
car2.color = "black"

print(car1.engine)
print(car2.engine)

#to see the inbuilt methods any object has - to see all the inbuilt methods
print(dir(car1))

##these are the methods present in a generic object
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__',
 '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
 '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'color', 'engine']
'''