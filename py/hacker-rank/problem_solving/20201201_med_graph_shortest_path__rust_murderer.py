#!/bin/python3

import os
import sys


# https://www.hackerrank.com/challenges/rust-murderer/problem

#
# The map of the city is a graph consisting N nodes (labeled 1 to N)
# where a specific given node S represents the current position of Rust and
# the rest of the nodes denote other places in the city,
# and an edge between two nodes is a main road between two places in the city.
# It can be suitably assumed that an edge that doesn't exist/isn't shown on the map is a village road (side lane).
# That means, there is a village road between two nodes a and b iff(if and only if) there is no city road between them.
#
# In this problem, distance is calculated as number of village roads (side lanes) between any two places in the city.
#
# Rust wants to calculate the shortest distance from his position (Node S) to
# all the other places in the city if he travels only using the village roads (side lanes).
#
# Sample 0
# n = 4
# S = node(1)
# city roads:
# 1 2
# 2 3
# 1 4
# output:
# 3 1 2
# The distance from 1 to 2 is 3. Path: 1 -> 3 -> 4 -> 2
# The distance from 1 to 3 is 1. Path: 1 -> 3
# The distance from 1 to 4 is 2. Path: 1 -> 3 -> 4
#
# Sample 1
# n: 4
# s: 2
# roads:
# [[1, 2], [2, 3]]
# expected output
# 2 2 1
#   1-2-3
#   start 2
#   2->[4]
#   4->[1,3]

# *** Result Summary ***
#   Implemented the obvious solutions first (finding the inverse of the graph for the village roads, then BFS
#       to find shortest path - see: rustMurderer__n2_timeout). This timed out. I had a guess that runtime would
#       be n^2 since we were visiting lots of nodes. Read on Wikipedia and confirmed that O(V + E) runtime, with
#       E = n (n-1) / 2 for a fulling connected graph, which is close to what the inverse graph would be with the
#       original being sparse.
#
#   Attempt 2: intuition that walking the sparse graph would be faster, and finding the inverse at each level.
#       was fuzzy on how to find the inverse at each level, and it was more complex that I originally though.
#       (see: rustMurderer_inverse_attempt_01). The rails eventually came off and I had to walk away.
#
#   Attempt 3: v2 of the "walk the original graph but find the inverse". Drew it out on paper with a more complex graph.
#       Ended up with:
#       - track unvisited nodes (unvisited "village" nodes, the inverse)
#       - walk the main road graph G
#       - current_level_nodes = main road walk current level
#       - foreach node at current level, find connected nodes, filter/intersect with unvisited
#       - visited nodes = unvisited.diff(connected)
#       - log depth of the current level for visited nodes
#       - remove visited nodes from unvisited
#       - add visited nodes to the next_current_level collection
#       - when current_level is exhausted, switch to the next_current_level
#
# Overall, this took almost 1hr per attempt, not great... should have walked away from attempt #2 quicker.

