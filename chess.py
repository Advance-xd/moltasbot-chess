# define the initial state of the board
board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]

# define the players
WHITE = 'w'
BLACK = 'b'

# define the direction vectors for each piece
DIRECTIONS = {
    'N': (-1, -2),
    'K': (-1, -1),
    'B': (-1, -1),
    'R': (-1, 0),
    'Q': (-1, 0),
    'P': (-1, 0),
}

def generate_moves(board, player):
    """Generate all possible moves for the given player."""
    moves = []
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece == ' ' or piece.lower() != player:
                continue
            for dr, dc in DIRECTIONS[piece.upper()]:
                r2 = r + dr
                c2 = c + dc
                # check if the move is on the board
                if r2 < 0 or r2 > 7 or c2 < 0 or c2 > 7:
                    continue
                # check if the destination is empty or an enemy piece
                if board[r2][c2] == ' ' or board[r2][c2].lower() != player:
                    moves.append((r, c, r2, c2))
    return moves

def evaluate_board(board, player):
    """Evaluate the board position for the given player."""
    score = 0
    # evaluate material advantage
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece == ' ':
                continue
            if piece.lower() == player:
                score += 1
            else:
                score -= 1
    return score

def search(board, player, depth):
    """Search for the best move using minimax with alpha-beta pruning."""
    # generate all possible moves
    moves = generate_moves(board, player)
    if depth == 0 or not moves:
        return None, evaluate_board(board, player)
    # initialize the best move and score
    best_move = None
    if player == WHITE:
        best_score = float('inf')
        for move in moves:
            # simulate the move
            board[move[2]][move[3]] = board[move[0]][move[1]]

import cv2
from PIL import ImageGrab
import time
import pyautogui
import random

# read the image






# define the templates for each piece
TEMPLATES = {
    'K': cv2.imread('pieces/wk.png'),    # white king
    'Q': cv2.imread('pieces/wq.png'),   # white queen
    'R': cv2.imread('pieces/wr.png'),    # white rook
    'B': cv2.imread('pieces/wb.png'),  # white bishop
    'N': cv2.imread('pieces/wn.png'),  # white knight
    'P': cv2.imread('pieces/wp.png'),    # white pawn
    'k': cv2.imread('pieces/bk.png'),    # black king
    'q': cv2.imread('pieces/bq.png'),   # black queen
    'r': cv2.imread('pieces/br.png'),    # black rook
    'b': cv2.imread('pieces/bb.png'),  # black bishop
    'n': cv2.imread('pieces/bn.png'),  # black knight
    'p': cv2.imread('pieces/bp.png'),    # black pawn
}

# initialize the board

mycolor = None


def randomnumber():
    return random.random() * 0.1

def reverselistandrow(board):
    board = list(reversed(board))
    reversed_lists = []
    for lst in board:
        reversed_lst = list(reversed(lst))
        reversed_lists.append(reversed_lst)
    return reversed_lists

def waitforenemy():
    global mycolor
    enemyturn = True
    while enemyturn:
        if mycolor == "white":
            pixles = ImageGrab.grab(bbox=(775, 163, 776, 164))
            for y in range(0, 2, 2):
                    for x in range(0, 2, 2):
                        color = pixles.getpixel((x, y))
            if color[0] == 38 and color[1] == 33 and color[2] == 27:
                print("enemy turn")
            else:
                print("my turn")
                enemyturn = False
        else:
            pixles = ImageGrab.grab(bbox=(775, 163, 776, 164))
            for y in range(0, 2, 2):
                    for x in range(0, 2, 2):
                        color = pixles.getpixel((x, y))
            if color[0] == 255:
                print("enemy turn")
            else:
                print("my turn")
                enemyturn = False
        print("wating")
        time.sleep(1)
    copyenemymovetobot()

