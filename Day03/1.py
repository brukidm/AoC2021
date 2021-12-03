from statistics import mode

with open(r"input.txt") as f:
    values = f.read().split('\n')

    matrix = []
    for value in values:
        matrix.append(list(value))
    
    # transpose
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    gamma = ""
    epsilon = ""
    for column in matrix:
        common = mode(column)
        gamma += str(common)
        epsilon += "0" if int(common) else "1"
    
    print(int(gamma, 2) * int(epsilon, 2))
