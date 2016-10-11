# Generate 100 random numbers from 0 to 10000
import random

def sort(my_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i+1]: # Find adjacent list items that are out of order
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i] # Tuple unpacking
                swapped = True
    return my_list

random_list = [random.randint(0,10000) for count in range(100)]

print(random_list)
print(sort(random_list))
