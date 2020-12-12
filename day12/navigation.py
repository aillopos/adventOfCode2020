#!/usr/bin/env python3

from pprint import pprint
from re import compile

ACTION_N = "N"
ACTION_E = "E"
ACTION_S = "S"
ACTION_W = "W"
ACTION_F = "F"
ACTION_R = "R"
ACTION_L = "L"

EAST_WEST = "EW"
NORTH_SOUTH = "NS"
HEADING = "heading"

TURN = {0: ACTION_N, 1: ACTION_E, 2: ACTION_S, 3: ACTION_W}

NAVIGATION_TRANSLATION = {
    ACTION_N: lambda x: x,
    ACTION_S: lambda x: -x,
    ACTION_E: lambda x: x,
    ACTION_W: lambda x: -x,
    ACTION_R: lambda x: x / 90,
    ACTION_L: lambda x: -x / 90,
}


def read_input(filename):
    regex = compile(r"^([EFLNRSW])(\d+)$")

    fd = open(filename, 'r')
    formatted = []
    for line in fd:
        line = line.strip()
        line_split = list(filter(None, regex.split(line)))
        formatted.append([line_split[0], int(line_split[1])])
    fd.close()

    return formatted


def move_direction(ins, total):
    if ins[0] in [ACTION_N, ACTION_S]:
        total[NORTH_SOUTH] += NAVIGATION_TRANSLATION[ins[0]](ins[1])
    elif ins[0] in [ACTION_E, ACTION_W]:
        total[EAST_WEST] += NAVIGATION_TRANSLATION[ins[0]](ins[1])
    elif ins[0] in [ACTION_R, ACTION_L]:
        total[HEADING] = (total[HEADING] + NAVIGATION_TRANSLATION[ins[0]](ins[1])) % 4


def get_total_instruction_ferry(instructions):
    total = {
        EAST_WEST: 0,
        NORTH_SOUTH: 0,
        HEADING: 1
    }

    for ins in instructions:
        if ins[0] == ACTION_F:
            move_direction([TURN[total[HEADING]], ins[1]], total)
        else:
            move_direction(ins, total)

    return abs(total[EAST_WEST]) + abs(total[NORTH_SOUTH])


def turn(ins, position):
    quadrant = ins[1] / 90 % 4
    if quadrant % 2 == 0:
        position[EAST_WEST] *= -1
        position[NORTH_SOUTH] *= -1
    else:
        sign = 1 if ins[0] == ACTION_R else -1
        ew = position[EAST_WEST]
        position[EAST_WEST] = int(sign * (-1) ** int(quadrant / 2) * position[NORTH_SOUTH])
        position[NORTH_SOUTH] = int(-1 * sign * (-1) ** int(quadrant / 2) * ew)


def get_total_instruction_waypoint(instructions):
    ferry = {
        EAST_WEST: 0,
        NORTH_SOUTH: 0,
    }
    waypoint = {
        EAST_WEST: 10,
        NORTH_SOUTH: 1,
    }

    for ins in instructions:
        if ins[0] == ACTION_F:
            direction = ACTION_N if waypoint[NORTH_SOUTH] > 0 else ACTION_S
            move_direction([direction, ins[1] * abs(waypoint[NORTH_SOUTH])], ferry)
            direction = ACTION_E if waypoint[EAST_WEST] > 0 else ACTION_W
            move_direction([direction, ins[1] * abs(waypoint[EAST_WEST])], ferry)
        elif ins[0] in [ACTION_R, ACTION_L]:
            turn(ins, waypoint)
        else:
            move_direction(ins, waypoint)

    return abs(ferry[EAST_WEST]) + abs(ferry[NORTH_SOUTH])


if __name__ == "__main__":
    data = read_input("data.txt")
    total_fields = get_total_instruction_ferry(data)
    print("total fields to move: {}".format(total_fields))
    total_fields = get_total_instruction_waypoint(data)
    print("total fields to move with waypoint: {}".format(total_fields))