def copymovefrombot():
    global mycolor

    pixles = ImageGrab.grab(bbox=(1320, 335, 1532, 345))
    for y in range(0, 2, 2):
            for x in range(0, 2, 2):
                color = pixles.getpixel((x, y))
    if color[1] == 101 and color[2] == 101:
        print("bot won")
        pyautogui.moveTo(1585, 343)
        pyautogui.click()
        time.sleep(.5)

    right = getrightboard()
    left = getleftboard()
    left = reverselistandrow(left)
    pyautogui.moveTo(96 + randomnumber(), 191 + randomnumber())
    pyautogui.click()
    for a in range(8):
        if right[a] != left[a]:
            for b in range(8):
                if right[a][b] != left[a][b] and not ((right[a][b].isupper() and mycolor == "white") or (right[a][b].islower() and mycolor == "black")):
                    
                    print("found empty", a, b)
                    pyautogui.moveTo(96 +  8 * 97 - (b * 97) - 97/2 - randomnumber(), 191 + 8 * 97 - (a * 97) - 97/2 - randomnumber())
    time.sleep(randomnumber())
    pyautogui.click()
    time.sleep(randomnumber())
    times = 0
    for a in range(8):
        if right[a] != left[a]:
            for b in range(8):
                if right[a][b] != left[a][b] and ((right[a][b].isupper() and mycolor == "white") or (right[a][b].islower() and mycolor == "black")):
                    times += 1
                    print("found should move to", a, b)
                    if times > 1:
                        input("err")
                    else:
                        pyautogui.moveTo(96 +  8 * 97 - (b * 97) - 97/2 + randomnumber(), 191 + 8 * 97 - (a * 97) - 97/2 + randomnumber())
    time.sleep(randomnumber())
    pyautogui.click()
    pyautogui.moveTo(96 - randomnumber(), 191 - randomnumber())
    time.sleep(3 + randomnumber())
    waitforenemy()

def copyenemymovetobot():
    global mycolor
    right = getrightboard()
    left = getleftboard()
    right = reverselistandrow(right)
    pyautogui.moveTo(1045 +  randomnumber(), 186 + randomnumber())
    pyautogui.click()
    times = 0
    for a in range(8):
        if right[a] != left[a]:
            for b in range(8):
                if right[a][b] != left[a][b] and ((right[a][b].isupper() and mycolor == "black") or (right[a][b].islower() and mycolor == "white")):
                    times += 1
                    print("found should move from", a, b)
                    if times > 1:
                        input("err")
                    else:
                        pyautogui.moveTo(1045 +  8 * 98 - (b * 98) - 98/2 - randomnumber(), 186 + 8 * 98 - (a * 98) - 98/2 - randomnumber())
    time.sleep(randomnumber())
    pyautogui.click()
    time.sleep(randomnumber())
    for a in range(8):
        if right[a] != left[a]:
            for b in range(8):
                if right[a][b] != left[a][b] and not ((right[a][b].isupper() and mycolor == "black") or (right[a][b].islower() and mycolor == "white")):
                    print("found empty", a, b)
                    pyautogui.moveTo(1045 +  8 * 98 - (b * 98) - 98/2 - randomnumber(), 186 + 8 * 98 - (a * 98) - 98/2 - randomnumber())
    time.sleep(randomnumber())
    pyautogui.click()
    pyautogui.moveTo(1045 -  randomnumber(), 186 - randomnumber())
    time.sleep(5)
    copymovefrombot()

def checkcolor():
    global mycolor
    pixles = ImageGrab.grab(bbox=(811, 916, 812, 917))
    for y in range(0, 2, 2):
            for x in range(0, 2, 2):
                color = pixles.getpixel((x, y))
    if color[0] == 255:
        mycolor = 'white'
    else:
        mycolor = 'black'
    right = getrightboard()
    left = getleftboard()
    right = reverselistandrow(right)
    for y in range(8):
        print(left[y], " ", right[y])
    print()
    right = getrightboard()
    left = getleftboard()
    left = reverselistandrow(left)
    for y in range(8):
        print(left[y], " ", right[y])
    
    print("You are " + mycolor + " start a bot game with the other color")
    input("wait")
    #copyenemymovetobot()
    #copymovefrombot()
    if mycolor == "black":
        waitforenemy()
    else:
        copymovefrombot()

