from collections import Counter
import math

with open(r"input.txt") as f:
    polymer = f.readline().strip()
    f.readline()

    values = f.read().split("\n")

    rules = {}
    for value in values:
        k, v = value.split(" -> ")
        rules[k] = v

    elements = {}
    for i in range(len(polymer)-1):
        if polymer[i] and polymer[i+1]:
            a = polymer[i]
            b = polymer[i+1]

            if a+b not in elements.keys():
                elements[a+b] = 1
            else:
                elements[a+b] += 1

    print(elements)

    for i in range(40):
        new_elements = {}

        for k in elements.keys():
            insert = rules[k]
            how_many = elements[k]

            left = k[0] + insert
            right = insert + k[1]

            
            if left not in new_elements.keys():
                new_elements[left] = how_many
            else:
                new_elements[left] += how_many

            if right not in new_elements.keys():
                new_elements[right] = how_many
            else:
                new_elements[right] += how_many
        elements = new_elements

    appearances = {}

    for key, value in elements.items():
        for c in key:
            if c not in appearances:
                appearances[c] = value
            else:
                appearances[c] += value

    min_value = 9999999999999999999999999
    max_value = 0
    print(appearances)
    for k, v in appearances.items():
        if v < min_value:
            min_value = v
            min_char = k
        
        if v > max_value:
            max_value = v
            max_char = k

    print(min_char, max_char)
    print(math.ceil(max_value/2) - math.ceil(min_value/2))
