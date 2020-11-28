#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/count-luck/problem
# maze solver, dfs

# summary
#   - straight DFS worked within time limits
#   - I didn't create any fancy data structures for nodes/edges, probably would have made the code
#       slightly more efficient
#
#   - error 1: I was "undoing" the decision in backtracking for the wrong node
#   - error 2: I assumed `.pop` worked from the start of a list, not the end

# Complete the countLuck function below.
def countLuck(matrix, k):
    '''
    Complete the countLuck function in the editor below. It should return a string, either  if Ron is correct or  if he is not.

    matrix: a list of strings, each one represents a row of the matrix
    k: an integer that represents Ron's guess

    Maze Sample (. open, X blocked, M start, * end)
    .X.X......X
    .X*.X.XXX.X
    .XX.X.XM...
    ......XXXX.

    solution (1 decision, 0 no decision)
    .X.X.10000X
    .X*0X0XXX0X
    .XX0X0XM01.
    ...100XXXX.

    count number of decisions, compare to guess k
    It is guaranteed that there is only one path from the starting location to the portkey

    ###
    depth first search
    - at each location,
    -   count unblocked options
    -       if 1 then take it
    -       if more than one, k++ (how do we handle decisions not part of final path -- need to k-- when walking back up the stack)
    -   find end (short circuit?), or first unblocked direction (u, r, d, l)
    -       no unblocked direction?
    -           pop active node
    -           active node is decision? k--
    -   # assuming there always exists a solution, otherwise, handle that edge case

    runtime complexity
       NxM nodes = V
       each node has 4 edges
       edges E = v*4
       O(V + E)

    algo
    - visited_nodes = {node_id: Boolean} (or simple node_id Hash)
    - decision_nodes = {node_id: Boolean}
    - find M (start) x,y
    - node_id = 'x_y'
    -
    - while not at end:
    -   set active node_id (probably in a Stack, in python is just a list, pushed to front?)
    -   is end? done
    -
    -   log visited
    -   is blocked?
            - current node is_decision? k--
            - pop
    -   check is_decision_node?
    -       log
    -       k++
    -   set next active node to next unvisited
    '''

    path_stack = []
    visited_nodes = set()
    decision_nodes = set()
    active_node = _get_start_node(matrix)
    decision_count = 0

    while active_node is not None:
        # check if we are at end, if so, finished
        node_val = _get_node_val(active_node, matrix)
        if node_val == "*":
            break

        # log visited
        if active_node not in visited_nodes:
            visited_nodes.add(active_node)

        # find next move
        next_nodes = _get_next_nodes(active_node, visited_nodes, matrix)

        # blocked? go back
        if len(next_nodes) == 0:
            # did we log a decision at this node before, and now we're backtracking?
            #   then remove from our decision count
            if active_node in decision_nodes:
                decision_count -= 1
            active_node = path_stack.pop()

            # oops, we undo the decision if our CURRENT active node is a decision node,
            #   NOT the one we're going back to
            # did we log a decision at this node before, and now we're backtracking?
            #   then remove from our decision count
            # if active_node in decision_nodes:
            #     decision_count -= 1
            continue
        else:
            # oops, .pop goes from END of list
            # path_stack.insert(0, active_node)
            path_stack.append(active_node)

        # log if decision node
        if active_node not in decision_nodes and len(next_nodes) > 1:
            decision_nodes.add(active_node)
            decision_count += 1

        # take first node as next active node
        active_node = next_nodes[0]

    print(f"decision count: {decision_count}")

    if decision_count == k:
        return "Impressed"
    else:
        return "Oops!"


def _get_next_nodes(_node_id, _visited, _matrix):
    '''
    Gets the number of path decisions possible from a node

    :param _node_id:
    :param _visited:
    :param _matrix:
    :return:
    '''
    # check up/down/left/right
    all_next_node_ids = _get_all_next_node_id_options(_node_id)
    next_node_ids = []

    for n in all_next_node_ids:
        if _is_node_open(n, _visited, _matrix):
            next_node_ids.append(n)

    return next_node_ids


def _get_all_next_node_id_options(_node_id):
    up_node_id = (_node_id[0], _node_id[1] + 1)
    down_node_id = (_node_id[0], _node_id[1] - 1)
    left_node_id = (_node_id[0] - 1, _node_id[1])
    right_node_id = (_node_id[0] + 1, _node_id[1])

    return [up_node_id, down_node_id, left_node_id, right_node_id]



def _get_node_val(_node_id, _matrix):
    '''
    Gets the string value of the node_id in the matrix
    :param _node_id:
    :param _matrix:
    :return:
    '''
    # check bounds
    if _node_id[0] < 0 or \
            _node_id[0] >= len(_matrix[0]) or \
            _node_id[1] < 0 or \
            _node_id[1] >= len(_matrix):
        return None

    # array of arrays is in y, x indexing
    return _matrix[_node_id[1]][_node_id[0]]


def _is_node_open(_node_id, _visited, _matrix):
    '''
    True if the node has not been visited AND is not an 'X'

    :param _node_id:
    :param _visited:
    :param _matrix:
    :return:
    '''
    # if visited, then not an open direction
    if _node_id in _visited:
        return False

    node_val = (_get_node_val(_node_id, _matrix))
    if node_val is None or node_val == 'X':
        return False

    return True


def _get_start_node(_matrix):
    '''
    Gets the start ('M') node: (x, y)

    :param _matrix:
    :return: (x, y)
    '''
    start_node = None
    for y in range(len(_matrix)):
        for x in range(len(_matrix[y])):
            if _matrix[y][x] == 'M':
                start_node = (x, y)
                break
        if start_node is not None:
            break
    print(start_node)
    return start_node


test_matrix_00 = [
    "*.M",
    ".X."
]

test_matrix_01 = [
    ".X.X......X",
    ".X*.X.XXX.X",
    ".XX.X.XM...",
    "......XXXX."
]

test_matrix_03 = [
    "*..M..",
    ".X.X.X",
    "XXX..."
]


def run_test_case_1():
    countLuck(
        test_matrix_01,
        3)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
