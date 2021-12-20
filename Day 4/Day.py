import sys


class BingoBoard:
    #boardNumber: list[int] = [-1]
    #timeToWin: int = 100
    #winningNumber: int = 101
    #score: int = 0
    #board: list[int] = []
    #unmarkedNumbers: list[int] = []
    #validLines: list[int] = []
    #winningLine: list[int] = []
    #numbersAtwin: list[int] = []

    def calculateScore(self) -> int:
        s = 0
        for row in self.board:
            for (num, _) in row:
                if num not in self.numbersAtwin:
                    s += num
                    self.unmarkedNumbers.append(num)
        return s

    def addHorizontalLines(self) -> None:
        self.validLines.extend(map(list, zip(*self.board[::-1])))

    def findTimeToWin(self) -> None:
        for row in self.validLines:
            rowWinsAt = max(row, key=lambda x: x[1])
            #print(row, rowWinsAt)
            if rowWinsAt[1] <= self.timeToWin:
                self.timeToWin = rowWinsAt[1]
                self.winningNumber = rowWinsAt[0]
                self.winningLine = row

    def __init__(self, boardNumber: int, board: list[int], numbers: list[int]) -> None:
        self.timeToWin: int = 100
        self.winningNumber: int = 101
        #self.score: int = 0
        #self.board: list[int] = []
        self.unmarkedNumbers: list[int] = []
        self.validLines: list[int] = []
        self.winningLine: list[int] = []
        #self.numbersAtwin: list[int] = []
        self.boardNumber = boardNumber
        self.board = board
        self.validLines.extend(board)
        self.addHorizontalLines()
        self.findTimeToWin()
        # print(numbers[:self.timeToWin+1])
        self.numbersAtwin = numbers[:self.timeToWin+1]
        self.score = self.calculateScore()


# numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10,
#          16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

numbers = [28, 82, 77, 88, 95, 55, 62, 21, 99, 14, 30, 9, 97, 92, 94, 3, 60, 22, 18, 86, 78, 71, 61, 43, 79, 33, 65, 81, 26, 49, 47, 51, 0, 89, 57, 75, 42, 35, 80, 1, 46, 83, 39, 53, 40, 36, 54, 70, 76,
           38, 50, 23, 67, 2, 20, 87, 37, 66, 84, 24, 98, 4, 7, 12, 44, 10, 29, 5, 48, 59, 32, 41, 90, 17, 56, 85, 96, 93, 27, 74, 45, 25, 15, 6, 69, 16, 19, 8, 31, 13, 64, 63, 34, 73, 58, 91, 11, 68, 72, 52]

#(number, position)
numbers_Enumerated = {value: enum for (enum, value) in enumerate(numbers)}
# print(numbers_Enumerated)
lines = []
path = sys.path[0]+"\input.txt"
with open(path, 'r', encoding='utf-8') as f:
    for l in f:
        lines.append(l.rstrip())

boards = [BingoBoard(BoardNumber, [list(map(lambda line: (int(line), numbers_Enumerated[int(line)]), y.split())) for y in lines[x:x+5]], numbers)
          for (BoardNumber, x) in enumerate(range(0, len(lines), 5))]

fistWinningBoard = min(boards, key=lambda x: x.timeToWin)
print(fistWinningBoard.score*fistWinningBoard.winningNumber)

lastWinningBoard = max(boards, key=lambda x: x.timeToWin)
print(lastWinningBoard.score*lastWinningBoard.winningNumber)
# for b in boards:
#     print(b.boardNumber)
#     print(b.score*b.winningNumber)
#     print(b.score)
#     print(b.winningNumber)
#     print(b.timeToWin)
#     print(b.numbersAtwin)
#     print(b.winningLine)
#     print(b.board)
#     print(b.unmarkedNumbers)


# b0 = BingoBoard(0, boards[0], list(numbers.keys()))

# print(b0.validLines)
# print(b0.timeToWin)
# print(b0.winningNumber)
# print(b0.score)

# for d in boards:
#     boards[d].extend(map(list, zip(*boards[d][::-1])))

# for row in boards[0]:
#     print(max(row, key=lambda x: x[1]))

# board = -1
# minWin = 100
# for i in range(0, 100):
#     for row in boards[i]:
#         shortestWin = max(row, key=lambda x: x[1])
#         if shortestWin[1] < minWin:
#             minWin = shortestWin[1]
#             board = i

# print(board, minWin, numbers[minWin])
# print(numbers)
# validLines = {}
# for k, v in boards.items():
#     for x in v:
#         #print(k, x)
#         validLines.setdefault(tuple(x), k)

# print(numbers)
#print(*combinations(numbers[0:6], 5))
