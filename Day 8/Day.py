import sys

output = 0
lines = []
path = sys.path[0]+"\input.txt"
with open(path, 'r', encoding='utf-8') as f:
    for l in f:

        lines.append(list(map(str.split, l.rstrip().split(" | "))))

dict = {frozenset([1,2,3,5,6,7]):0,  frozenset([3,6]):1, frozenset([1,3,4,5,7]):2, frozenset([1,3,4,6,7]):3, frozenset([2,3,4,6]):4, frozenset([1,2,4,6,7]):5, frozenset([1,2,4,5,6,7]):6, frozenset([1,3,6]):7, frozenset([1,2,3,4,5,6,7]):8, frozenset([1,2,3,4,6,7]):9}
result1 = 0
result2 = 0
for input, output in lines:
    input_dict = {}
    for line in output:
        if len(line) == 2 or len(line) == 4 or len(line) == 3 or len(line) == 7:
            result1 += 1

    for line in input:
        input_dict.setdefault(len(line), []).append(list(line))

    #print(input_dict)
    number_to_line_dict = {k: "" for k in range(1, 8)}
    number_to_letters_dict = {k: [] for k in range(1, 10)}

    # line 1
    for letters in input_dict[3][0]:
        if letters not in input_dict[2][0]:
            number_to_line_dict[1] = letters

    number_to_letters_dict[1] = input_dict[2]

    # line 3
    for lines in input_dict[6]:
        for letters_one in input_dict[2][0]:
            if letters_one not in lines:
                number_to_line_dict[3] = letters_one
                number_to_letters_dict[6] = lines
                #print(lines, letters_one)

    # line 6
    for letter in input_dict[3][0]:
        if letter not in number_to_line_dict.values():
            number_to_line_dict[6] = letter

    # line 4 and 7 - get all lengths of 5, subtract lines in 7, find the remaining intersection between the 3
    # this is line 4 and 7, use 4 to differentiate between them
    five1, five2, five3 = input_dict[5]
    for letters in input_dict[3][0]:
        if letters in five1:
            five1.remove(letters)
        if letters in five2:
            five2.remove(letters)
        if letters in five3:
            five3.remove(letters)
    if len(five1) == 2:
        four_and_seven = five1
    if len(five2) == 2:
        four_and_seven = five2
    if len(five3) == 2:
        four_and_seven = five3

    for letters in input_dict[4][0]:
        if letters in four_and_seven:
            number_to_line_dict[4] = letters

    for i in four_and_seven:
        if i != number_to_line_dict[4]:
            number_to_line_dict[7] = i

    # line 2 from the remaining line in 4
    for letters in input_dict[4][0]:
        if letters not in number_to_line_dict.values():
            number_to_line_dict[2] = letters

    # line 5 last one from 8
    for letters in input_dict[7][0]:
        if letters not in number_to_line_dict.values():
            number_to_line_dict[5] = letters

    inv_map = {v: k for k, v in number_to_line_dict.items()}

    activated_lines = []
    for lines in output:
        a = []
        for letters in list(lines):
            a.append(inv_map[letters])
        activated_lines.append(frozenset(a))

    output_value = ""
    for l in activated_lines:
        output_value += str(dict[l])
    print(output_value)
    result2 += int(output_value)
    
    #print(dict)
# print(number_to_line_dict)
print(number_to_letters_dict)


print(result1)
print(result2)
