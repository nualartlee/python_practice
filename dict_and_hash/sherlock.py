#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    s_list = [i for i in s]
    s_set = set(s_list)
    duplicates = len(s_list) - len(s_set)
    f = math.factorial
    result = 0
    for i in range(duplicates):
        result += f(duplicates) // f(i)

    return result


if __name__ == '__main__':

    file_in = fileinput.input()
    lines = int(file_in[0])

    for i in range(lines):
        result = sherlockAndAnagrams(file_in[i])
        print(result)

