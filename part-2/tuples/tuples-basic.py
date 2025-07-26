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
#checking if an element is present in the tuple
if"max" in my_tuple:
    print("yes han hai!")

#xcount the number of times an element has appeared in a tuple
no = 'q', 'e','q'
print("number of times q has appeared in the tuple is: ", no.count('q'))  # Output: 2

#index is used to find the first occuring index of  an element inthe tuple
print("index of e is: ", no.index('e'))  # Output: 1    

#this is the making of range in the tuples
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#This will return the items from position 2 to 5.
#and note that the item in position 5 is NOT included



## adding an element in the tuple

#method-1 - since tuples are immmutable , we need to create a new tuple to add with the other tuple wih this so we are basically playing around to what we desire

thisTuple = ("apple", "banana", "cherry")
y = ("orange" ,)

#so now i am going to concat a tuple
thisTuple += y
print(thisTuple)  # Output: ('apple', 'banana', 'cherry', 'oranage')


#method-2 - converting the tuple into a  list then adding any thing  that we want  and then converting it back into a tuple

tuplehun = ("apple", "banana", "cherry")
tupletoList = list(tuplehun)
tupletoList.append("orange")
tuplehun = tuple(tupletoList)
print(tuplehun)  # Output: ('apple', 'banana', 'cherry', 'orange')


#removing items in tuple
#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)