#!/usr/bin/env python3

import numpy as np
from re import compile, sub


def is_valid_line(line, regex):
    regex = compile(regex)
    if not regex.match(line):
        raise ValueError("line contains unrecognized value; only [a-z] allowed")


def get_unique_char_no(line):
    is_valid_line(line, "^[a-z]+$")
    return len(set(line))


def get_char_no_in_all_elements(line):
    is_valid_line(line, "^[a-z ]+$")
    entries = line.split(" ")
    if len(entries) == 1:
        return len(entries[0])
    count_all = 0
    for c in entries[0]:
        if all(c in e for e in entries[1:]):
            count_all += 1
    return count_all


f = open("data.txt")
raw = f.readlines()
f.close()

raw_length = len(raw)
data_clean = []
data_unique = []
total_checked_any = total_checked_all = 0

i = 0
while i < raw_length:
    if raw[i] != "\n":
        data_clean.append(raw[i])
        j = i + 1
        while j < raw_length and raw[j] != "\n":
            data_clean[-1] += " " + raw[j]
            j += 1
        else:
            i = j + 1
            total_checked_any += get_unique_char_no(sub(r"[\n\t\s]*", "", data_clean[-1]))
            total_checked_all += get_char_no_in_all_elements(sub(r"[\n\t]*", "", data_clean[-1]))


print("'Any' logic: checked fields of all groups in total: {}".format(total_checked_any))
print("'All' logic: checked fields of all groups in total: {}".format(total_checked_all))

