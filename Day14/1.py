from collections import Counter

with open(r"input.txt") as f:
    polymer = f.readline().strip()
    f.readline()

    values = f.read().split("\n")

    rules = {}
    for value in values:
        k, v = value.split(" -> ")
        rules[k] = v

    for i in range(10):
        new_polymer = ""
        for i in range(len(polymer)-1):
            if polymer[i] and polymer[i+1]:
                a = polymer[i]
                b = polymer[i+1]
                if i == 0:
                    new_polymer += a
                new_polymer += rules[a+b] + b

        polymer = new_polymer
    
    max_char = max(polymer, key=polymer.count)
    min_char = min(polymer, key=polymer.count)

    c = Counter(polymer)
    print(c[max_char] - c[min_char])