def getrightboard():
    # RIGHT screen bot game
    img = ImageGrab.grab(bbox=(1045, 186, 1045 + 97*8, 186 + 97 * 8))

    img.save('res.png', 'PNG')

    image = cv2.imread('res.png')

    #cv2.imshow("res.png", image)

    # define the dimensions of each square on the board
    SQUARE_SIZE = (image.shape[0] // 8, image.shape[1] // 8)
    #print(SQUARE_SIZE)
    board = []

    # iterate over each square on the board
    for r in range(8):
        row = []
        for c in range(8):
            # extract the square from the image
            square = image[r*SQUARE_SIZE[0]:(r+1)*SQUARE_SIZE[0], c*SQUARE_SIZE[1]:(c+1)*SQUARE_SIZE[1]]
            # initialize the best matching piece and score
            best_match = ' '
            best_score = 0
            score = 0
            #score2 = 0
            # iterate over each piece
            for piece, template in TEMPLATES.items():
                # resize the template to match the square
                template = cv2.resize(template, SQUARE_SIZE)
                # compute the normalized cross-correlation score
                score = cv2.matchTemplate(square, template, cv2.TM_CCOEFF_NORMED)[0][0]
                #score2 = cv2.matchTemplate(square, template, cv2.TM_CCORR_NORMED)[0][0]
                #print(str(r) + " " + str(c) + " " + str(score))
                # update the best matching piece
                if score > best_score:
                    best_match = piece
                    best_score = score #+ score2/12
            if (best_score < 0.55):
                best_match = ' '
            row.append(best_match)
        board.append(row)

    # print the board
    #print("-------------------")
    #for row in board:
    #    print(' '.join(row))
    return board

def getleftboard():
    # LEFT screen online game
    img2 = ImageGrab.grab(bbox=(96, 191, 96 + 96*8, 191 + 96 * 8))

    img2.save('res2.png', 'PNG')

    image2 = cv2.imread('res2.png')

    #cv2.imshow("res.png", image)

    # define the dimensions of each square on the board
    SQUARE_SIZE = (image2.shape[0] // 8, image2.shape[1] // 8)
    #print(SQUARE_SIZE)
    board = []

    # iterate over each square on the board
    for r in range(8):
        row = []
        for c in range(8):
            # extract the square from the image
            square = image2[r*SQUARE_SIZE[0]:(r+1)*SQUARE_SIZE[0], c*SQUARE_SIZE[1]:(c+1)*SQUARE_SIZE[1]]
            # initialize the best matching piece and score
            best_match = ' '
            best_score = 0
            score = 0
            #score2 = 0
            # iterate over each piece
            for piece, template in TEMPLATES.items():
                # resize the template to match the square
                template = cv2.resize(template, SQUARE_SIZE)
                # compute the normalized cross-correlation score
                score = cv2.matchTemplate(square, template, cv2.TM_CCOEFF_NORMED)[0][0]
                #score2 = cv2.matchTemplate(square, template, cv2.TM_CCORR_NORMED)[0][0]
                #print(str(r) + " " + str(c) + " " + str(score))
                # update the best matching piece
                if score > best_score:
                    best_match = piece
                    best_score = score #+ score2/12
            if (best_score < 0.55):
                best_match = ' '
            row.append(best_match)
        board.append(row)

    # print the board
    #print("-------------------")
    #for row in board:
    #    print(' '.join(row))
    return board

    #cv2.imshow("im", image2[7*SQUARE_SIZE[0]:(8)*SQUARE_SIZE[0], 7*SQUARE_SIZE[1]:(8)*SQUARE_SIZE[1]])
    #cv2.waitKey(0)


checkcolor()


#firstmoves()
