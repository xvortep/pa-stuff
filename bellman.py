import math
from enum import Enum
from math import inf
from queue import Queue


class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """

    def __init__(self, p=None, d=None, name=None):
        """
        Vertex constructor
        @param p - parent
        @param d - distance
        @param n - name
        """
        self.p = p
        if d is None:
            self.d = math.inf
        else:
            self.d = d
        self.name = name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class Edge:
    """
    Graph vertex: A graph vertex (node) with data
    """

    def __init__(self, src=None, dst=None, w=None):
        """
        Edge constructor
        @param src - source vertex
        @param dst - destination vertex
        @param w - edge weight
        """
        self.u = src
        self.v = dst
        self.w = w

    def __str__(self):
        return str(self.name)


class Graph:
    def __init__(self, V=None, E=None):
        self.V = V
        self.E = E

    def __str__(self):
        s = ''
        for e in self.E:
            s += e.u.name + ' -> ' + e.v.name + ', w = ' + str(e.w) + '.\n'
        return s

    def initialize_single_source(self, s):
        for v in self.E:
            v.d = inf
            v.p = None
        s.d = 0

    def get_weight(self, u, v):
        for i in self.E:
            if i.u == u and i.v == v:
                return i.w
        return inf

    def relax(self, u, v):
        # print(u, v)
        if v.d > u.d + self.get_weight(u, v):
            v.d = u.d + self.get_weight(u, v)
            v.p = u

    def bellman_ford(self, s):
        self.initialize_single_source(s)
        for v in self.V:
            for e in self.E:
                self.relax(e.u, e.v)
        for e in self.E:
            if e.u.d > e.v.d + self.get_weight(e.u, e.v):
                return False

        return True

    def print_path(self, s, v):
        if v is s:
            print(s)
        elif v.p is None:
            print("No path from", s, "to", v, "exists")
        else:
            self.print_path(s, v.p)
            print(v)


def shortest_path(a, b, V, E):
    G = Graph(V, E)
    print(G)
    G.bellman_ford(a)
    G.print_path(a, b)
    print('dist from a to b is ', b.d)


if __name__ == "__main__":
    va = Vertex(name='a')
    vb = Vertex(name='b')
    vc = Vertex(name='c')
    vd = Vertex(name='d')
    ve = Vertex(name='e')
    vf = Vertex(name='f')

    V = [va, vb, vc, vd, ve, vf]

    e1 = Edge(va, vb, -6)
    e2 = Edge(va, vd, -4)
    e3 = Edge(vb, vc, 7)
    e4 = Edge(vc, vf, -3)
    e5 = Edge(vf, ve, 5)
    e6 = Edge(ve, vc, 13)
    e7 = Edge(va, ve, 15)
    e8 = Edge(vd, ve, 11)

    E = [e1, e2, e3, e4, e5, e6, e7, e8]

    shortest_path(va, ve, V, E)
