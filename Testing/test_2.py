import random

for i in range(10):
    my_number = random.randrange(5)
    if my_number == 0:
        print("Dragon!")
    else:
        print("No Dragon.")