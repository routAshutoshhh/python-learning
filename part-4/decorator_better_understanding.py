 #lets work with another example to undersstand the argument passing and key words argyuemnt passing
import functools

 #defining the decorator
def decoratorFunction(func):
    @functools.wraps(func)  # This preserves the metadata of the original functionS
    def wrapper(*args , **kwargs):
        print("wrapper function hun bhai")
        result = func(*args , **kwargs)
        return result 
    return wrapper


@decoratorFunction
def  normalFunction(x):
    print("normal  function hun bhai")
    return x+5

print(normalFunction(12))

print(normalFunction.__name__)# for normal function to be working recognnized propperly which is  will not work without functools which will wrap the function and preserve the metadata
print(decoratorFunction.__name__)