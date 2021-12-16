import heapq

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
    visited = set()
    queue = []
    heapq.heappush(queue, source)

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            dist[(x,y)] = float("inf")

    dist[source] = 0
    i = 0
    while True:
        node = heapq.heappop(queue)
        if node == (len(matrix)-1, len(matrix)-1):
            return dist

        minimum_value = dist[node]

        neighbours = get_adjacent_indices(node[0], node[1], len(matrix), len(matrix))
        for neighbour in neighbours:
            new_weight = minimum_value + matrix[neighbour[0]][neighbour[1]]
            old_weight = dist[neighbour]

            if new_weight < old_weight:
                dist[neighbour] = new_weight
                heapq.heappush(queue, neighbour)


with open(r"input.txt") as f:
    values = f.read().split('\n')

    matrix = []
    for value in values:
        one_row = []
        for c in value:
            one_row.append(int(c))
        matrix.append(one_row)

    new_matrix = matrix

    new_matrix = []
    for row in matrix:
        new_row = []
        for x in range(5):
            for i in row:
                new_value = (int(i) + x) % 9 if (int(i) + x) > 9 else (int(i) + x)
                new_row.append(new_value)
        new_matrix.append(new_row)
    
    for p in range(len(matrix) + 1, 5*len(matrix) + 1):
        last_row = new_matrix[-len(matrix)]
        new_row = []
        for i in last_row:
            new_value = (int(i) + 1) % 9 if (int(i) + 1) > 9 else (int(i) + 1)
            new_row.append(new_value)
        new_matrix.append(new_row)


    with open("2.txt", "w") as o:
        for x in range(len(new_matrix)):
            for y in range(len(new_matrix)):
                print(new_matrix[x][y], end="", file=o)
            print(file=o)
    
    dist = dijkstra(new_matrix, (0,0))
    print(dist[len(new_matrix)-1, len(new_matrix)-1])