import sys
import collections

infinite = float('inf')


def normalize(entrances, exits, path):
    length = len(path)
    new_length = length + 2
    new_path = [[0 for i in range(new_length)] for j in range(new_length)]

    for i in range(length):
        for j in range(length):
            new_path[i+1][j+1] = path[i][j]

    for entrance in entrances:
        new_path[0][entrance+1] = infinite
    for eexit in exits:
        new_path[eexit+1][new_length-1] = infinite

    return new_path


def breadth_first_search(normalized_network, source, sink, parent):
    # trying to find a path from source to sink where every c(u, v) > 0 (capacity between vertices)
    # returns true if there is a path from source 's' to sink 't'
    # stores path in parent[]

    # all vertices start as not visited
    visited = [False] * len(normalized_network)

    # queue for BFS
    queue = collections.deque()

    # source node in enqueued and marked as visited
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.popleft()

        # Get all adjacent vertices of the dequeued vertex u
        # If an adjacent has not been visited, then mark it
        # visited and enqueue it
        for ind, val in enumerate(normalized_network[u]):
            if (visited[ind] is False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    # If we reached sink in BFS starting from source, then return
    # true, else false
    return visited[sink]


def edmonds_karp(normalized_network, source, sink):

    # This array is filled by BFS and to store path
    parent = [-1] * len(normalized_network)

    max_flow = 0  # There is no flow initially

    # Augment the flow while there is path from source to sink
    while breadth_first_search(normalized_network, source, sink, parent):

        # Find minimum residual capacity of the edges along the
        # path filled by BFS. Or we can say find the maximum flow
        # through the path found.
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, normalized_network[parent[s]][s])
            s = parent[s]

        # Add path flow to overall flow
        max_flow += path_flow

        # update residual capacities of the edges and reverse edges
        # along the path
        v = sink
        while v != source:
            u = parent[v]
            normalized_network[u][v] -= path_flow
            normalized_network[v][u] += path_flow
            v = parent[v]

    return max_flow


# https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm#Algorithm
# https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm
# https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
# https://en.wikipedia.org/wiki/Breadth-first_search

def solution(entrances, exits, path):
    normalized_network = normalize(entrances, exits, path)
    return edmonds_karp(normalized_network, 0, len(normalized_network)-1)


if __name__ == '__main__':
    entrances = [0, 1]
    exits = [4, 5]
    path = [
        [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
        [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
        [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
        [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
        [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
        [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
    ]

    # normalized_network = normalize(entrances, exits, path)
    #
    # maximum_flow = edmonds_karp(normalized_network, 0, (len(normalized_network)-1))
    #
    # print(f'max_flow is {maximum_flow}')

    print(solution(entrances, exits, path))


