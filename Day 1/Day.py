output1 = 0
output2 = 0

with open("Day1\input.txt", 'r', encoding='utf-8') as f:

    LastLine = 99999
    lines = []
    for l in f:
        line = int(l)
        if line > LastLine:
            output1 += 1

        LastLine = line

        lines.append(line)

LastLineSum = 9999999
for i in range(0, len(lines)):

    CurrentSum = sum(lines[i:i+3])
    # print(CurrentSum)
    if CurrentSum > LastLineSum:
        output2 += 1
    LastLineSum = CurrentSum

print(output1)
print(output2)
