import random
'''
    Quicksort 
        Adopted From: https://stackoverflow.com/a/31102672 & http://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
        Time Complexity - O(n log(n))
        Space Complexity - O(n)
        Developer Note: Sorts a list in place

    Sort the range list[start_index, end_index] in-place with vanilla QuickSort

    :param list:  the list of numbers to sort
    :param start_index: the first index from list to begin sorting from,
                must be in the range [0, len(list))
    :param end_index: the last index from list to stop sorting at
                must be in the range [start_index, len(list))
    :return:    nothing, the side effect is that list[start_index, end_index] is sorted
'''
def quicksort(list: list, start_index: int, end_index: int):

    # we've reach the end of our paritition so let's return back
    if start_index >= end_index:
        return
    i, j = start_index, end_index
    # choose random piviot based on value in between the left and right index
    pivot = list[random.randint(start_index, end_index)]

    # while the left index is less than or equal to the right index
    while i <= j:
        # while the left element is less than the randomly chosen piviot
        while list[i] < pivot:
            # increase the left index by 1
            i += 1
        # while the right element is greater than the randomly chosen piviot
        while list[j] > pivot:
            # decrease the right index by 1
            j -= 1
        # if the left index is less than or equal to the right index
        if i <= j:
            # swap left and right elements - vital since it wouldn;t be quicksort if it was not in-place.
            list[i], list[j] = list[j], list[i]
            # increment and decrement left and right index
            i, j = i + 1, j - 1
    # quicksort left partition
    quicksort(list=list, start_index=start_index, end_index=j)
    # quicksort right partition
    quicksort(list=list, start_index=i, end_index=end_index)


arr = [9,8,7,5,3,7,8,1]
quicksort(list=arr, start_index=0, end_index=len(arr)-1)
print(arr)