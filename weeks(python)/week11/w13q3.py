def greedy_vertex_cover(graph):
    visited_edges = set()
    cover = set()

    # Convert edge list to set of unique edges (u, v)
    edges = set()
    for u in graph:
        for v in graph[u]:
            if (v, u) not in edges:
                edges.add((u, v))

    while edges:
        # Pick any edge (u, v)
        u, v = edges.pop()

        # Add both u and v to the cover
        cover.add(u)
        cover.add(v)

        # Remove all edges incident to u or v
        edges = {e for e in edges if u not in e and v not in e}

    return cover

# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

cover = greedy_vertex_cover(graph)
print("Approximate Vertex Cover:", cover)
