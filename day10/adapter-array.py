#!/usr/bin/env python3

import numpy as np
from copy import deepcopy
import pprint


def find_adapter_array(adapters):
    last_min = 0
    remaining_adapters = deepcopy(adapters)
    d = {
        1: 0,
        2: 0,
        3: 0,
    }
    for i in range(adapters.size):
        min_adapter_i = np.argmin(remaining_adapters)
        d[remaining_adapters[min_adapter_i] - last_min] += 1

        last_min = remaining_adapters[min_adapter_i]
        remaining_adapters = np.delete(remaining_adapters, min_adapter_i)

    return d


def find_adapter_possibilities(adapters, last_min, counter):
    if 0 <= adapters.size <= 1:
        counter[0] += 1
        lastno.append(last_min)
        return
    where = np.where((0 < adapters) & (adapters - last_min <= 3))
    if where[0].size > 0:
        for w in where[0]:
            slice_i = np.where(adapters > adapters[w])
            find_adapter_possibilities(adapters[slice_i], adapters[w], counter)


if __name__ == "__main__":
    data = np.loadtxt("data.txt", dtype=int)

    d = find_adapter_array(data)
    pprint.pprint(d)

    print("adapter differences where dj=1 and dj=3 multiplied: {}".format(d[1] * (d[3] + 1)))

    max_adapter = np.max(data)
    lastno = []

    data_expanded = np.append(data, [0, max_adapter + 3])
    data_sorted = np.sort(data_expanded)
    data_diff = np.diff(data_sorted)
    pprint.pp(data_sorted)
    pprint.pp(data_diff)
    wheres = np.append([-1], np.where(data_diff == 3)[0])

    possibility_dict = {}
    for i in range(wheres.size - 1):
        counter = [0]
        ones = wheres[i + 1] - wheres[i] - 1
        if ones <= 1:
            continue
        if ones in possibility_dict.keys():
            possibility_dict[ones]["count"] += 1
            continue
        vec = np.arange(1, ones + 1)
        find_adapter_possibilities(vec, 0, counter)
        possibility_dict[ones] = {
            "combinations": counter[0],
            "count": 1
        }

    p = 1
    for d in possibility_dict:
        p *= possibility_dict[d]["combinations"] ** possibility_dict[d]["count"]

    pprint.pprint(possibility_dict)

    print("number of possibilities: {}".format(p))
