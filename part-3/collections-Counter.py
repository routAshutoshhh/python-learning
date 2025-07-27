#the python proviudes  with a collection module - 
#collections - counter, namedtuple, OrderedDict, defaultdict , deque

#using collection 
#counter
from collections import Counter   # iimporting the counter from the collections module
'''
a counter is a basically a dictionary that keeps track of the elements as the keys and their  counts as their values
'''
stringhun = "aaaabbbbbcccc"

#creating a counter
my_counter = Counter(stringhun) # using Counter constructor to create a counter  object

#lets try printting the counter and items and keys and values
print(my_counter)  # Output: Counter({'a': 4, 'b': 5, 'c': 4})
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())


# so if i want to know the most common elements in the counter i mean the most occuring  elements  so we can  use the most_common() method passing the number ofd most commmon elemets we want to see
# i wwant to see the 2 most common elements  lets say
print(my_counter.most_common(2)) #since the 1st most commmon element is 'b' and the 2nd most common element is 'a' so it will return [('b', 5), ('a', 4)]

#so instead of seeing the most common elements in the dicttioanry and inside of dictionary tuple  and inside of tuple we have the elents we can do something like this
print("the most common element  here in the string is ")
highest_occuring_element = my_counter.most_common(1)[0][0] #we are printing the most common element by first getting in the list format so list[0] then the list has the tuple format and then the tuple has in the [0] indes the item  b 
print(highest_occuring_element)

#to convert the string "stringhun" to a  list we can do this

#easiest way to convert a string to list
listhun = list(stringhun)
print(listhun)

#if we want to use the my_counter to make   the string itereable
#here ill not break the string into the list - but will break the my_counter into string
listhun1 = list(my_counter)#this will give me the keys only - [a , b , c]
print(my_counter.elements()) #this wil return an object from the the copunter class which has the elements 
listhun2 = list(my_counter.elements())
print(listhun1)
print(listhun2) #this will give me the list of the keys repeated according to their values - ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c']