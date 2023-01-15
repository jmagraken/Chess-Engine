import random
import sys

board = [['wr', 'wh', 'wb', 'wq', 'wk', 'wb', 'wh', 'wr'], ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'], ['br', 'bh', 'bb', 'bq', 'bk', 'bb', 'bh', 'br']]
wkingPos = [4, 0]
bkingPos = [4, 7]
val = {'bp': 1, 'wp': 1, 'bh': 3, 'wh': 3, 'bb': 3, 'wb': 3, 'br': 4, 'wr': 4, 'bq': 5, 'wq': 5, 'wk': 5, 'bk': 5, 'x': 0}

def printBoard(board):
    for i in range(7, -1, -1):
        print(f'{board[i][0].ljust(2)} {board[i][1].ljust(2)} {board[i][2].ljust(2)} {board[i][3].ljust(2)} {board[i][4].ljust(2)} {board[i][5].ljust(2)} {board[i][6].ljust(2)} {board[i][7].ljust(2)}')

def printBoardRotate(board):
    for i in range(0, 8):
        print(f'{board[i][7].ljust(2)} {board[i][6].ljust(2)} {board[i][5].ljust(2)} {board[i][4].ljust(2)} {board[i][3].ljust(2)} {board[i][2].ljust(2)} {board[i][1].ljust(2)} {board[i][0].ljust(2)}', i + 1)
    print("h  g  f  e  d  c  b  a")

def queen1(pos, fin):
     if pos[0] == fin[0] or pos[1] == fin[1]:
            if pos[0] == fin[0]:
                i = min(pos[0], fin[0])
                j = min(pos[1], fin[1]) + 1
            else:
                i = min(pos[0], fin[0]) + 1
                j = min(pos[1], fin[1])
            while i < max(pos[0], fin[0]) or j < max(pos[1], fin[1]):
                if board[j][i] != 'x':
                    return False
                if j == max(pos[1], fin[1]):
                    i += 1
                else:
                    j += 1
            return True
     else:
        return False


def incTowards(pos, fin):
    if pos < fin:
        return pos + 1
    else :
        return pos - 1



def queen2(pos, fin):
     if abs(fin[0] - pos[0]) == abs(fin[1] - pos[1]):
            i = incTowards(pos[0], fin[0])
            j = incTowards(pos[1], fin[1])
            while(i != fin[0] and j != fin[1]):
                if board[j][i] != 'x':
                    return False
                i = incTowards(i, fin[0])
                j = incTowards(j, fin[1])
            return True
     else:
            return False



def isValid(pos, fin, t):
    global board
    if pos == fin:
        return False
    if (board[fin[1]][fin[0]])[0] == (board[pos[1]][pos[0]])[0]:
        return False
    piece = board[pos[1]][pos[0]]
    final = board[fin[1]][fin[0]]
    if piece == 'x' or ((final == 'wk' or final == 'bk') and not t): 
        return False
    elif piece[1] == 'p':
        if pos[1] == 1 and piece[0] == 'w' or pos[1] == 6 and piece[0] == 'b':
            if final == 'x' and pos[0] == fin[0] and (piece[0] == 'w' and fin[1] - pos[1] <= 2 and fin[1] - pos[1] >= 0  or piece[0] == 'b' and fin[1] - pos[1] >= -2 and fin[1] - pos[1] <= 0):
                if abs(fin[1] - pos[1]) == 2:
                    return (piece[0] == 'w' and board[pos[1] + 1][pos[0]] == 'x' or piece[0] == 'b' and board[pos[1] - 1][pos[0]] == 'x')
                else:
                    return True
            elif final != 'x' and abs(pos[0] - fin[0]) == 1 and (piece[0] == 'w' and fin[1] - pos[1] == 1  or piece[0] == 'b' and fin[1] - pos[1] == -1):
                return True
            else:
                return False
        else:
            if final == 'x' and pos[0] == fin[0] and (piece[0] == 'w' and fin[1] - pos[1] == 1  or piece[0] == 'b' and fin[1] - pos[1] == -1):
                return True
            elif final != 'x' and abs(pos[0] - fin[0]) == 1 and (piece[0] == 'w' and fin[1] - pos[1] == 1  or piece[0] == 'b' and fin[1] - pos[1] == -1):
                return True
            else:
                return False
    elif piece[1] == 'b':
        if abs(fin[0] - pos[0]) == abs(fin[1] - pos[1]):
            i = incTowards(pos[0], fin[0])
            j = incTowards(pos[1], fin[1])
            while(i != fin[0] and j != fin[1]):
                if board[j][i] != 'x':
                    return False
                i = incTowards(i, fin[0])
                j = incTowards(j, fin[1])
            return True
        else:
            return False
    elif piece[1] == 'h':
        return abs(pos[0] - fin[0]) == 2 and abs(pos[1] - fin[1]) == 1 or abs(pos[0] - fin[0]) == 1 and abs(pos[1] - fin[1]) == 2
    elif piece[1] == 'r':
        if pos[0] == fin[0] or pos[1] == fin[1]:
            if pos[0] == fin[0]:
                i = min(pos[0], fin[0])
                j = min(pos[1], fin[1]) + 1
            else:
                i = min(pos[0], fin[0]) + 1
                j = min(pos[1], fin[1])
            while i < max(pos[0], fin[0]) or j < max(pos[1], fin[1]):
                if board[j][i] != 'x':
                    return False
                if j == max(pos[1], fin[1]):
                    i += 1
                else:
                    j += 1
            return True
        else:
            return False
    elif piece[1] == 'k':
        return abs(pos[0] - fin[0]) <= 1 and abs(pos[1] - fin[1]) <= 1
    elif piece[1] == 'q':    
        return queen1(pos, fin) or queen2(pos, fin)

def isInCheck(color):
    global wkingPos
    global bkingPos
    if color == 'w':
        pos = wkingPos
    else:
        pos = bkingPos
    for i in range(8):
        for j in range(8):
            if isValid([i, j], pos, True):
                return True
    return False


def pieceswap(first, second):
    global board
    global bkingPos

    if first[0] == 'a':
        first[0] = 1
    elif first[0] == 'b':
        first[0] = 2
    elif first[0] == 'c':
        first[0] = 3
    elif first[0] == 'd':
        first[0] = 4
    elif first[0] == 'e':
        first[0] = 5
    elif first[0] == 'f':
        first[0] = 6
    elif first[0] == 'g':
        first[0] = 7
    else:
        first[0] = 8

    if second[0] == 'a':
        second[0] = 1
    elif second[0] == 'b':
        second[0] = 2
    elif second[0] == 'c':
        second[0] = 3
    elif second[0] == 'd':
        second[0] = 4
    elif second[0] == 'e':
        second[0] = 5
    elif second[0] == 'f':
        second[0] = 6
    elif second[0] == 'g':
        second[0] = 7
    else:
        second[0] = 8
    if isValid([first[0] - 1, first[1] - 1], [second[0] - 1, second[1] - 1], False):
        newBKP = bkingPos.copy()
        newBoard = board.copy()
        board[second[1] - 1][second[0] - 1] = board[first[1] - 1][first[0] - 1]
        board[first[1] - 1][first[0] - 1] = 'x'
        if board[second[1] - 1][second[0] - 1] == 'bp' and second[1] == 1:
            board[second[1] - 1][second[0] - 1] = 'bq'
        if board[second[1] - 1][second[0] - 1] == 'bk':
            bkingPos = [second[1] - 1, second[0] - 1]
        if isInCheck('b'):
            bkingPos = newBKP
            board = newBoard
            return False
        return True
    else:
        return False

def copyBoard(board):
    newBoard = []
    for line in board:
        newBoard.append(line.copy())
    return newBoard


def randMoveBlack():
    global board
    global bkingPos
    while True:
        one = random.randint(0, 7)
        two = random.randint(0, 7)
        three = random.randint(0, 7)
        four = random.randint(0, 7)
        firstLoc = [one, two]
        secondLoc = [three, four]
        if board[two][one][0] == 'b' and isValid(firstLoc, secondLoc, False):
            newBoard = copyBoard(board)
            newBKP = bkingPos.copy()
            board[four][three] = board[two][one]
            board[two][one] = 'x'
            if board[four][three] == 'bp' and four == 0:
                board[four][three] = 'bq'
            if board[four][three] == 'bk':
                bkingPos = secondLoc
            if isInCheck('b'):
                board = newBoard
                bkingPos = newBKP
                continue
            break

def randMoveWhite():
    global board
    global wkingPos
    newBoard = copyBoard(board)
    newWKP = wkingPos.copy()
    bestBoard = newBoard
    bestkingPos = newWKP
    topScore = -1
    for i in range(8):
        for j in range(8):
            if board[j][i][0] != 'w':
                continue
            for k in range(10):
                board = copyBoard(newBoard)
                wkingPos = newWKP.copy()
                one = i
                two = j
                three = random.randint(0, 7)
                four = random.randint(0, 7)
                firstLoc = [one, two]
                secondLoc = [three, four]
                if isValid(firstLoc, secondLoc, False):
                    points = val[board[four][three]]
                    board[four][three] = board[two][one]
                    board[two][one] = 'x'
                    if board[four][three] == 'wp' and four == 7:
                        board[four][three] = 'wq'
                    if board[four][three] == 'wk':
                        wkingPos = secondLoc
                    if isInCheck('w'):
                        continue
                    if points >= topScore:
                        topScore = points
                        bestBoard = board
                        bestkingPos = wkingPos
    board = bestBoard
    wkingPos = bestkingPos
    if topScore == -1:
        randMoveWhite()
    
    

def main(gamemode):
    if gamemode == "botvbot":
        while True:
            randMoveWhite()
            printBoard(board)
            print('/' * 50)
            randMoveBlack()
            printBoard(board)
            print('/' * 50)

    elif gamemode == "botvhuman":
        while True:
            randMoveWhite()
            printBoardRotate(board)
            print('/' * 50)
            move = input()
            while not pieceswap([move[0], int(move[1])], [move[3], int(move[4])]):
                print("INVALID MOVE")
                move = input()
            printBoardRotate(board)
            print('/' * 50)

   
if len(sys.argv) > 1:
    main(sys.argv[1])


