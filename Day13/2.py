import numpy as np

with open(r"input.txt") as f:
    values = f.read().split('\n')

    max_x = 0
    max_y = 0

    coords = []
    folds = False
    manual = []
    for value in values:
        if not folds:
            if not value:
                folds = True
                continue

            x, y = [int(x) for x in value.split(",")]

            if x > max_x:
                max_x = x
            
            if y > max_y:
                max_y = y

            coords.append((x,y))
        else:
            coord, index = value.split(" ")[-1].split("=")
            manual.append((coord, int(index)))

    matrix = np.empty(shape=(max_y + 1, max_x + 1))
    matrix.fill(0)

    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) in coords:
                matrix[y][x] = "1"
    
    for entry in manual:
        if entry[0] == "x":
            if len(matrix[0]) % 2 != 0:
                matrix = np.delete(matrix, entry[1], 1)
            left_matrix, right_matrix = np.hsplit(matrix, 2)

            right_matrix = np.fliplr(right_matrix)

            for i in range(len(left_matrix)):
                for j in range(len(left_matrix[0])):
                    left_matrix[i][j] = left_matrix[i][j] or right_matrix[i][j]

            matrix = left_matrix
        else:
            if len(matrix) % 2 != 0:
                matrix = np.delete(matrix, entry[1], 0)
            top_matrix, bot_matrix = np.vsplit(matrix, 2)

            bot_matrix = np.rot90(bot_matrix, 2)
            bot_matrix = np.fliplr(bot_matrix)

            for i in range(len(bot_matrix)):
                for j in range(len(bot_matrix[0])):
                    top_matrix[i][j] = top_matrix[i][j] or bot_matrix[i][j]

            matrix = top_matrix
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("█" if matrix[i][j] else "░", end="")
        print()