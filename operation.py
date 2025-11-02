# a = 7
# b = a

# print(7)

x = int ("257")
z = int("257")

x = print(id(x))
z = print(id(z))

a = int("3")
b = int("3")

a = print(id(a))
b = print(id(b))

# print(x > 5 and x < 10)  #False
# print(x > 5 or x < 10)  #True
# print(not x >= 5)  #False
# print(not x > 5)  #True

# print(x  == z)  #False

print(x is z)  #False
print(a is b)  #True