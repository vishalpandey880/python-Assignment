my_list = [1,2,3,4,5,3,6,7,8,9,10]
unique_list = []

for x in my_list:
    if x not in unique_list:
        unique_list.append(x)
        print(unique_list)
