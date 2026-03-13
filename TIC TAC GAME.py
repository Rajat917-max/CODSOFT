# Tic-Tac-Toe AI using Minimax

import math

# Create board
board = [" " for _ in range(9)]

# Display board
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Check winner
def check_winner(b, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if b[pos[0]] == b[pos[1]] == b[pos[2]] == player:
            return True
    return False

# Check draw
def is_draw(b):
    return " " not in b

# Minimax algorithm
def minimax(b, depth, is_maximizing):

    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth+1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score

    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth+1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

# Human move
def human_move():
    while True:
        move = int(input("Enter position (1-9): ")) - 1
        if board[move] == " ":
            board[move] = "X"
            break
        else:
            print("Position already taken!")

# Game loop
while True:
    print_board()

    human_move()
    if check_winner(board, "X"):
        print_board()
        print("You Win!")
        break

    if is_draw(board):
        print_board()
        print("Match Draw!")
        break

    ai_move()
    if check_winner(board, "O"):
        print_board()
        print("AI Wins!")
        break

    if is_draw(board):
        print_board()
        print("Match Draw!")
        break