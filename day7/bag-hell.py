#!/usr/bin/env python3

from re import compile, sub


def create_graph(raw):
    graph = {}
    for line in raw:
        line = sub(r"[\n\t]*", "", line)
        regex1 = compile(r"^([a-z]+ [a-z]+) bags contain (.*).$")
        first = list(filter(None, regex1.split(line)))

        if "no other bags." in first[1]:
            graph[first[0]] = None
            continue

        regex2 = compile(r"([0-9] [a-z]+ [a-z]+)")
        second = regex2.findall(first[1])
        graph[first[0]] = {}
        for s in second:
            regex3 = compile(r"^([0-9]) ([a-z]+ [a-z]+)$")
            entry = list(filter(None, regex3.split(s)))
            graph[first[0]][entry[1]] = int(entry[0])

    return graph


def get_bag_wrap(bag_color):
    for k in graph.keys():
        if bag_color in graph[k].keys():
            shiny_list.append(k)
            get_bag_wrap(k)


def get_bag_interior(bag_color, no):
    bags_in_no[0] += no
    if bag_color in graph.keys() and graph[bag_color]:
        for k in graph[bag_color].keys():
            get_bag_interior(k, no * graph[bag_color][k])


if __name__ == "__main__":
    f = open("data.txt")
    raw = f.readlines()
    f.close()

    graph = create_graph(raw)

    searched_color = "shiny gold"

    shiny_list = []
    get_bag_wrap(searched_color)
    print("Number of bags eventually containing {}: {}".format(searched_color, len(set(shiny_list))))

    bags_in_no = [0]
    get_bag_interior(searched_color, 1)
    print("Number of bags in my {} one: {}".format(searched_color, bags_in_no[0] - 1))
