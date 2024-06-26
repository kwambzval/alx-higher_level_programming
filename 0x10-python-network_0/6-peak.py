#!/usr/bin/python3
def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]

    mid = length // 2
    if (mid == length - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]) and \
       (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]):
        return list_of_integers[mid]
    elif mid != length - 1 and list_of_integers[mid + 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[mid + 1:])
    return find_peak(list_of_integers[:mid])
