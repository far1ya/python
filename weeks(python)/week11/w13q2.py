import itertools

def tsp_brute_force(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    min_path = float('inf')
    best_route = []

    for perm in itertools.permutations(cities[1:]):
        current_path = [0] + list(perm) + [0]
        current_distance = sum(distance_matrix[current_path[i]][current_path[i + 1]] for i in range(n))
        if current_distance < min_path:
            min_path = current_distance
            best_route = current_path

    return min_path, best_route

# Example
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cost, path = tsp_brute_force(distance_matrix)
print(f"Minimum cost: {cost}")
print(f"Path: {path}")
