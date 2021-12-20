import sys
import statistics

output = 0
lines = []
path = sys.path[0]+"\input.txt"
with open(path, 'r', encoding='utf-8') as f:
    for l in f:
        l = l.rstrip()
        for crabs in l.split(","):
            lines.append(int(crabs))

median_crab = statistics.median(lines)
avg_crab = sum(lines)//len(lines)

print(median_crab)
print(avg_crab)

median_total_cost = 0
avg_total_cost = 0
for crab in lines:
    median_total_cost += abs(crab-median_crab)
    avg_total_cost += abs(crab-avg_crab)*(abs(crab-avg_crab)+1)/2


print(median_total_cost)
print(avg_total_cost)

# 85015849
# 85015721
