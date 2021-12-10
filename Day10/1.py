with open(r"input.txt") as f:
    values = f.read().split('\n')

    weight = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    appearances = {
        ")": 0,
        "]": 0,
        "}": 0,
        ">": 0
    }

    for value in values:
        stack = []
        for char in value:
            if char in ["(", "[", "{", "<"]:
                stack.append(char)
            else:
                top_of_stack = stack.pop()
                valid = False
                if not (
                    (char == ")" and top_of_stack == "(") or
                    (char == "]" and top_of_stack == "[") or
                    (char == "}" and top_of_stack == "{") or
                    (char == ">" and top_of_stack == "<")
                ):
                    appearances[char] += 1
                    break
    total = 0
    for k in appearances.keys():
        total += appearances[k] * weight[k]
    print(total)
                    
