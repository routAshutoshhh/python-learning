'''
so basically decorator are higher order function that wrap another function and add some extra functionality to it
'''
#deifning the decorator
def mydecorator(func):
    def wrappper():
        print("start")
        func()
        print("end")
    return wrappper

#we can choose to use decorator in any of the following ways

#method -1
# here we are wrapping the function with teh decorator 
@mydecorator
def function_name():
    print("Hello, I am a function")

#method -2
 # or we can do this instead instead of wraping the funciton in the decorator  - we can pass the function as an argument and then assign it the same function
#function_name = mydecorator(function_name)

function_name()
 