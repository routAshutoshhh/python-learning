#tuples - ordered ,i9mmutable, allows duplicate elements: 
# tuples are similar to lists but they cannot be changed after creation - tuples are often created for  objects that belong together
#how to declare a tuple - it will work with both ways

my_tuple = ("max" , 29 , "india")
print(my_tuple)
tuplehun = "max" , 29 , "india"
print(tuplehun)



#if our tuple has only one element
my_tuple2 = ("max",) # we cannot do my_tuple2 = ("max") - this will be interpreted as a string

#to create tuple from iterables
my_tuple3  = tuple(["max", 29, "india"])
print(my_tuple3)

#to ACCESS SINGULAR elements in the tuple
items = my_tuple3[1]
print(items)  # Output: 29
print(my_tuple3[-1])
#cant do this - mutating a tuple

#my_tuple3[1] = 30  # TypeError: 'tuple' object does not support item assignment



