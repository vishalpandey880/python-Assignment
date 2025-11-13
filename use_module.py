# import custom_module
#from custom_module import y
# import custom_module as nums
#from custom_module import x as a #wrong 

#print(custom_module.x)
# print(nums.x)
# print(y)
# print(nums.y)

# import custom_module as validate

# print(validate.validate(10))


try:
    print(x)
except Exception as e:
    print("default")
else:
    print("inside else")
finally:
    print("inside finally")

my_set = {5, 6, 7, 7,True, 1} #false consider as 0 and true consider as 1
# my_set[0]

for x in my_set:
    print(x)

my_set.add("Q")
 #pop,remove, discard, clear