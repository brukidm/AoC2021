with open(r"input.txt") as f:
    values = f.read().split('\n')
    fishes = values[0].split(",")
    fishes = [int(x) for x in fishes]

    fish_dict = dict.fromkeys(range(0, 9), 0)

    for fish in fishes:
        if fish in fish_dict.keys():
            fish_dict[fish] += 1
        else:
            fish_dict[fish] = 1
    
    print(sorted(fish_dict.keys()))
    
    for i in range(1, 257):
        for k in sorted(fish_dict.keys()):
            if k == 0:
                fishes_to_add = fish_dict[0]
            else:
                fish_dict[k-1] = fish_dict[k]
        fish_dict[8] = fishes_to_add
        fish_dict[6] += fishes_to_add
    print(sum(fish_dict.values()))
            
        