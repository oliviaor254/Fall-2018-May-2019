from numpy import *
print("How to tell where you are on the board:\n  Selecting a row: (1-8 from top to bottom)\nSelecting a column(a-h left to right)")
chess_board = [['R','N','B','Q','K','B','N','R'],['P','P','P','P','P','P','P','P'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['p','p','p','p','p','p','p','p'],['r','n','b','q','k','b','n','r']]
print("Select column 'a', and row '9' to cancel.")
c= 0
cr = 0
cn = ''
patchwork = True            #Will determine when to exit program
columns = ['a','b','c','d','e','f','g','h']
rows = [1,2,3,4,5,6,7,8]
while patchwork == True:
    while c < len(chess_board[0]):      #IT PRINTS CORRECTLY!!
        c = 0
        for a in range(len(chess_board)):
            for b in range(len(chess_board[a])):
                print(chess_board[a][b], end=' ')
                c += 1
            if chess_board[a][b] == chess_board[a][-1]:
                print()

    #HOW TO KNOW WHAT SPOT IS BEING CALLED
    onepcC = input("What column do you want to select a piece from? ")
    onepcR = int(input("In that column, what spot is that piece in?"))
    if onepcC in columns:
        cn = columns.index(onepcC)
    else:
        patchwork = False
        print("Error, that is not in the board's bounds.")
        break
    #break ; USE a while loop to keep going. Select [0][9] to exit?
    if onepcR in rows:
        cr = rows.index(onepcR)
    else:
        patchwork = False
        print("Error, that is not in the board's bounds.")
        break
    actual = chess_board[cr][cn]
    if actual == '.':
        patchwork = False
        print("Error, that move is not allowed.")
        break
    print("You selected", actual)
    next_spotc = input("What column do you want to move it to? ")
    next_spotr = int(input("What row do you want to move it to? "))
    if next_spotc in columns:
        ac2 = columns.index(next_spotc)
    else:
        patchwork = False
        print("Error, that is not in the board's bounds.")
        break
    if next_spotr in rows:
        ar2 = rows.index(next_spotr)
    else:
        patchwork = False
        print("Error, that is not in the board's bounds.")
        break
    moveto = chess_board[ar2][ac2]
    chess_board[ar2][ac2] = actual
    chess_board[cr][cn] = '.'
    print("You have selected", moveto)
    c = 0
    while c < len(chess_board[0]):
        c = 0
        for a in range(len(chess_board)):
            for b in range(len(chess_board[a])):
                print(chess_board[a][b], end=' ')
                c += 1
            if chess_board[a][b] == chess_board[a][-1]:
                print()
