#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    name = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        if(re.findall("@gmail.com",emailID)):
            name.append(firstName)
    
    for ele in sorted(name):
        print(ele) 
