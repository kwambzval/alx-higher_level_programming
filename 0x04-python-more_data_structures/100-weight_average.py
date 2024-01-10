#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all
       integers tuple (<score>, <weight>)."""
    if my_list:
        total = sum(x[0] * x[1] for x in my_list)
        weight = sum(x[1] for x in my_list)
        return total / weight
    return 0
