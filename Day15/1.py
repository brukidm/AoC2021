def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices

def dijkstra(matrix, source):
    dist = {}
    prev = {}
    vertex_set = set()

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            vertex_set.add((int(x), int(y)))
            dist[(x,y)] = float("inf")
            prev[(x,y)] = None

    dist[source] = 0

    while vertex_set:
        minimum = min(dist, key=dist.get)
        vertex_set.remove(minimum)
        minimum_value = dist[minimum]

        neighbours = get_adjacent_indices(minimum[0], minimum[1], len(matrix), len(matrix))

        if minimum == (len(matrix)-1, len(matrix)-1):
            return dist, prev

        for neighbour in neighbours:
            if neighbour in vertex_set:
                alt = minimum_value + matrix[neighbour[0]][neighbour[1]]
                if alt < dist[neighbour]:
                    dist[neighbour] = alt
                    prev[neighbour] = minimum
        dist.pop(minimum)


    return dist, prev

with open(r"input.txt") as f:
    values = f.read().split('\n')

    matrix = []
    for value in values:
        one_row = []
        for c in value:
            one_row.append(int(c))
        matrix.append(one_row)
    
    dist, prev = dijkstra(matrix, (0,0))

    print(dist[(len(matrix)-1, len(matrix)-1)])