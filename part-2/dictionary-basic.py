# in the recent version of python the dictionary is now ordered and  in the previous versions it would be unrodered
#dictionary - ordered  , mutable  and keyvalue pairs
'''
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
'''

#creating a dictionary 
disc = {
    "brand": "ford",
    "model": "mustang",
    "year": 2020
}

print(disc)

#length of the dictionary
print(len(disc))

#creating a dictionary using the dict() constructor
disc2 = dict(
    name ="henry" ,
    age = 30,
    country = "india"

)
print(disc2)


#accessing the items in the dictionary is done using the key
x= disc["brand"]
print(x)

#or we an use the get() method
y = disc.get("brand")

if x == y : 
    print("both are same")

#using the keys method to get all the keys in the particular dictionary 
keys = disc.keys()
print(keys)

#using the values method to get all the values in any particular dictionary
values = disc.values()
print(values)

#trying to get all the items in the dictionary  - The items() method will return each item in a dictionary, as tuples in a list.
print(disc.items())



#since the dictionary is mutable we can update /change  it using update() method
#method 1 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#method 2 - using update() method adn can use update  to add new key value pairs as well
thisdict.update({"color": "red"})

thisdict.update({"year": 2020})
print(thisdict)


#popping  or deleting the item in the dictionary
dictu ={
    "name": "john",
    "age": 25,
    "country": "USA"
}

# to pop the last item - popitem()
dictu.popitem()
print(dictu)

# to pop a specific item - pop()
dictu.pop("name")
print(dictu)

#to clear the dictionary - it clear the dictionary but does not delete it aand due to that reason i can still enter elements inside of it
dictu.clear()
print(dictu)  # this will print an empty dictionary {}

#we can delete the entire dictionary using del keyword
del dictu # most easy to delete the entire dictionary - it will delete the entire dictionary
#print(dictu)  # this will give an error as the dictionary is deleted

#making the  dictionary copy using -  .copy() and creating a new dictionary with the same 
#method 1- using .copy()  
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#method2 - using dict()

dictuuuu= dict(thisdict)
print(dictuuuu)
