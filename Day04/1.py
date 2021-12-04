import re

def find(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return (i, j)
    return None

def check_match(row):
    chars = "".join(row)
    if re.findall(r'x{5}', chars):
        return True

def play(numbers, tables):
    for number in numbers:
        for table in tables:
            coords = find(number, table)
            if coords:
                table[coords[0]][coords[1]] = "x"

            for row in table:
                if check_match(row):
                    return table, int(number)
            
            for i in range(len(table)):
                column = []
                for row in table:
                    column.append(row[i])

                if check_match(column):
                    return table, int(number)


with open(r"input.txt") as f:
    values = f.read().split('\n')

    numbers = values[0].split(",")
    
    tables = []
    table = []
    for row in values[2:]:
        if not row:
            tables.append(table)
            table = []
            continue
        table.append(re.findall(r'\s*(\s*\S+)', row.rstrip()))
    
    winner, winning_number = play(numbers, tables)

    total = 0
    for row in winner:
        for char in row:
            if char.isnumeric():
                total += int(char)

    print(total * winning_number)

