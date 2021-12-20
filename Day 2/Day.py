import sys

output = 0
lines = []
path = sys.path[0]+"\input.txt"
with open(path, 'r', encoding='utf-8') as f:
    for l in f:
        lines.append(l)

hor = depth = aim = 0

for l in lines:
    desc, num = l.split()
    num = int(num)

    if desc == 'forward':
        hor += num
        depth += aim*num
    if desc == 'down':
        #depth += num
        aim += num
    if desc == 'up':
        #depth -= num
        aim -= num
    #print(hor, depth, aim, hor*depth)
#print(hor, depth, hor*depth)
print(hor, depth, aim, hor*depth)
