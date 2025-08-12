class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


    #here this init is overwriting the previous one and hence we can conclude that python can never have multiple constructors 
    def __init__(self, name, species, age ):
        self.name = name
        self.species = species
        self.age = age



#hack - we can use still create the multiple constructors  using the below method and example 

# we can do this using the positional arguments and keywords arguments

#basically a illusion of multiiple constructor 
class Car:
    def __init__(self , *args):
        if len(args) == 2:
            self.make = args[0]
            self.model = args[1]
        elif len(args) == 3:
            self.make = args[0]
            self.model = args[1]
            self.year = args[2]
        else:
            raise ValueError("Invalid number of arguments")


#making the object for this 
car1 = Car("2012" , "bmw")

print(car1.model)
print (car1.make)