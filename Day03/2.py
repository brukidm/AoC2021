from statistics import mode


def remove_elements(matrix, column, type):
    if len(matrix) == 1:
        return "".join(matrix[0])

    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    most_common = mode(transposed_matrix[column])

    count_zeros = transposed_matrix[column].count("0")
    count_ones = transposed_matrix[column].count("1")

    if type == "oxy":
        if count_zeros == count_ones:
            most_common = 1
    else:
        most_common = 1 - int(most_common)
        if count_zeros == count_ones:
            most_common = 0
    
    new_matrix = []
    for entry in matrix:
        if entry[column] == str(most_common):
            new_matrix.append(entry)
    return remove_elements(new_matrix, column + 1, type)

with open(r"input.txt") as f:
    values = f.read().split('\n')

    matrix = []
    for value in values:
        matrix.append(list(value))

    # find oxygen
    oxy = remove_elements(matrix, 0, "oxy")
    # find co2
    co2 = remove_elements(matrix, 0, "co2")
    print(int(oxy, 2) * int(co2, 2))






