import sys

output = 0
lines = []
diagonalLines = []
path = sys.path[0]+"\input.txt"
with open(path, 'r', encoding='utf-8') as f:
    for l in f:
        l = l.rstrip()
        a = list(map(lambda x: x.split(","), l.split(" -> ")))
        a1 = list(zip(a[0], a[1]))
        # print(a)
        # a[0].split(",")
        #a1 = lambda x: list(map(int, a.split(",")))
        if a1[0][0] == a1[0][1] or a1[1][0] == a1[1][1]:
            lines.append(a1)
        else:
            diagonalLines.append(a1)

#(x1, x2)(y1,y2)
# print(lines)
dict = {}

for p in lines:
    #addx = 1 if int(p[0][0]) == int(p[0][1]) else 0
    #addy = 1 if int(p[1][0]) == int(p[1][1]) else 0
    #negx = 1 if int(p[0][0]) < int(p[0][1]) else -1
    #negy = 1 if int(p[1][0]) < int(p[1][1]) else -1
    #print(int(p[0][0]), int(p[0][1]), "->", int(p[1][0]), int(p[1][1]))

    x_is_static = False

    if int(p[0][0]) == int(p[0][1]):
        x_is_static = True
        neg = 1 if int(p[1][0]) < int(p[1][1]) else -1
        TestRange = range(int(p[1][0]), int(p[1][1])+neg, neg)
        static_val = int(p[0][0])
    else:
        neg = 1 if int(p[0][0]) < int(p[0][1]) else -1
        TestRange = range(int(p[0][0]), int(p[0][1])+neg, neg)
        static_val = int(p[1][0])

    # print(TestRange)

    for i in TestRange:
        # for j in range(int(p[1][0]), int(p[1][1])+addy, negy):
        if x_is_static:
            key = (i, static_val)
        else:
            key = (static_val, i)
        # print(key)
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1

# print(diagonalLines)

for p in diagonalLines:

    negx = 1 if int(p[1][0]) < int(p[1][1]) else -1
    TestRangex = range(int(p[1][0]), int(p[1][1])+negx, negx)
    negy = 1 if int(p[0][0]) < int(p[0][1]) else -1
    TestRangey = range(int(p[0][0]), int(p[0][1])+negy, negy)

    #print(p, TestRangex, TestRangey)
    zipped = list(zip(list(TestRangex), list(TestRangey)))
    for key in zipped:
        # print(key)
        # for j in TestRangey:
        #     key = (i, j)
        #     print(key)
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1

# for i in range(0, 10):
#     for j in range(0, 10):
#         key = (i, j)
#         if key not in dict:
#             print(".", end=" ")
#         else:
#             print(dict[key], end=" ")
#     print("\n")

# print(dict)
print(len(list(filter(lambda v: v > 1, dict.values()))))
# print(lines)
