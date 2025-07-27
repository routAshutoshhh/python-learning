from collections import defaultdict 
# defaultdict is a subclass of the built-in dict class that returns a default value when a key is not found
'''
normal dictionary will raise a key error if you try to access a key that does not exist
'''

#create a defaultdict with a default value of int 

#default value of an integer is 0
default_dict = defaultdict(int)
default_float_dict = defaultdict(float)
#adding elemets to the defaultDict
default_dict['a'] = 1
default_dict['b'] = 2
default_dict['c'] = 3


#adding elemets to the defaultFloatDict
default_float_dict['a'] = 1.0
default_float_dict['b'] = 2.0


print(default_dict)
# accessing a key that does not exist will return the default value
print(default_dict['d'])  # this will print 0 since 'd' is not in the dictionary and the default value is 0
print(default_float_dict)
print(default_float_dict['d'])