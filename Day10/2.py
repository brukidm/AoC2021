with open(r"input.txt") as f:
    values = f.read().split('\n')

    weight = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    scores = []
    for value in values:
        stack = []
        corrupted = False
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
                    corrupted = True
                    break
        if len(stack) > 0 and not corrupted:
            total_score = 0
            for char in reversed(stack):
                if char == "(":
                    total_score = total_score * 5 + 1
                elif char == "[":
                    total_score = total_score * 5 + 2
                elif char == "{":
                    total_score = total_score * 5 + 3
                elif char == "<":
                    total_score = total_score * 5 + 4
            scores.append(total_score)
    scores = sorted(scores, key=int)
    print(scores[int(len(scores)/2)])

