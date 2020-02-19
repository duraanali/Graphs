
from collections import defaultdict


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def dfs(starting_vertex, family):
    visited = []
    s = Stack()
    s.push([starting_vertex])
    while s.size() > 0:
        path = s.pop()
        v = path[-1]
        if v not in visited:
            visited.append(v)
        for neighbor in family[v]:
            path_copy = [*path]
            path_copy.append(neighbor)
            s.push(path_copy)
    return visited[-1]


def earliest_ancestor(ancestors, starting_node):
    family = defaultdict(list)
    for parent, child in ancestors:
        family[child].append(parent)
    if starting_node not in family:
        return -1
    ancestor = dfs(starting_node, family)
    return ancestor
