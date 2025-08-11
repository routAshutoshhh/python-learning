'''
why funtions are important
1.to make the code more readable 
2. to make the code more efficient 
3. to make the code more maintaiable 
4. to make the  code more reusable 
5. to make the code more extensible 
'''


#this is the better way to define and write a function 
def odd_even_sum(lst : list)->tuple:
    '''
    description : this function does the work of finding the sum of the odd numbers and the even numbers inserted and send using a list

    return: integer
    '''
    
    even_sum = 0
    odd_sum = 0

    for i in lst: 
        if i%2 == 0:
            even_sum+=i
        else:
            odd_sum+=i

    return even_sum,odd_sum





print(odd_even_sum([1,23,21,233,34,34,3,4]))