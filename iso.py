from collections import defaultdict, deque
from sage.rings.integer import Integer


def BFS(g, root):
    level = {}
    parent = {}

    for v in g.vertices():
        level[v] = None
        parent[v] = None

    level[root] = 0
    q = deque([root])
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in g.neighbors(u):
            if level[v] is None:
                level[v] = level[u] + 1
                parent[v] = u
                q.append(v)

    return order, parent


def edge_isoperimetric_number_of_tree(g):
    if not g.is_tree():
        raise ValueError("this algorithm only works for trees")

    iso = {}

    root = g.random_vertex()
    order, parent = BFS(g, root)
    children = defaultdict(set)
    for u, v in parent.viewitems():
        children[v].add(u)
    for v in order[::-1]:
        iso[v] = 1 + sum(iso[u] for u in children[v])

    k = max(min(iso[v], iso[root] - iso[v]) for v in order)
    return Integer(1) / k
