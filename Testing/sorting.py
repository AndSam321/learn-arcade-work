# Sorting items

my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
print(my_list)

# Swap the 15 and 14 values

temp = my_list[2]
my_list[2] = my_list[0]
my_list[0] = temp

"""my_list[0], my_list[2] = my_list[2], my_list[0]"""


print(my_list)