#inheritance in the python classes

class Car:
    def __init__(self,windows , door , enginetype):
        self.windows = windows
        self.door = door
        self.enginetype = enginetype

    def driving(self):
        print("i am driving from car")

    def stop(self):
        print("i  have stopped from here")


#creaing a child class first of all -  audi is inherinting the car class
class Audi(Car):
    def __init__(self, windows, door, enginetype, model):
        super().__init__(windows, door , enginetype)
        self.model = model

    def driving(self):
        print("i am driving from Audi with blueprint of car")

   
   #defining a function of the same name in the child class automatically over rides the parent class
    def stop(self):
        super().stop()# here i am invoking the parent class also 
        print(" hey i am stopping from  audi here ")


#creating the  instance of the child class 
audiA8 = Audi(4 , 2, "V8", "A8")


print(audiA8.model)
print(audiA8.windows )#accesssing the parent attribute 

#lets try calling the function 
audiA8.driving()
#lets try calling the super function from here only

audiA8.stop()


