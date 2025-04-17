class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(vertices)

    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

# Example usage
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 6),
    ('C', 'D', 4),
    ('C', 'E', 2),
    ('D', 'E', 5)
]

mst, total = kruskal(vertices, edges)
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")
print(f"Total weight of MST: {total}")
