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

def search_basins(i, j, result=None):
    adjs = get_adjacent_indices(i, j, len(matrix), len(matrix[i]))
    if not result:
        result = [(i, j)]

    for cell in adjs:
        if (int(matrix[i][j]) < int(matrix[cell[0]][cell[1]]) 
        and int(matrix[cell[0]][cell[1]]) != 9 
        and (cell[0],cell[1]) not in result):
            result.append((cell[0], cell[1]))
            search_basins(cell[0], cell[1], result)
    return result

with open(r"input.txt") as f:
    values = f.read().split('\n')

    matrix = []

    for value in values:
        row = []
        for c in value:
            row.append(c)
        matrix.append(row)

    lowest_points = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            adjs = get_adjacent_indices(i, j, len(matrix), len(matrix[i]))
            lower = True
            for cell in adjs:
                if int(matrix[i][j]) >= int(matrix[cell[0]][cell[1]]):
                    lower = False

            if lower:
                lowest_points.append((i, j))
    
    basins = []
    for point in lowest_points:
        basins.append(search_basins(point[0], point[1]))

    basins = sorted(basins, key=len)
    total = 1
    for basin in basins[-3:]:
        total = total * len(basin)
    print(total)