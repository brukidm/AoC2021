with open(r"input.txt") as f:
    values = f.read().split('\n')
    values = [int(i) for i in values]
    limit = len(values)
    total = 0
    prev_value = sum(values[0:3])
    i = 1
    while i < limit:
        value = sum(values[i:i+3])
        if prev_value < value:
            total += 1
        prev_value = value
        i += 1

    print(total)