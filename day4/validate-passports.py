#!/usr/bin/env python3

import re


def hair_valid(hair):
    if hair[0] != '#' or len(hair) != 7:
        return False
    p = re.compile(r"^#[a-f0-9]{6}$")
    if not p.match(hair):
        return False
    return True


def pid_valid(pid):
    p = re.compile(r"^\d{9}$")
    if not p.match(pid):
        return False
    return True


def height_valid(height):
    if height[-2:] == "cm":
        return 150 <= string_to_int(height[:-2]) <= 193
    elif height[-2:] == "in":
        return 59 <= string_to_int(height[:-2]) <= 76
    return False


def string_to_int(x):
    try:
        return int(x)
    except ValueError:
        return 0


ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

valid_fields = {
    "byr": lambda x: 1920 <= string_to_int(x) <= 2002,
    "iyr": lambda x: 2010 <= string_to_int(x) <= 2020,
    "eyr": lambda x: 2020 <= string_to_int(x) <= 2030,
    "hgt": height_valid,
    "hcl": hair_valid,
    "ecl": lambda x: x in ecl,
    "pid": pid_valid,
}


def field_valid(kv):
    kv_split = kv.split(":")
    if kv_split[0] not in valid_fields.keys():
        return True
    return valid_fields[kv_split[0]](kv_split[1])


def valid2(line):
    split = line.split(" ")
    is_valid = True
    for s in split:
        is_valid = is_valid and field_valid(s)

    return is_valid


f = open("data.txt")
raw = f.readlines()
f.close()

line_total = len(raw)

valid_no = 0
valid2_no = 0

i = 0
data_clean = []
while i < line_total:
    if raw[i] != "\n":
        data_clean.append(raw[i])
        j = i + 1
        while j < line_total and raw[j] != "\n":
            data_clean[-1] += " " + raw[j]
            j += 1
        else:
            i = j + 1
        data_clean[-1] = data_clean[-1].replace("\n", "")
        if all(valid_field in data_clean[-1] for valid_field in valid_fields.keys()):
            valid_no += 1
            valid2_no += int(valid2(data_clean[-1]))
    else:
        i += 1

print(line_total)
print("no of valid passwords: {}".format(valid_no))
print("no of valid passwords 2: {}".format(valid2_no))
