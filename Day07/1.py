with open(r"input.txt") as f:
    values = f.read().split('\n')
    values = [int(x) for x in values[0].split(",")]

    limit = max(values)

    minimum = 0
    for i in range(limit+1):
        total = 0
        for value in values:
            total += abs(value-i)
        
        if not minimum or minimum > total:
            minimum = total
    
    print(minimum)