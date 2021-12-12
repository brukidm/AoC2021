import copy

def has_duplicates(l):
    if len(l) == len(set(l)):
        return False
    return True

def search_for_options(path, visited_small_caves, total_path):
    total = 0
    if path == "end":
        total_path += "end"
        return 1

    total_path += path + ","

    if path.islower():
        visited_small_caves = copy.deepcopy(visited_small_caves)
        visited_small_caves.append(path)

    for next in conns[path]:
        if next.islower():
            if next not in visited_small_caves:
                total += search_for_options(next, visited_small_caves, total_path)

            elif (not has_duplicates(visited_small_caves) and next != "start") or next == "end":
                total += search_for_options(next, visited_small_caves, total_path)
        else:
            total += search_for_options(next, visited_small_caves, total_path)
    
    return total

            
with open(r"input.txt") as f:
    values = f.read().split('\n')

    conns = {}

    for value in values:
        a, b = value.split("-")
        if a not in conns.keys():
            conns[a] = [b]
        else:
            conns[a].append(b)

        if b not in conns.keys():
            conns[b] = [a]
        else:
            conns[b].append(a)

    print(search_for_options("start",[], ""))