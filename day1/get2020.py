#!/usr/bin/env python3

import numpy as np

data = np.loadtxt("data.txt", dtype=int)

if3found = False


def find_two_for_total(dataset, start_index=1, total=2020):
    data_size = len(dataset)
    for i in range(start_index, data_size):
        for j in range(i + 1, data_size):
            if dataset[i] + dataset[j] == total:
                return dataset[i], dataset[j]
        else:
            continue
        break
    return 0, 0


print("Find two number that add to 2020")
a, b = find_two_for_total(data, total=2020)
print("\tfirst: {:d}, second: {:d}, product: {:d}".format(a, b, a * b))

print("\n")

print("Find three number that add to 2020")
for k in range(0, len(data) - 1):
    a, b = find_two_for_total(data[k:], start_index=k + 1, total=2020 - data[k])
    if a != 0 and b != 0:
        print("\tfirst: {:d}, second: {:d}, third: {:d}, product: {:d}".format(data[k], a, b, data[k] * a * b))
