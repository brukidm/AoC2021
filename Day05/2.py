def get_range(start, end):
    if start > end:
        return range(start, end-1, -1)
    else:
        return range(start, end+1)

def get_diagonal_points(x_start, y_start, x_end, y_end):
    if x_start > x_end:
        x_start, y_start, x_end, y_end = x_end, y_end, x_start, y_start

    result = []
    slope = (y_end - y_start) // (x_end - x_start)
    for i, j in zip(range(x_start, x_end), range(y_start, y_end, slope)):
        result.append((i, j))
    result.append((x_end, y_end))  # add end point
    return result

with open(r"input.txt") as f:
    values = f.read().split('\n')

    matrix = {}

    for value in values:
        start, end = value.split(" -> ")
        x_start, y_start = start.split(",")
        x_end, y_end = end.split(",")

        x_start, y_start, x_end, y_end = int(x_start), int(y_start), int(x_end), int(y_end)

        # horizontal
        if x_start == x_end or y_start == y_end:
            xs = get_range(x_start, x_end)
            ys = get_range(y_start, y_end)
            for x in xs:
                for y in ys:
                    if (x, y) not in matrix.keys():
                        matrix[(x, y)] = 1
                    else:
                        matrix[(x, y)] += 1
            continue

        # diagonal
        else:
            coords = get_diagonal_points(x_start, y_start, x_end, y_end)
            for coord in coords:
                if coord not in matrix.keys():
                    matrix[coord] = 1
                else:
                    matrix[coord] += 1
        

    count = 0
    for v in matrix.values():
        if v > 1:
            count += 1
    print(count)
