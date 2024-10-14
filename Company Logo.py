#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input()
    s = sorted(s)
    
    # using counter method to find the frequency of each of the words
    freq = Counter(list(s))
    
    # using for loop to print the three words with frequency
    for i, j in freq.most_common(3):
        print(i, j)
