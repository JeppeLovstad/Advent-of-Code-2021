import sys

output = 0
lines = []
path = sys.path[0]+"\input.txt"
with open(path, 'r', encoding='utf-8') as f:
    for l in f:
        l = l.rstrip()
        lines.append(l)

print(lines)

open_symbols = ("<","(","[","{")
close_symbols = (">",")","]","}")
symbol_points_part1 = {">":25137,")":3,"]":57,"}":1197}
symbol_points_part2 = {"<":4,"(":1,"[":2,"{":3}

lines_non_corrupt = []#lines.copy()

result = 0
for line in lines:
    is_corrupt = False
    symbol_queue = []
    for curr_symbol in line:
        if curr_symbol in open_symbols:
            symbol_queue.append(curr_symbol)
        elif curr_symbol in close_symbols:
            last_open_symbol = symbol_queue.pop()
            match (last_open_symbol,curr_symbol):
                case ("<",">") | ("(",")") | ("[","]")| ("{","}"):
                    pass#lines_non_corrupt.append(line)
                case _:
                    result += symbol_points_part1[curr_symbol]
                    is_corrupt = True
                    #lines_non_corrupt.remove(line)
                    continue
    if not is_corrupt:
        lines_non_corrupt.append((line, symbol_queue))
    
results2 = []
for line in lines_non_corrupt:
    res = 0
    for symbol in line[1][::-1]:
        res = (res*5) +  symbol_points_part2[symbol]
    results2.append(res)
    
print(result)
print(sorted(results2)[len(results2)//2])
#print(results2)