import sys

output = 0
lines = []
path = sys.path[0]+"\input.txt"
with open(path, 'r', encoding='utf-8') as f:
    for lineNum in f:
        lines.append(lineNum.rstrip())

bitLen = len(lines[0])
counts = [0]*bitLen
countsDict = {}
for lineNum in lines:
    # listed = list(lineNum[:-1])
    for i in range(bitLen):
        counts[i] += int(lineNum[i])


# print(countsDict)
# countsDict[2].remove(['1', '0', '1', '0', '1'])
# print(countsDict)

most = least = ''
total = len(lines)
for i in range(bitLen):
    if counts[i] > total//2:
        most += "1"
        least += "0"
    else:
        most += "0"
        least += "1"

print(most, least, counts)
print(int(most, 2)*int(least, 2))

linesMost = lines
linesLeast = lines.copy()
leastCounts = counts.copy()
i = 0
while len(linesMost) > 1:
    mostTotal = len(linesMost)
    ones = counts[i]
    zeroes = mostTotal-counts[i]
    #deleteKeyMost = "0" if mostTotal-counts[i] >= 0 else "1"
    deleteKeyMost = "0" if ones >= zeroes else "1"
    #print(counts, mostTotal)
    lineNum = 0
    while counts[i] != len(linesMost):
        #print(len(linesMost), len(linesMost[0]), i)
        # print(linesMost, f"linenum:{lineNum}",
        #       f"i:{i}", deleteKeyMost, len(linesMost))
        if linesMost[lineNum][i] == deleteKeyMost:
            for letterNum in range(bitLen):
                counts[letterNum] -= int(linesMost[lineNum][letterNum])
            linesMost.pop(lineNum)
            lineNum -= 1
        lineNum += 1
        if lineNum == len(linesMost):
            break
    i += 1

i = 0
while len(linesLeast) > 1:
    LeastTotal = len(linesLeast)
    ones = leastCounts[i]
    zeroes = LeastTotal-ones
    deleteKeyLeast = "1" if ones >= zeroes else "0"
    #print(ones, zeroes, deleteKeyLeast, leastCounts)
    lineNum = 0
    while LeastTotal-leastCounts[i] != len(linesLeast):
        if linesLeast[lineNum][i] == deleteKeyLeast:
            for letterNum in range(bitLen):
                leastCounts[letterNum] -= int(linesLeast[lineNum][letterNum])
            linesLeast.pop(lineNum)
            lineNum -= 1
        lineNum += 1
        if lineNum == len(linesLeast):
            break
    #print(lineNum, len(linesLeast))
    i += 1


print(linesMost, linesLeast, counts, leastCounts)
print(int(linesMost[0], 2)*int(linesLeast[0], 2))
