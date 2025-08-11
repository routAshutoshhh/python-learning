def arguments(*args , **kwargs):
    print("postional argument" , args)
    print("keyword argument" , kwargs)


#creating list and dictionary to insert into the arguments
lst = list(("sahin","kumar"))

dictionary ={
     "name" :"ashu",
     "age": 34
}



arguments(lst, dictionary ) # this will  put every thing into the positional argument 
print("the right way to do this:")
#right way to  put the dictionary into keyword argument 
arguments(*lst , **dictionary )