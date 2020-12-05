#!/usr/bin/env python3

import numpy as np
from re import compile

data = np.loadtxt("data.txt", dtype=str)
row_max = 127
col_max = 7


def get_row_column_from_id(seat_chars, max_possible):
    sr_lower_bound = 0
    sr_max_1 = max_possible + 1
    for s in seat_chars:
        if s == 'F' or s == 'L':
            sr_max_1 = sr_max_1 - (sr_max_1 - sr_lower_bound) / 2
        elif s == 'B' or s == 'R':
            sr_lower_bound = sr_lower_bound + (sr_max_1 - sr_lower_bound) / 2
        else:
            raise ValueError("seat ID not 'B' nor 'F'!")
    return int(sr_lower_bound)


def calculate_unique_id(row, col):
    return row * 8 + col


def get_coordinates_from_id(seat_id):
    return int(seat_id / 8), seat_id % 8


def is_my_seat(my_row, my_col):
    my_id = calculate_unique_id(my_row, my_col)
    could_be_mine = False
    if my_id <= 0:
        could_be_mine = seat_layout[get_coordinates_from_id(my_id + 1)]
    if my_id >= row_max * 8 + col_max:
        could_be_mine = seat_layout[get_coordinates_from_id(my_id - 1)]
    else:
        could_be_mine = seat_layout[get_coordinates_from_id(my_id - 1)] and seat_layout[
            get_coordinates_from_id(my_id + 1)]
    return could_be_mine


max_found = 0

seat_layout = np.zeros((row_max + 1, col_max + 1), dtype=bool)

for seat in data:
    p = compile(r"^([BF]{7})([LR]{3})$")
    seat_ids = list(filter(None, p.split(seat)))
    seat_row = get_row_column_from_id(seat_ids[0], row_max)
    seat_col = get_row_column_from_id(seat_ids[1], col_max)
    unique_id = calculate_unique_id(seat_row, seat_col)
    max_found = unique_id if unique_id > max_found else max_found

    seat_layout[seat_row, seat_col] = True

print("maximum unique set ID: {}".format(max_found))

for ix in range(seat_layout.shape[0]):
    for iy in range(seat_layout.shape[1]):
        if not seat_layout[ix, iy]:
            is_mine = is_my_seat(ix, iy)
            if is_mine:
                print("my seat: row {}, col {}, id {}".format(ix, iy, calculate_unique_id(ix, iy)))
