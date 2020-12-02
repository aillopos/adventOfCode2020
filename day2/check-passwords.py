#!/usr/bin/env python3

import numpy as np
import re

# data = np.loadtxt("data.txt", dtype=str, delimiter=None)
f = open("data.txt", "r")
data = f.readlines()
f.close()

validNo = 0
stupidNo = 0

for i, val in enumerate(data):
    print(val)
    p = re.compile(r'^(\d+)-(\d+) ([a-zA-Z]+): ([a-zA-Z]+$)\n')
    result = p.split(val)
    print(result)
    regex = '[{}]'.format(result[3])
    p = re.compile(regex)
    occurrence = p.findall(result[4])
    # print(occurrence)
    ll = len(occurrence)
    if int(result[1]) <= ll <= int(result[2]):
        validNo += 1

    if (result[4][int(result[1]) - 1] == result[3]) != (result[4][int(result[2]) - 1] == result[3]):
        stupidNo += 1
        print("Huurraaayy!")

print("valid: {}".format(validNo))
print("validStupid: {}".format(stupidNo))
