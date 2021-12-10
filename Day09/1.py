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


with open(r"input.txt") as f:
    values = f.read().split('\n')

    matrix = []

    for value in values:
        row = []
        for c in value:
            row.append(c)
        matrix.append(row)

    total = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            adjs = get_adjacent_indices(i, j, len(matrix), len(matrix[i]))
            lower = True
            for cell in adjs:
                if int(matrix[i][j]) >= int(matrix[cell[0]][cell[1]]):
                    lower = False

            if lower:
                res = int(matrix[i][j]) + 1
                total += res
    print(total)