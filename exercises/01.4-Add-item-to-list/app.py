#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
for i in range(10):
    my_random_num = random.randint(1, 100)
    my_list.append(my_random_num)

print(my_list)