def rustMurderer(n, s, roads):
    '''
    :param s: the start node of Detective Rust
    :param n: number of nodes
    :param roads: array of int[2] (node_ids with city roads between)
    :return: array of distances (ints) from S to all other Nodes
    '''

    # I don't think I thought through the "inverse" strategy completely, starting again
    # probably should try to do this between 2-5pm... :(
    #
    # example 0
    # s = 1
    # 1 -2  -3
    #   -4
    # ** current_level = [1], depth = 1 **
    # unvisited = [2,3,4]
    # active = 1
    # conn = 2,4 . unvisited = 2,4
    # next = (unvisited).diff(conn) = (3)
    # depths = {3:1}
    # unvisited = unvisited - depths.keys = [2,4]
    #
    # ** current_level = next(all) = [3], depth = 2 **
    # active = 3
    # conn = 2 . unvisited = 2
    # next = (unvisited).diff(conn) = 4
    # depths = {3:1, 4:2}
    # unvisited = [2]
    #
    # ** current_level = [4], depth = 3 **
    # conn () . unvisited = ()
    # next = (unvisited).diff(()) = 2
    # depths = {3:1, 4:2, 2:3}
    # unvisited = []


    # example X1
    # s = 1
    # 1 -2  -3  -5  -7
    #   -3
    #   -4
    #   -6
    #   -7
    #
    # 1 -5  -2  -7
    #       -4  -3
    #       -6
    #
    # depths = {}
    # unvisited = [2,3,4,5,6,7]
    # ** curr_level = [1], depth = 1 **
    # next_level = []
    # for active in curr_level
    #   active = 1
    #   conn = [2,3,4,6,7] . unvisited = [2,3,4,6,7]
    #   next_level = [unvisited]-[conn] = [5]
    #   depths += {[next_level]: depth} = {5:1}
    #   unvisited -= next_level = [2,3,4,6,7]
    #
    # ** curr_level = [5], depth = 2, unvisited = [2,3,4,6,7] **
    # next_level = []
    # for active in curr_level
    #   active = 5
    #   conn = [3,7] . unvisited = [3,7]
    #   next_level = [unvisited]-[conn] = [2,4,6]
    #   depths += {[next_level]:depth} = {5:1, [2,4,6]:2}
    #   unvisited -= next_level = [3,7]
    #
    # ** curr_level = [2,4,6], depth=3, unvisited = [3,7] **
    # next_level = []
    # for active in curr_level
    #   active = 2
    #   conn = [3] . unvisited = [3]
    #   next_level = [unvisited]-[conn] = [7]
    #   depths += {[next_level]:depth} = {5:1, [2,4,6]:2, 7:3}
    #   unvisited -= next_level = [3]
    #   ---
    #   active = 4
    #   conn = [] . unvisited = []
    #   next_level = unvisited-conn = [3]
    #   depths += {[next_level]:depth} = {5:1, [2,4,6]:2, 7:3, 3:3}
    #   unvisited -= next_level = []
    #
    #   unvisited empty, break;

    print(f"n: {n}")
    print(f"s: {s}")
    print(f"roads:\n{roads}")

    # map existing roads with fast lookup
    road_map = {}
    for r in roads:
        # roads are unidirectional, log for each node of the road (edge)
        n1 = r[0]
        n2 = r[1]

        if n1 in road_map:
            road_map[n1].add(n2)
        else:
            road_map[n1] = {n2}

        if n2 in road_map:
            road_map[n2].add(n1)
        else:
            road_map[n2] = {n1}

    # node IDs start at 1
    unvisited_nodes = set(range(1, n + 1))
    unvisited_nodes.remove(s)

    # could use Ordered Dictionary, but we'll just brute force sort at the end
    node_depths = {}
    current_level = [s]
    depth = 0
    while len(current_level) > 0:
        depth += 1
        next_level = []

        for active_node in current_level:
            connected_nodes = set()
            if active_node in road_map:
                connected_nodes = road_map[active_node].intersection(unvisited_nodes)

            # village roads are the inverse of the main roads (the connected edges)
            visited_nodes = unvisited_nodes - connected_nodes
            next_level += list(visited_nodes)

            # remove the connected nodes
            unvisited_nodes = unvisited_nodes - visited_nodes

            # log depth
            for _n in visited_nodes:
                node_depths[_n] = depth

        current_level = next_level


    result = []
    node_depth_keys_sorted = sorted(node_depths.keys())
    for _n in node_depth_keys_sorted:
        result.append(node_depths[_n])

    return result


def rustMurderer_inverse_attempt_01(n, s, roads):
    '''
    :param s: the start node of Detective Rust
    :param n: number of nodes
    :param roads: array of int[2] (node_ids with city roads between)
    :return: array of distances (ints) from S to all other Nodes
    '''

    # first attempt (rustMurderer__n2_timeout) inverted the edges to create the "village roads",
    # but, since the graph is SPARSE, then the village road graph is dense, so we get n^2 running time
    #   I though that maybe with 10^5 nodes, it wouldn't timeout, but python is slow??
    #
    # must have to use the fact that the city roads are sparse in order to optimize?
    #
    # example 0
    # s = 1
    # 1 -2  -3
    #   -4
    # actives = 1
    # active = 1
    # next = 2,4
    # depth = 1
    # log depths: !s & !active & !next & !depths = !1 & !(2,4) & !() = 3
    # depths: {3:1}
    #
    # *** actives = [2,4] ***
    # active = 2
    # next = 3
    # depth = 2
    # log depths: !s & !active & !next & !depths = !1 & !(2) & !(3) & !(3) = 4
    # depths: {3:1, 4:2}
    # --
    # active = 4
    # next = []
    # depth = 2
    # log depths: !s & !active & !next & !depths = !1 & !(4) & !() & !(3,4) = (2)
    # depths: {3:1, 4:2}
    #
    # *** actives = [3], depth = 3 ***
    # active = 3
    # next = [2]
    # log depths: !s & !active & !next & !depths = !1 & !3 & !(2) & !(3,4) = ()
    #
    # no next, at end, all other nodes last depth
    # depth {3:1, 4:2, 2:3}

    print(f"n: {n}")
    print(f"s: {s}")
    print(f"roads:\n{roads}")

    # map existing roads with fast lookup
    road_map = {}
    for r in roads:
        # roads are unidirectional, log for each node of the road (edge)
        n1 = r[0]
        n2 = r[1]

        if n1 in road_map:
            road_map[n1].add(n2)
        else:
            road_map[n1] = {n2}

        if n2 in road_map:
            road_map[n2].add(n1)
        else:
            road_map[n2] = {n1}

    # node IDs start at 1
    unvisited_nodes = set(range(1, n + 1))
    unvisited_nodes.remove(s)

    all_nodes = set(unvisited_nodes)

    # could use Ordered Dictionary, but we'll just brute force sort at the end
    node_depths = {}
    active_nodes = [s]
    depth = 0
    while len(active_nodes) > 0:
        depth += 1
        next_nodes = []
        # bfs, find next set of unvisited nodes that don't have a main road to `node`
        for active_node in active_nodes:
            connected_nodes = []
            for unvisited in unvisited_nodes:
                if active_node in road_map and unvisited in road_map[active_node]:
                    connected_nodes.append(unvisited)

            # log depths using "inverse" of connected
            # = !s & !active & !next & !depths
            village_nodes = all_nodes \
                .difference([active_node]) \
                .difference(connected_nodes) \
                .difference(node_depths)

            for _n in village_nodes:
                node_depths[_n] = depth

            # remove the connected nodes, add them to the next_nodes result
            for connected_node in connected_nodes:
                unvisited_nodes.remove(connected_node)
                next_nodes.append(connected_node)

        active_nodes = next_nodes

    # add remaining
    village_nodes = all_nodes \
        .difference(node_depths)

    for _n in village_nodes:
        node_depths[_n] = depth

    result = []
    node_depth_keys_sorted = sorted(node_depths.keys())
    for _n in node_depth_keys_sorted:
        result.append(node_depths[_n])

    return result


