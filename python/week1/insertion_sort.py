# Insertion Sort
#Insertion Sort w/ While-Loop

x = [23,11,2,27,1,16]

def insertion_sort(my_list):
    len_list = len(my_list)
    # loop through every element after the first
    for i in range(1,len_list):
        current = my_list[i]
        counter = i
        while counter > 0 and my_list[counter - 1] > current:
            my_list[counter] = my_list[counter-1]
            counter -= 1
        my_list[counter] = current
    return my_list

print insertion_sort(x)
