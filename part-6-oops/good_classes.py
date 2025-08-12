class Car:
    #constructor code - which gets called when we are creating an object /instance for the class
    def __init__(self , windows , color , engine):#here we are just passing the things in the run time and then we also need to pass the self argumernt here in this constructor
        self.win = windows
        self.rang = color
        self.engine = engine

    #method to check if it is self driving 
    def is_self_driving(self):
        return True if  self.win> 4 else False
    
    #function to check engine
    def engine_type(self, engine):
        print("the engine type previously  is : {} and then changed to this :{}".format(self.engine, engine))


car1 = Car(5 , "red" , "v8")
print("THE NO OF TYRES IN OBJECT CAR 1 IS: {}".format(car1.win))


#using the function to check  the car type for car1
if (car1.is_self_driving()):
    print("car is self driven ")

else:
    print("jhantu gaadi hai")


#using the function to check the engine type and understand the usage of self and parameter passing in the function of the classes
car1.engine_type("v9")