def rustMurderer__n2_timeout(n, s, roads):
    '''
    :param s: the start node of Detective Rust
    :param n: number of nodes
    :param roads: array of int[2] (node_ids with city roads between)
    :return: array of distances (ints) from S to all other Nodes
    '''

    # each node is guaranteed to connect to all other nodes by village roads
    # no weighting, so probably can use BFS? -> ~n^2

    # *** algo ***
    # set active_nodes = [s], depth = 0
    # node_depths = { n: depth }

    # * OOPS - this loop isn't quite right, but the general idea is...*
    # while unvisited nodes:
    #   next_active_nodes = []
    #   for n in active_nodes:
    #       find all unvisited nodes that connect to n (that don't have a city road)
    #           - hash set lookup of some sort? Set of sets?
    #       add to next_active_nodes
    #       remove from unvisited
    #
    #   if depth > 0:
    #       record distance for active_nodes at depth
    #   depth++
    #   active_nodes = next_active_nodes
    # * /OOPS *

    # - its RECURSIVE, so maybe a stack of some sort?
    #       - nope, because it's BFS, we find all the next depth of nodes at once
    # - loop on if we have any active nodes
    # while active_nodes:
    #   if depth > 0:
    #       record distance for active_nodes at depth
    #
    #   next_active_nodes = []
    #   for n in active_nodes:
    #       find all unvisited nodes that connect to n (that don't have a city road)
    #           - hash set lookup of some sort? Set of sets?
    #       add to next_active_nodes
    #       remove from unvisited
    #
    #   active_nodes = next_active_nodes
    #   depth++
    #
    # return node_depths:depth - sorted by node id

    print(f"n: {n}")
    print(f"s: {s}")
    print(f"roads:\n{roads}")

    # map existing roads with fast lookup
    road_map = {}
    for r in roads:
        # roads are unidirectional, log for each node of the road (edge)
        n1 = r[0]
        n2 = r[1]

        if n1 in road_map:
            road_map[n1].add(n2)
        else:
            road_map[n1] = {n2}

        if n2 in road_map:
            road_map[n2].add(n1)
        else:
            road_map[n2] = {n1}

    # node IDs start at 1
    unvisited_nodes = set(range(1, n + 1))
    unvisited_nodes.remove(s)
    # could use Ordered Dictionary, but we'll just brute force sort at the end
    node_depths = {}
    active_nodes = [s]
    depth = 0
    while len(active_nodes) > 0:
        if depth > 0:
            for _n in active_nodes:
                node_depths[_n] = depth

        next_nodes = []
        # bfs, find next set of unvisited nodes that don't have a main road to `node`
        for node in active_nodes:
            connected_nodes = []
            for unvisited in unvisited_nodes:
                if node not in road_map or unvisited not in road_map[node]:
                    connected_nodes.append(unvisited)

            # remove the connected nodes, add them to the next_nodes result
            for connected_node in connected_nodes:
                unvisited_nodes.remove(connected_node)
                next_nodes.append(connected_node)

        active_nodes = next_nodes
        depth += 1

    result = []
    node_depth_keys_sorted = sorted(node_depths.keys())
    for _n in node_depth_keys_sorted:
        result.append(node_depths[_n])

    return result


def _run_example_0():
    n = 4
    s = 1
    roads = [
        [1, 2],
        [2, 3],
        [1, 4]
    ]

    result = rustMurderer(n, s, roads)
    print(f"***result***\n{result}")


def _run_example_1():
    n = 4
    s = 2
    roads = [[1, 2], [2, 3]]

    result = rustMurderer(n, s, roads)
    print(f"***result***\n{result}")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        roads = []

        for _ in range(m):
            roads.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = rustMurderer(n, s, roads)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
