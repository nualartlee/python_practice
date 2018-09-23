#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    #s_list = [i for i in s.strip()]
    s_list = s.strip()
    result = 0

    # For each possible number of characters i
    for i in range(1, len(s_list)):
        #print("Checking {} chars:".format(i))
        #print(s_list)

        # For each subset of i characters starting at j
        for j in range(len(s_list) - i):
            #print("j: {}".format(j))

            # For each subset of characters starting at k
            for k in range(j+1, len(s_list) - i + 1):
                #print("k: {}".format(k))
                #print("{0} ==== {1}".format(sorted(s_list[j:j+i]), sorted(s_list[k:k+i])))
                if sorted(s_list[j:j+i]) == sorted(s_list[k:k+i]):
                    result += 1
                    #print("Result: {}".format(result))
    return result


if __name__ == '__main__':

    file_in = fileinput.input()
    lines = int(file_in[0])

    for line in file_in:
        result = sherlockAndAnagrams(line)
        print(result)

    s = 'shdfuytwqeuigvsdfjkhiuwteriugshjdvcjhsgyuftweiufjkxvgxhgviusgfsiudwggfiusytiwehjvcsjgeyrgefhwegwfgefvjshdjsadn'
    print(len(s))
    print(sherlockAndAnagrams(s))
