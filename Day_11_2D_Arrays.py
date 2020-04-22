#!/bin/python3

import math
import os
import random
import re
import sys

def calculatesum(i,j):
    return(a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2])

if __name__ == '__main__':
    a = []
    sums = []

    for _ in range(6):
        a.append(list(map(int, input().rstrip().split())))
    
    for j in range(0,4):
        for i in range(0,4):
            sum = calculatesum(i,j)
            sums.append(sum)
    print(max(sums))


