#sets - sets can not contain duplicates and sets  contain unique elements
'''
sets are unordered colllection of items where they are yet unchangable but we can still add and remove items from it 
 they are unindexed sort of 

sets are written with curly braces like this { 1, 2, 3,}

certain things to understand avbout sets
Set Items

Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.
'''

#True and 1 considered the same in sets 
thisset = {"apple" , "banana" , 1 , True , 1.5}
print(thisset) # only  singular 1 is printed 

sethun = {"apple" , "banana", "kiwi", "orange"}
print(len(sethun))

#creating a set with the set() constructor
set1 = set(("apple", "banana", "kiwi"))  # set content is added  in rount brackets
print(set1)

#adding set items
thisgame = {"pubg", "free fire"}
for x in thisgame:
    print(x)


#to check if anything present in a set
print("pubg" in thisgame ) #this will be boolean value if pubg exists in the thisgame set
#to check if anything is not present
print("thor" not in thisgame) # this will be also true kind (!=thor)



#Adding  items to a set
set2 = {"apple", "banana"}
set2.add("orange")
print(set2)


#adding another set to a set
set3 = {1 , 2 , 3}
set4 = {4 , 5 , 6}
set3.update(set4)
print(set3) # this will be merged  and set3+set4

#so update is a crazy method which can add multiple colection lie tuples , lists , dictionaries etc  - any basically iterable object
set5 = {1, 2, 3}
tuple1 = (4 , 5, 6) # we are basically adding or may be converting a tuple to set and then merging it 
set5.update(tuple1)
print(set5)

#removing items from a set - remove () will raise an error if the item does not exist- this will give error
setu = {"apple", "banana", "kiwi"}
setu.remove("banana")  # this will remove banana from the set
#setu.remove("banana") - this will give error
print(setu)

#discard() - this will do the same as remove but will not raise any error if the item does not exits
setu.discard("banana")



#sethun - to clear method - clear() - method that can be used to remove all the items
#sethun = del - destructor the set - this will delete the set eg - del sethun
