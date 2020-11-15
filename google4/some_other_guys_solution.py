import itertools


def answer(times, time_limit):
    num_bunnies = len(times) - 2
    bunny_indices = [bunny + 1 for bunny in range(num_bunnies)]

    distance_matrix = complete_bellman_ford(times)
    if has_negative_cycle(distance_matrix):
        return range(num_bunnies)

    for width in range(num_bunnies, 0, -1):
        for perm in itertools.permutations(bunny_indices, width):
            cost = get_path_cost(perm, distance_matrix)
            if cost <= time_limit:
                return [bunny - 1 for bunny in sorted(perm)]

    return []


def get_path_cost(bunnies, distance_matrix):
    cost = 0
    for i in range(0, len(bunnies) - 1):
        _from = bunnies[i]
        _to = bunnies[i + 1]
        cost += distance_matrix[_from][_to]
    start_node = 0
    end_node = len(distance_matrix) - 1
    cost += distance_matrix[start_node][bunnies[0]]
    cost += distance_matrix[bunnies[-1]][end_node]
    return cost


def complete_bellman_ford(edges):
    distance_matrix = []
    for vertex in range(len(edges)):
        distances = bellman_ford(edges, vertex)
        distance_matrix.append(distances)
    return distance_matrix


def bellman_ford(edges, start):
    distances = [float('inf') for vertex in edges]
    distances[start] = edges[start][start]
    for i in range(len(edges)):
        for u, v, weight in enumerate_edges(edges):
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    return distances


def enumerate_edges(edges):
    for u, row in enumerate(edges):
        for v, weight in enumerate(row):
            yield (u, v, weight)


def has_negative_cycle(bellman_ford_matrix):
    distances = bellman_ford_matrix[0]
    for u, v, weight in enumerate_edges(bellman_ford_matrix):
        if distances[u] + weight < distances[v]:
            return True
    return False


def test(times, budget, expected):
    ans = answer(times, budget)
    print(expected, ans, ans == expected)


cases = [
        ([[0, 1, 1, 1, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [1, 1, 1, 0, 1],
          [1, 1, 1, 1, 0]], 3, [0, 1]),

        ([[0, 2, 2, 2, -1],
          [9, 0, 2, 2, -1],
          [9, 3, 0, 2, -1],
          [9, 3, 2, 0, -1],
          [9, 3, 2, 2, 0]], 1, [1, 2])
]


if __name__ == '__main__':
    for times, budget, expected in cases:
        test(times, budget, expected)

