with open(r"input.txt") as f:
    values = f.read().split('\n')
    fishes = values[0].split(",")
    fishes = [int(x) for x in fishes]

    # Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, 
    # while each other number decreases by 1 if it was present at the start of the day.

    for i in range(1, 81):
        fishes_to_add = 0
        for j in range(0, len(fishes)):
            new = fishes[j] - 1
            if not fishes[j]:
                fishes[j] = 6
                fishes_to_add += 1
            else:
                fishes[j] = new
        fishes.extend([8] * fishes_to_add)
        #print(f"After day {i}: {','.join(map(str, fishes))}")
    print(len(fishes))
        