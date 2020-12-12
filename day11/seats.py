#!/usr/bin/env python3

from copy import deepcopy
from pprint import pprint

rows = "rows"
cols = "cols"
empty = "L"
occupied = "#"
floor = "."


def read_input(filename):
    fd = open(filename, 'r')
    seat_plan = []
    for line in fd:
        line = line.strip()
        chars = []
        for c in line:
            chars.append(c)
        seat_plan.append(chars)
    fd.close()

    return seat_plan


def get_neighbor_seats(seats, ri, ci, row_col_no):
    neighbors = []
    neighbor_rows = [r for r in range(ri - 1, ri + 2) if 0 <= r < row_col_no[rows]]
    neighbor_cols = [c for c in range(ci - 1, ci + 2) if 0 <= c < row_col_no[cols]]
    for nri in neighbor_rows:
        for nci in neighbor_cols:
            if nri == ri and nci == ci:
                continue
            neighbors.append(seats[nri][nci])
    return neighbors


def get_first_seat_along_axis(seats, i, axis_len, increment):
    stop = axis_len if increment > 0 else -1
    for ni in range(i + increment, stop, increment):
        # print("len(seats[ni]): {}, i: {}, axis_len: {}, increment: {}, stop: {}, ni: {}".format(len(seats), i, axis_len, increment, stop, ni))
        if seats[ni] != floor:
            return seats[ni]
    return []


def get_first_seat_along_diagonal(seats, ri, ci, r_inc, c_inc, lim):
    for i in range(1, lim):
        if seats[ri + i * r_inc][ci + i * c_inc] != floor:
            return seats[ri + i * r_inc][ci + i * c_inc]


def get_visible_seats(seats, ri, ci, row_col_no):
    # search for next seat along row
    neighbors = [get_first_seat_along_axis(seats[ri], ci, row_col_no[cols], 1),
                 get_first_seat_along_axis(seats[ri], ci, row_col_no[cols], -1)]
    # search for next seat along column
    col = [r[ci] for r in seats]
    neighbors.append(get_first_seat_along_axis(col, ri, row_col_no[rows], 1))
    neighbors.append(get_first_seat_along_axis(col, ri, row_col_no[rows], -1))
    # search for next seat along diagonals
    neighbors.append(
        get_first_seat_along_diagonal(seats, ri, ci, +1, +1, min([row_col_no[rows] - ri, row_col_no[cols] - ci])))
    neighbors.append(
        get_first_seat_along_diagonal(seats, ri, ci, -1, +1, min([ri+1, row_col_no[cols] - ci])))
    neighbors.append(
        get_first_seat_along_diagonal(seats, ri, ci, +1, -1, min([row_col_no[rows] - ri, ci+1])))
    neighbors.append(
        get_first_seat_along_diagonal(seats, ri, ci, -1, -1, min([ri + 1, ci +1])))

    return neighbors


def change_state(seats_original, row_col_no, neighbor_func, occupied_limit):
    seats_changed = deepcopy(seats_original)
    changed = False

    for ri in range(row_col_no[rows]):
        for ci in range(row_col_no[cols]):
            if seats_original[ri][ci] == floor:
                continue
            neighbors = neighbor_func(seats_original, ri, ci, row_col_no)
            if seats_original[ri][ci] == empty and occupied not in neighbors:
                seats_changed[ri][ci] = occupied
                changed = True
            if seats_original[ri][ci] == occupied and neighbors.count(occupied) >= occupied_limit:
                seats_changed[ri][ci] = empty
                changed = True

    return changed, seats_changed


def reach_equilibrium(seat_plan, neighbor_func, occupied_limit):
    changed = True
    seat_plan_after = deepcopy(seat_plan)
    row_col_no = {
        rows: len(seat_plan),
        cols: len(seat_plan[0])
    }
    while changed:
        changed, seat_plan_after = change_state(seat_plan_after, row_col_no, neighbor_func, occupied_limit)

    flat_seat_plan = [s for r in seat_plan_after for s in r]
    return flat_seat_plan.count(occupied)


if __name__ == "__main__":
    data = read_input("data.txt")
    occupied_seats = reach_equilibrium(data, get_neighbor_seats, 4)
    print("part I: number of occupied seats: {}".format(occupied_seats))
    occupied_seats = reach_equilibrium(data, get_visible_seats, 5)
    print("part II: number of occupied seats: {}".format(occupied_seats))
