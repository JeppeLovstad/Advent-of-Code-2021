import sys

output = 0
lines = []
path = sys.path[0]+"\input.txt"
with open(path, 'r', encoding='utf-8') as f:
    for l in f:
        l = l.rstrip()
        for fish in l.split(","):
            lines.append(int(fish))


fish_dict = {}

for fish in lines:
    if fish in fish_dict:
        fish_dict[fish] += 1
    else:
        fish_dict[fish] = 1

for i in range(0, 9):
    if i not in fish_dict:
        fish_dict[i] = 0

print(sorted(fish_dict.items(), key=lambda x: x[0]))

DAYS = 256
for day in range(DAYS):
    for fish, amount in sorted(fish_dict.items(), key=lambda x: x[0], reverse=True):
        #print(fish, amount)
        if fish > 0:
            fish_dict[fish] -= amount
            fish_dict[fish-1] += amount
        if fish == 0:
            fish_dict[fish] -= amount
            fish_dict[8] += amount
            fish_dict[6] += amount
        #print(fish, amount, "->", fish_dict[fish])

print(sorted(fish_dict.items(), key=lambda x: x[0]))
print(sum(fish_dict.values()))
