my_tuple = (1, 2, 3, 4, 5)
user_input = int(input("Enter a value to find index"))
if user_input in my_tuple:
    for x in list(my_tuple):
        if x== user_input:
            print(list(my_tuple).index(x)) 
else:
    print("input number doesn't exist")