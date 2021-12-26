import sys

output = 0
lines = []
path = sys.path[0]+"\\input.txt"
with open(path, 'r', encoding='utf-8') as f:
    for l in f:
        l = l.rstrip()
        
        lines.append(l.split("-"))
        
        

connection_dict = {}
small_caves = set()
large_caves = set()
for cave in lines:
    connection_dict.setdefault(cave[0], []).append(cave[1])
    connection_dict.setdefault(cave[1], []).append(cave[0])
    
    if cave[1].isupper():
        large_caves.add(cave[1])
    else:
        small_caves.add(cave[1])
    
    if cave[0].isupper():
        large_caves.add(cave[0])
    else:
        small_caves.add(cave[0])

print(connection_dict)
print(small_caves)

def recurse(curr_path, curr_cave, paths, visited_small_caves, small_cave_limit):
    if curr_cave == "end":
        paths.append(curr_path)
        return paths
    
    #set bit if any small cave is at visit limit
    visited_same_twice = True if small_cave_limit in visited_small_caves.values() else False
    
    for cave in connection_dict[curr_cave]:
        if cave in small_caves and visited_same_twice and cave in curr_path:
            continue
        if cave == 'start':
            continue
        
        new_path = curr_path.copy()
        new_path.append(cave)
        new_visited_small_caves = visited_small_caves.copy()
        if cave in small_caves:
            if cave in visited_small_caves:
                new_visited_small_caves[cave] += 1
            else:
                new_visited_small_caves[cave] = 1
                
        paths = recurse(new_path, cave, paths, new_visited_small_caves, small_cave_limit)
    
    return paths
    
paths = recurse(["start"], "start", [], {}, 1)
paths2 = recurse(["start"], "start", [], {}, 2)

print(len(paths))
print(len(paths2))
