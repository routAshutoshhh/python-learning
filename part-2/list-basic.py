#list - ordered , mutable, allows duplicate elements:

#defining a list 
listsimple = ["banana", "apple", "orange", "kiwi", "mango"]
mixedlist =  ["banana", 1, 2.5, True, "apple" ,"apple"]
print(listsimple)
print(mixedlist)
#accesing using index 
print(mixedlist[0])  # output: banana
print(mixedlist[-1]) # output: apple (last element) due to negative indexing

#output: ['banana', 'apple', 'orange', 'kiwi', 'mango'] amd ['banana', 1, 2.5, True, 'apple','apple']

# creating list using a function
mylist = list()
print(mylist) # shall create an empty list in which later we can add elements
mylist.append("banana") # in this way we can append elements to the list in the end of the list
mylist.append("apple")
print(mylist)  # output: ['banana']


# for looping to iterate the list
for i in mixedlist:
    print("printing ",i)


# to check  if the element is  in the list just wihtout using loops  then:
if "apple" in mixedlist:
    print("apple is in the list")
else:
    print("apple is not in the list")

#printing the length of the list
print("Length of mixedlist is:", len(mixedlist))  # output: 6


#methods for list to 
#append , insert , remove 
#insert - we use this method to directly insert this element at the specific index
mixedlist.insert(2, "grape")  # inserting "grape" at index 2
print("After inserting grape at index 2:", mixedlist)  # output: ['banana', 1, 'grape', 2.5, True, 'apple', 'apple']

#pop - we  use this to just pop hte elment from the rear end of the list
mixedlist.pop()  # removes the last element- last apple 
print("After popping the last element:", mixedlist)  # output: ['banana', 1, 'grape', 2.5, True, 'apple']

#remove - we use this to remove the first occurrence of the specified element
mixedlist.remove("apple")  # removes the first occurrence of "apple"
print("After removing the first occurrence of apple:", mixedlist)  # output: ['banana', 1, 'grape', 2.5, True]

#clear
mixedlist.clear()  # removes all elements from the list
print("After clearing the list:", mixedlist)  # output: []


#working with sorting the elements in the list

noList = [5, 2, 9, 1, 5, 6]
# sorting the list in ascending order
# to basically create a new sorted list without changing the original list , we can use the built in function sorted()
newSortedList = sorted(noList) 
print("Original list:", noList)  # output: [5, 2, 9, 1, 5, 6]
print(newSortedList)  # output: [1, 2, 5, 5, 6, 9] - this does not change the original list

#sorting the original list in the place
#noList.sort()
print("Sorted  original list in ascending order:", noList)  # output: [1, 2, 5, 5, 6, 9]- but this happens in place 



