with open(r"input.txt") as f:
    values = f.read().split('\n')
    prev_value = None
    total = 0
    for value in values:
        if prev_value and prev_value < int(value):
            total += 1
        prev_value = int(value)
    print(total)