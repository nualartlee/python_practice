#!/bin/python3

import random
import datetime
from functools import reduce


def reduce_sort(arr):
    print('reduce sort')
    swaps = 0
    mapped = reduce(lambda x, y: (y, x)[y < x], arr)
    return mapped


def select_sort_copy_imp(arr):
    print('select sort copy imp')
    sorted_arr = sorted(arr.copy())
    result = 0
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            arr[arr.index(sorted_arr[i])] = arr[i]
            arr[i] = sorted_arr[i]
            result += 1
    return result


def select_sort_copy(arr):
    print('select sort copy')
    sorted_arr = sorted(arr.copy())
    result = 0
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            pos = arr.index(sorted_arr[i])
            arr[pos] = arr[i]
            arr[i] = sorted_arr[i]
            result += 1
    return result


def select_sort_deleting(arr):
    print('select sort deleting')
    result = 0
    for i in range(len(arr)):
        max_position = arr.index(max(arr))
        if max_position != len(arr) - 1:
            result += 1
            arr[max_position] = arr[-1]
        del arr[-1]
        #print("{0} {1} {2}".format(i, result, arr))
    return result


def fastest_sort(arr):
    """
    Only for consecutive integers 0 to length - 1
    :param arr:
    :return:
    """
    print('fastest sort')
    result = 0
    for i in range(len(arr)):
        if arr[i] != i:
            arr[arr.index(i)] = arr[i]
            arr[i] = i
            result += 1
        #print("{0} {1} {2}".format(i, result, arr))
    return result


def select_sort(arr):
    print('select sort')
    swap = 0
    for j in range(len(arr) - 1):
        change = False
        minimum = arr[j]
        position = 0
        for i in range(j + 1, len(arr)):
            if arr[i] < minimum:
                position = i
                minimum = arr[i]
                change = True
        if change:
            swap += 1
            arr[position] = arr[j]
            arr[j] = minimum
    return swap


def bubble_sort(arr):
    print('bubble sort')
    swap = 0
    for j in range(len(arr) - 1):
        change = False
        for i in range(len(arr) - j -1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                change = True
        if change:
            swap += 1
    print(arr)
    return swap


def merge_sort_count(org_arr):

    print(org_arr)
    tuple_arr = [[i, 0] for i in org_arr]

    def merge_sort(arr):

        if len(arr) > 1:
            half = len(arr) // 2
            left_arr = arr[:half]
            right_arr = arr[half:]

            merge_sort(left_arr)
            merge_sort(right_arr)

            i = j = k = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i][0] < right_arr[j][0]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    # Mark element as moved
                    right_arr[j][1] += 1
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            # add any remainder elements if lists are not equal in size
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1

        print(arr)

    merge_sort(tuple_arr)
    result = sum([i[1] > 0 for i in tuple_arr])
    return result


def diff_count(arr):
    print('diff count')
    length = len(arr)
    diff_arr = [i - j for i, j in zip(arr, sorted(arr))]
    move_left_arr = [i for i in diff_arr if i < 0]
    move_right_arr = [i for i in diff_arr if i > 0]
    out_of_place = length - diff_arr.count(0)
    move_left = len(move_left_arr) - move_left_arr.count(0)
    move_right = len(move_right_arr) - move_right_arr.count(0)
    print(arr)
    print(diff_arr)
    #print("diff arr {}".format(diff_arr))
    print("out of place {}".format(out_of_place))
    print("move left {}".format(move_left))
    print("move right {}".format(move_right))
    if out_of_place % 2:
        return out_of_place // 2 + 1
    return out_of_place // 2


def position_track(arr):
    print('position track')

    length = len(arr)
    tarr = [[arr[i], i] for i in range(length)]
    tarr.sort()
    swaps = sorted([[tarr[i][1], i] for i in range(length) if i != tarr[i][1]])
    temp_swaps = []
    final_swaps = []
    print(swaps)
    result = 0

    def independent_swaps(sw_arr):
        flat_list = [position for swap in sw_arr for position in swap]
        return len(flat_list) == len(set(flat_list))

    while not independent_swaps(swaps.copy()):
        i = 0
        while i < len(swaps) - 1:
            if swaps[i] == swaps[i+1]:
                #swaps[i] = swaps[i+1] = [0, 0]
                result += 1
                final_swaps.append(swaps[i])
                i += 2
                continue
            if swaps[i][0] == swaps[i+1][0]:
                temp_swaps.append([swaps[i][1], swaps[i+1][1]])
                final_swaps.append([swaps[i]])
                #swaps[i] = swaps[i+1] = [0, 0]
                result += 1
                i += 2
                continue
            if swaps[i][1] == swaps[i+1][1]:
                temp_swaps.append([swaps[i][0], swaps[i+1][0]])
                final_swaps.append([swaps[i]])
                #swaps[i] = swaps[i+1] = [0, 0]
                result += 1
                i += 2
                continue
            if swaps[i][0] == swaps[i+1][1]:
                temp_swaps.append([swaps[i][1], swaps[i+1][0]])
                final_swaps.append([swaps[i]])
                #swaps[i] = swaps[i+1] = [0, 0]
                result += 1
                i += 2
                continue
            if swaps[i][1] == swaps[i+1][0]:
                temp_swaps.append([swaps[i][0], swaps[i+1][1]])
                final_swaps.append([swaps[i]])
                #swaps[i] = swaps[i+1] = [0, 0]
                result += 1
                i += 2
                continue
            temp_swaps.append(swaps[i])
            i += 1
        #swaps = [i for i in swaps if i != [0, 0]]
        swaps = temp_swaps.copy()
        temp_swaps.clear()
        #print("final {}".format(final_swaps))
        #print("pendi {}".format(swaps))

    final_swaps += swaps
    print(final_swaps)
    return len(final_swaps)


def rand_array(length, swaps):
    arr = [i for i in range(length)]
    print('swap')
    swap = random.sample(range(length), swaps * 2)
    print(swap)
    for i in range(0, swaps, 2):
        j = swap[i]
        k = swap[i + 1]
        temp = arr[j]
        arr[j] = arr[k]
        arr[k] = temp
    return arr


def rand_array_free(length, swaps):
    arr = [i for i in range(length)]
    for i in range(swaps):
        j = k = 0
        while j == k:
            j = random.randint(0, length - 1)
            k = random.randint(0, length - 1)
        temp = arr[j]
        arr[j] = arr[k]
        arr[k] = temp
        print("swapped {0} {1}".format(j, k))
    return arr


if __name__ == '__main__':

    start = datetime.datetime.now()

    print('\nGenerating array')
    length = 10
    ra = rand_array_free(length, length//2)
    print(ra)
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()

    print('\nPython')
    sorted(ra.copy())
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()

    print('\n')
    print(fastest_sort(ra.copy()))
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()

    print('\n')
    print(position_track(ra.copy()))
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()

    #print('\n')
    #print(select_sort(ra.copy()))
    #print(datetime.datetime.now() - start)
    #start = datetime.datetime.now()

    #print('\nMerge')
    #print(merge_sort_count(ra.copy()))
    #print(datetime.datetime.now() - start)
    #start = datetime.datetime.now()

    #print('\n')
    #print(select_sort_copy(ra.copy()))
    #print(datetime.datetime.now() - start)
    #start = datetime.datetime.now()

    #print('\n')
    #print(select_sort_copy_imp(ra.copy()))
    #print(datetime.datetime.now() - start)
    #start = datetime.datetime.now()
