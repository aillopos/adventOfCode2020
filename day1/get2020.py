#!/usr/bin/env python3

import numpy as np

data = np.loadtxt("data.txt", dtype=int)

if3found = False

for i, val in enumerate(data):
    for j in range(i+1, len(data)):
        if val + data[j] == 2020:
            print("first: {:d}, second: {:d}, product: {:d}".format(val, data[j], val*data[j]))
        if not if3found:
            for k in range(j+1, len(data)):
                if val + data[j] + data[k] == 2020:
                    print("first: {:d}, second: {:d}, third: {:d}, product: {:d}".
                          format(val, data[j], data[k], val*data[j]*data[k]))
                    if3found = True
                    break
