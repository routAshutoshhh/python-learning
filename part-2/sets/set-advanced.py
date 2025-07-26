#joining sets
'''
just the way you can use join in a diagram 
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.


The values True and 1 are considered the same value. The same goes for False and 0.
'''

#union  and update () of two sets
set1 = {"apple" ,"banana","cake"}
set2 = { 1, 2, 3}

set3 = set1.union(set2)
set4 = set1 | set2 # same thing as union
print(set3)
print(set4)

#union multiple sets
set5 = {'a' ,'b', 'c'}
set6 = set1|set2|set5
set7 = set1.union(set2,set5)
print(set6)
print(set7)


#doing the   set and tuple with union
tuple1 = (4 , 5 , 6)
print (set7.union(tuple1))


#update()in the set

sethun = {"apple", "banana", "kiwi"}
sethun2 = {1, 2, 3}
sethun.update(sethun2)  # this will merge both sets
print(sethun)


#intersection() - this will  keep  only the common items in both the sets - just like vein diagram
set1 = {"a", "b", "c"}
set2 = {"b", "e", "d"}
set3 = set1.intersection(set2)
print(set3) # output - b


#the intersection() - we can replace this  with & 

set10 = {"apple", "banana", "cherry"}
set20 = {"google", "microsoft", "apple"}

set30 = set10 & set20
print(set30)
#intersection_update() - this will also keep only the duplicates but will  change the original set instead of returning a new set

#difference()
'''
The difference() method will 
return a new set that will contain only the items from the first set that are not present in the other set.

'''
set11 = {"apple", "banana" , "cherry"}
set21 = {"google", "microsoft", "apple"}

set31 = set11.difference(set21) #{'banana', 'cherry'}
set32 = set21 - set11 #{'google', 'microsoft'}
print(set31)
print(set32)  

'''
The difference_update() method will also keep the items from the first set that are not in the other set, 
but it will change the original set instead of returning a new set.

'''

set100 = {"apple", "banana", "cherry"}
set200 = {"google", "microsoft", "apple"}

set100.difference_update(set200)

print(set100)

#symmetric_difference()
'''
The symmetric_difference() method will keep only the elements that are NOT present in both sets. or we can use ^ operator 
 it will simillarly has symmetric_difference_update() method which will change the original set instead of returning a new set.
'''
set111 = {"apple", "banana", "cherry"}
set211 = {"google", "microsoft", "apple"}

set311 = set111.symmetric_difference(set211)

print(set311)
