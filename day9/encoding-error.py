#!/usr/bin/env python3

import numpy as np


def find_invalid_sum(data, preamble):
    for i in range(preamble, data.size):
        for j in range(i - preamble, i - 1):
            for k in range(i - preamble + 1, i):
                if data[j] + data[k] == data[i]:
                    break
            else:
                continue
            break
        else:
            return i, data[i]
    return None, None


def find_consecutive_sum(data, sum_value):
    for i in range(data.size - 1):
        for j in range(i + 1, data.size):
            if np.sum(data[i:j + 1]) == sum_value:
                return np.min(data[i:j + 1]), np.max(data[i:j + 1])
    return None


if __name__ == "__main__":
    data = np.loadtxt("data.txt", dtype=int)
    preamble = 25

    index, value = find_invalid_sum(data, preamble)
    print("first number that is not sum of the {} previous: index {}, value {}".format(preamble, index, value))

    result = find_consecutive_sum(data, value)
    if result:
        print("consecutive sum, min + max of range: {}".format(sum(result)))
