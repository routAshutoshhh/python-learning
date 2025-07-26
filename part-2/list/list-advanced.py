#this operation over the list will add elements to the list
mylist = [0] * 5
print(mylist)


# conmcatinating the lists
list1 = ["banana", "apple"]
list2 = ["orange", "kiwi"]
newlist = list1 + list2
print(newlist)

#slicing the list
listhun = ["banana", "apple", "orange", "kiwi", "mango"]

#while slicing  we  tell the start and stop index
list_sliced = listhun[1:3] # end index is exclusive
print("Sliced list:", list_sliced)  # output: ['apple', 'orange']

# using step index in slice
list_step = listhun[1::2] # will take every  2 nd index from the start
print(list_step)  # output: ['apple', 'kiwi']

# reversing the list using -1
print(listhun[::-1]) # this will take every index from the behind like starting index  before banana we have  mango

#advanced concept - for creating a copy 

list1 = [ 1, 2 , 3, 4 ]
copylist = list1 # if i do this this will not be copy rather the copylist will poiint to the samne list here
 #so we use this .copy() method
copylist1 = list1.copy()  
copylist2 = list(list1) # this will work the same as .copy 
copylist3 = list1[:] # this also makes an  copy not affect  the original list 
print("Original list:", list1)  # output: [1, 2, 3, 4]
copylist.append(5)  # this will change the original list as well
print("Copied list:", copylist, "and here is the original which also changed:", list1)  # output: [1, 2, 3, 4]
print("Copied list:", copylist1)  # output: [1, 2, 3, 4] this copylist has not appended 5



#advanced thing - list comprehension - method to create a new list using an existing list in the most fastest way
# understanding this  with creating a new list from a list of number sand the new list willl contain the square of the  elements of the original list
org_list= [1 , 2, 3 ]
sqr_list = [ i*i for i in org_list]
print("Original list:", org_list)  # output: [1, 2, 3]
print("Squared list:", sqr_list)  # output: [1, 4,9] sytax is - [ expression - for loop on the elements in the list ]
