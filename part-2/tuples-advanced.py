#unpacking in tuples - in python we are also allowed to extract the values back into variables 

#understanding the tuples-
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple","banana")

#unpacking a tuple - we can also extract the values back into variables
fruits = ("apple", "banana", "cherry")
 #Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#using asterist - f the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


#joining the tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)



fruits1 = ("apple", "banana", "cherry")
mytuple = fruits1 * 2

print(mytuple)