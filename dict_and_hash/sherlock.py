#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput
from datetime import datetime


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    s_list = s.strip()
    result = 0

    # For each possible number of characters i
    for i in range(1, len(s_list)):

        # For each subset of i characters starting at j
        for j in range(len(s_list) - i):
            sublist = sorted(s_list[j:j + i])
            sublist_set = set(sublist)

            # Check if the subset exists in the remaining string
            if sublist_set.issubset(set(s_list[j+1:])):

                # For each subset of characters starting at k
                for k in range(j + 1, len(s_list) - i + 1):

                    # Add if there is a match
                    result += sublist == sorted(s_list[k:k + i])

    return result


if __name__ == '__main__':

    file_in = fileinput.input()
    lines = int(file_in[0])

    start = datetime.now()
    for line in file_in:
        result = sherlockAndAnagrams(line)
        print(result)
    print(datetime.now() - start)

    ## 100: 807
    #s = 'shdfuytwqeuigvsdfugshjdvcjhsgyuftweiufjkxvgxhgviusgfsiudwggfiusytiwehjvcsjgeyrgefhwegwfgefvjshdjsadn'
    #print(len(s))
    #start = datetime.now()
    #print(sherlockAndAnagrams(s))
    #print(datetime.now() - start)
    ## 150: 1485
    #s = 'shdfuytwqeuigvsdfosaiiutixviuwxneyrrcweolxzwoeiuycitbxweyrcybufwgxyugshjdvcjhsgyuftweiufjkxvgxhgviusgfsiudwggfiusytiwehjvcsjgeyrgefhwegwfgefvjshdjsadn'
    #print(len(s))
    #start = datetime.now()
    #print(sherlockAndAnagrams(s))
    #print(datetime.now() - start)
