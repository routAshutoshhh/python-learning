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
mylist.append("banana") # in this way we can append elements to the list
print(mylist)  # output: ['banana']


# for looping to iterate the list
for i in mixedlist:
    print("printing ",i)


# to check  if the element is  in the list just wihtout using loops  then:
if "apple" in mixedlist:
    print("apple is in the list")
else:
    print("apple is not in the list")