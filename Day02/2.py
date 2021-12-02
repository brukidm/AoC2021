with open(r"input.txt") as f:
    values = f.read().split('\n')
    x, y = 0, 0
    aim = 0
    for value in values:
        move = value.split(" ")
        if move[0] == "forward":
            x += int(move[1])
            y += aim * int(move[1])
        elif move[0] == "down":
            aim += int(move[1])
        else:
            aim -= int(move[1])
    print(x*y)