import copy

def adjac(ele, sub = []):
  if not ele:
     yield sub
  else:
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2)
                for idx in adjac(ele[1:], sub + [j])]


with open(r"input.txt") as f:
    values = f.read().split('\n')

    matrix = dict()
    for j in range(len(values)):
        for i in range(len(values[j])):
            matrix[(j,i)] = int(values[i][j])

    steps = 100
    i = 1
    while True:
        for k, v in matrix.items():
            matrix[k] = v + 1
        flashes = 0
        while True:
            temp_matrix = copy.deepcopy(matrix)
            for k, v in matrix.items():
                if matrix[k] > 9:
                    matrix[k] = 0
                    flashes += 1
                    for adj in adjac(k):
                        adj = tuple(adj)
                        if adj in matrix.keys() and matrix[adj] != 0:
                            matrix[adj] = matrix[adj] + 1

            if matrix == temp_matrix:
                break
            if flashes == len(matrix.values()):
                print(i)
                exit()
        i += 1
