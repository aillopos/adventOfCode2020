#!/usr/bin/env python3

import numpy as np

data = np.loadtxt("map.txt", dtype=str, comments=None)

width = len(data[0])


def count_trees(dx, dy):
    tree_no = 0
    x = y = 0

    tree = '#'

    while y < len(data):
        if data[y][x % width] is tree:
            tree_no += 1
        x += dx
        y += dy
    return tree_no


trees_on_path = []
delta_x = 1
delta_y = 1
trees_on_path.append(count_trees(delta_x, delta_y))
print('number of encountered trees (dx={}, dy={}): {}'.format(delta_x, delta_y, trees_on_path[0]))
delta_x = 3
delta_y = 1
trees_on_path.append(count_trees(delta_x, delta_y))
print('number of encountered trees (dx={}, dy={}): {}'.format(delta_x, delta_y, trees_on_path[1]))
delta_x = 5
delta_y = 1
trees_on_path.append(count_trees(delta_x, delta_y))
print('number of encountered trees (dx={}, dy={}): {}'.format(delta_x, delta_y, trees_on_path[2]))
delta_x = 7
delta_y = 1
trees_on_path.append(count_trees(delta_x, delta_y))
print('number of encountered trees (dx={}, dy={}): {}'.format(delta_x, delta_y, trees_on_path[3]))
delta_x = 1
delta_y = 2
trees_on_path.append(count_trees(delta_x, delta_y))
print('number of encountered trees (dx={}, dy={}): {}'.format(delta_x, delta_y, trees_on_path[4]))
print('product: {}'.format(np.prod(trees_on_path)))
