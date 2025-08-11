
#this is the simple function 
def hello(name : str , age: int):
    print("hello my name is {name} and  my age is {age}")


#example for the keyword arguments
def hellopostitional(name : str, age:  int = 32 ):
    print(f"hello my name is {name} and  my age is {age}")


hellopostitional("sachin")
hellopostitional("sachin", 25) #by sending the new value for the age we shifted the keyword to positional


#understanding the args and kwargs where args means = positional arguments and kwargs means keyword arguments
def functional_arguments(*args , **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

functional_arguments(1, 2, 3,"PRAHAKAR", name="sachin", age=25)#THE ONES which are not set  with values with any  keyword will be send to kwargs and the others will be send to args