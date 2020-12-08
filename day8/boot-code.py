#!/usr/bin/env python3

import pprint
from re import compile, sub
from copy import deepcopy

commands = {
    "nop": lambda x: (0, 1),
    "acc": lambda x: (x, 1),
    "jmp": lambda x: (0, x),
}


def track_boot_code(code_lines):
    acc = 0
    passed = []
    index = 0
    while 0 <= index < len(code_lines):
        passed.append(index)
        a_plus, i_plus = commands[code_lines[index][0]](code_lines[index][1])
        acc += a_plus
        index += i_plus

        if index in passed:
            return acc, False

    return acc, True


def correct_boot_code(code_lines):
    for i, cl in enumerate(code_lines):
        code_lines_manipulated = deepcopy(code_lines)
        if cl[0] == "nop":
            code_lines_manipulated[i][0] = "jmp"
        elif cl[0] == "jmp":
            code_lines_manipulated[i][0] = "nop"
        else:
            continue
        acc, ok = track_boot_code(code_lines_manipulated)
        if ok:
            break

    return acc, ok


def clean_input(raw):
    clean_list = []
    regex = compile(r"^([a-z]{3}) ([\d+-]+)$")
    for line in raw:
        line = sub(r"[\n\t]*", "", line)
        line_list = list(filter(None, regex.split(line)))
        clean_list.append([line_list[0], int(line_list[1])])
    return clean_list


if __name__ == "__main__":
    f = open("data.txt")
    raw = f.readlines()
    f.close()

    data_clean = clean_input(raw)
    pprint.pprint(data_clean)

    accumulator, ok = track_boot_code(data_clean)
    print("Accumulator: {} (was OK? {})".format(accumulator, ok))

    accumulator, ok = correct_boot_code(data_clean)
    print("Accumulator: {} (was OK? {})".format(accumulator, ok))
