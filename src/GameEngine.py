
import copy


def selectSquare(xInput, yInput): # converts x and y inputs into array
        selectedSquare = [xInput, yInput]
        return selectedSquare

def selectCurrentPiece(board, selectedSquare): # returns piece at selected current square
        currentX = selectedSquare[0]
        currentY = selectedSquare[1]

        currentPiece = board[currentX][currentY]
        return currentPiece

def selectDestination(board, selectedSquare): # returns piece at destination square

        destinationX = selectedSquare[0]
        destinationY = selectedSquare[1]
        destinationPiece = board[destinationX][destinationY]

        return destinationPiece


def move(currentSquare, destinationSquare, currentPiece, boardInput): # moves piece to new square
        currentX = currentSquare[0]
        currentY = currentSquare[1]

        destinationX = destinationSquare[0]
        destinationY = destinationSquare[1]

        boardInput[destinationX][destinationY] = currentPiece
        boardInput[currentX][currentY] = 0

        return boardInput



# moves piece to new square and captures opponent piece
def capture(turn, currentSquare, destinationSquare, currentPiece, boardInput, whiteCapturedInput, blackCapturedInput): 
        currentX = currentSquare[0]
        currentY = currentSquare[1]

        destinationX = destinationSquare[0]
        destinationY = destinationSquare[1]
        
        capturedPiece = boardInput[destinationX][destinationY]
        boardInput[destinationX][destinationY] = currentPiece
        boardInput[currentX][currentY] = 0
        if turn == "white":
            whiteCapturedInput.append(capturedPiece)
        else:
            blackCapturedInput.append(capturedPiece)

        return boardInput


def validate(destinationSquare, possibleMoves, check): # validates move
        
        valid = False
        for i in range(len(possibleMoves)):
                if destinationSquare == possibleMoves[i]:
                    valid = True

        if check == True:
            valid = False


        return valid


def findMoveNotation(files, currentPiece, currentSquare, destinationSquare, captureMove, promotionMove, promotionChoice): # calculates move notation for move made
    destinationX = destinationSquare[0]
    destinationY = destinationSquare[1]

    currentX = currentSquare[0]
    currentY = currentSquare[1]

    if captureMove == True: # move notation for capture moves
        if abs(currentPiece) == 1:
            moveNotation = files[currentX] + "x" + files[destinationX] + str(destinationY+1) # special case where current file used to identify pawn during capture
        elif abs(currentPiece) == 2:
            moveNotation = "Rx" + files[destinationX] + str(destinationY + 1)
        elif abs(currentPiece) == 3:
            moveNotation = "Nx" + files[destinationX] + str(destinationY+1)
        elif abs(currentPiece) == 4:
            moveNotation = "Bx" + files[destinationX] + str(destinationY+1)
        elif abs(currentPiece) == 5:
            moveNotation = "Qx" + files[destinationX] + str(destinationY+1)
        elif abs(currentPiece) == 6:
            moveNotation = "Kx" + files[destinationX] + str(destinationY+1)

    else: # move notation for standard moves
        if abs(currentPiece) == 1:
            moveNotation = files[destinationX] + str(destinationY+1)
        elif abs(currentPiece) == 2:
            moveNotation = "R" + files[destinationX] + str(destinationY + 1)
        elif abs(currentPiece) == 3:
            moveNotation = "N" + files[destinationX] + str(destinationY+1)
        elif abs(currentPiece) == 4:
            moveNotation = "B" + files[destinationX] + str(destinationY+1)
        elif abs(currentPiece) == 5:
            moveNotation = "Q" + files[destinationX] + str(destinationY+1)
        elif abs(currentPiece) == 6:
            moveNotation = "K" + files[destinationX] + str(destinationY+1)

    if promotionMove == True: # move notation for promotion moves
        if abs(promotionChoice) == 2:
            moveNotation = files[destinationX] + str(destinationY + 1) + "=R"
        elif abs(promotionChoice) == 3:
            moveNotation = files[destinationX] + str(destinationY + 1) + "=N"
        elif abs(promotionChoice) == 4:
            moveNotation = files[destinationX] + str(destinationY + 1) + "=B"
        elif abs(promotionChoice) == 5:
            moveNotation = files[destinationX] + str(destinationY + 1) + "=Q"
            
    return moveNotation

    
    


def pawnPossibleMoves(board, currentSquare, turn): # detects pawn possible moves
        
        possibleMoves = []

        currentX = currentSquare[0]
        currentY = currentSquare[1]

        if turn == "white":
    
                if currentX < 8 and currentY+1 < 8: # checks to prevent list index out of range error
                    if board[currentX][currentY+1] == 0:
                          possibleMoves.append([currentX, currentY+1])
                    
                if currentY == 1 and currentX < 8 and currentY+2 < 8:
                    if board[currentX][currentY+1] == 0 and board[currentX][currentY+2] == 0:
                          possibleMoves.append([currentX, currentY + 2])

                if currentX+1 < 8 and currentY+1 < 8 and currentX+1 >= 0: 
                    if board[currentX+1][currentY+1] < 0:
                          possibleMoves.append([currentX+1, currentY+1])

                if currentX-1 < 8 and currentY+1 < 8 and currentX-1 >= 0: # if black piece in possible capture square
                    if board[currentX-1][currentY+1] < 0:
                        possibleMoves.append([currentX-1, currentY+1])
                

        elif turn == "black":

                if currentX < 8 and currentY-1 < 8:
                    if board[currentX][currentY-1] == 0:
                        possibleMoves.append([currentX, currentY-1])

                if currentY == 6 and currentX < 8 and currentY-2 < 8:
                    if board[currentX][currentY-1] == 0 and board[currentX][currentY-2] == 0:
                        possibleMoves.append([currentX, currentY-2])
                    

                if currentX+1 < 8 and currentY-1 < 8 and currentX+1 >= 0:  # if white piece in possible capture square 
                    if board[currentX+1][currentY-1] > 0:
                        possibleMoves.append([currentX+1, currentY-1])

                if currentX-1 < 8 and currentY-1 < 8 and currentX-1 >= 0:
                    if board[currentX-1][currentY-1] > 0:
                        possibleMoves.append([currentX-1, currentY-1])
                     
        return possibleMoves



def rookPossibleMoves(board, currentSquare, turn): # detects rook possible moves
    possibleMoves = []

    currentX = currentSquare[0]
    currentY = currentSquare[1]

    for i in range(currentY, 8): # file movement, increasing
        if i != currentY:
            if turn == "white":
                if board[currentX][i] <= 0:
                    possibleMoves.append([currentX, i])
                if board[currentX][i] != 0:
                    break

            if turn == "black":
                if board[currentX][i] >= 0:
                        possibleMoves.append([currentX, i])
                if board[currentX][i] != 0:
                        break
                 
    for i in range(currentX, 8): # rank movement, increasing
        if i != currentX:
                if turn == "white":
                    if board[i][currentY] <= 0:
                        possibleMoves.append([i, currentY])
                    if board[i][currentY] != 0:
                        break

                
                if turn == "black":
                    if board[i][currentY] >= 0:
                        possibleMoves.append([i, currentY])
                    if board[i][currentY] != 0:
                        break

    for i in range(currentY, -1 , -1): # file movement, decreasing
        if i != currentY:
            if turn == "white":
                if board[currentX][i] <= 0:
                    possibleMoves.append([currentX, i])
                if board[currentX][i] != 0:
                    break

            if turn == "black":
                if board[currentX][i] >= 0:
                        possibleMoves.append([currentX,i])
                if board[currentX][i] != 0:
                        break
                
    for i in range(currentX, -1, -1): # rank movement, decreasing
        if i != currentX:
                if turn == "white":
                    if board[i][currentY] <= 0:
                        possibleMoves.append([i, currentY])
                    if board[i][currentY] != 0:
                        break

                if turn == "black":
                    if board[i][currentY] >= 0:
                        possibleMoves.append([i, currentY])
                    if board[i][currentY] != 0:
                        break
         
         

    return possibleMoves



def bishopPossibleMoves(board, currentSquare, turn): # detects bishop possible moves

    possibleMoves = []
    currentX = currentSquare[0]
    currentY = currentSquare[1]

    x = currentX + 1
    y = currentY + 1
    while x < 8 and y < 8:
        
        if turn == "white" and board[x][y] <= 0:
            possibleMoves.append([x,y])
        elif turn == "black" and board[x][y] >= 0:
            possibleMoves.append([x,y])
        
        if board[x][y] != 0:
            break
        
        x = x + 1
        y = y + 1
            
        


    x = currentX + 1
    y = currentY - 1

    while x < 8 and y >= 0:
        
        if turn == "white" and board[x][y] <= 0:
            possibleMoves.append([x,y])
        elif turn == "black" and board[x][y] >= 0:
            possibleMoves.append([x,y])
        
        if board[x][y] != 0:
            break
        
        x = x + 1
        y = y - 1
    


    x = currentX - 1
    y = currentY + 1

    while x >= 0 and y < 8:
        
        if turn == "white" and board[x][y] <= 0:
            possibleMoves.append([x,y])
        elif turn == "black" and board[x][y] >= 0:
            possibleMoves.append([x,y])
        
        if board[x][y] != 0:
            break
        
        x = x - 1
        y = y + 1


            
    x = currentX - 1
    y = currentY - 1
    while x >= 0 and y >= 0:
        
        if turn == "white" and board[x][y] <= 0:
            possibleMoves.append([x,y])
        elif turn == "black" and board[x][y] >= 0:
            possibleMoves.append([x,y])
        
        if board[x][y] != 0:
            break
        
        x = x - 1
        y = y - 1

    return possibleMoves

def knightPossibleMoves(board, currentSquare, turn): # detects knight possible moves

    possibleMoves = []
    currentX = currentSquare[0]
    currentY = currentSquare[1]

    # appends every possible knight move regardless of restrictions
    possibleMoves.append([currentX+1, currentY+2])
    possibleMoves.append([currentX+1, currentY-2])
    possibleMoves.append([currentX+2, currentY+1])
    possibleMoves.append([currentX+2, currentY-1])
    possibleMoves.append([currentX-1, currentY+2])
    possibleMoves.append([currentX-1, currentY-2])
    possibleMoves.append([currentX-2, currentY+1])
    possibleMoves.append([currentX-2, currentY-1])

    i = 0
    while i < len(possibleMoves): # removes out of bounds ranks
        if possibleMoves[i][0] > 7:
            possibleMoves.pop(i)
            i = i - 1

        elif possibleMoves[i][0] < 0:
            possibleMoves.pop(i)
            i = i -1

        i = i + 1
    i = 0
    while i < len(possibleMoves): # removes out of bounds files
        if possibleMoves[i][1] > 7:
            possibleMoves.pop(i)
            i = i - 1

        elif possibleMoves[i][1] < 0:
            possibleMoves.pop(i)
            i = i - 1

        i = i + 1
    i = 0
    while i < len(possibleMoves): # removes squares containing own pieces

        x = possibleMoves[i][0]
        y = possibleMoves[i][1]
        if turn == "white" and board[x][y] > 0:
            possibleMoves.pop(i)
            i = i - 1
        if turn == "black" and board[x][y] < 0:
            possibleMoves.pop(i)
            i = i - 1
        i = i + 1
    return possibleMoves


def queenPossibleMoves(board, currentSquare, turn): # detects queen possible moves

    possibleMoves = []



    verticalHorizontalMoves = rookPossibleMoves(board, currentSquare, turn) # generates list of vertical and horizontal valid moves
    for i in range(len(verticalHorizontalMoves)):
        possibleMoves.append(verticalHorizontalMoves[i])

    diagonalMoves = bishopPossibleMoves(board, currentSquare, turn) # generates list of valid diagonal moves
    for i in range(len(diagonalMoves)):
        possibleMoves.append(diagonalMoves[i])

    return possibleMoves

def castle(board, turn, side): # performs castle move
    if turn == "white":
        if side == "queenside":
            board[0][0] = 0 # moves rook to new position
            board[3][0] = 2
        else:
            board[7][0] = 0 # moves rook to new position
            board[5][0] = 2
    else:
        if side == "queenside":
            board[0][7] = 0 # moves rook to new position
            board[3][7] = -2
        else:
            board[7][7] = 0 # moves rook to new position
            board[5][7] = -2

    return board

# determines if king can castle, queenside or kingside
def determineCastle(board, currentSquare, turn, possibleMoves, whiteKingMoved, blackKingMoved, whiteLeftRookMoved, whiteRightRookMoved, blackLeftRookMoved, blackRightRookMoved):
    queenSidePossible = True
    kingSidePossible = True
    totalPossibleMoves = []
    pieceMoved = False

    currentX = currentSquare[0]
    currentY = currentSquare[1]

    
    
    if turn == "white" and whiteKingMoved == False:
        for x in range(8):
            for y in range(8):
                if board[x][y] < 0: # generates a list of total black moves
                    square = selectSquare(x, y)
                    piece = selectCurrentPiece(board, square)
                    moves = detectPossibleMoves(board, square, piece, "black", whiteKingMoved, blackKingMoved)


                    for i in range(len(moves)):
                        totalPossibleMoves.append(moves[i])


        for i in range(len(totalPossibleMoves)):
            if totalPossibleMoves[i] == [4,0] or totalPossibleMoves[i] == [3,0] or totalPossibleMoves[i] == [2,0] or totalPossibleMoves[i] == [1,0] or totalPossibleMoves[i] == [0,0]:
                queenSidePossible = False # determines if queen side castling possible
            if totalPossibleMoves[i] == [4,0] or totalPossibleMoves[i] == [5,0] or totalPossibleMoves[i] == [6,0] or totalPossibleMoves[i] == [7,0]:
                kingSidePossible = False # determines if king side castling possible

    elif turn == "black" and blackKingMoved == False:
        for x in range(8):
            for y in range(8):
                if board[x][y] > 0: # generates a list of total white  moves
                    square = selectSquare(x, y)
                    piece = selectCurrentPiece(board, square)
                    moves = detectPossibleMoves(board, square, piece, "white", whiteKingMoved, blackKingMoved)


                    for i in range(len(moves)):
                        totalPossibleMoves.append(moves[i])#


        for i in range(len(totalPossibleMoves)):
            if totalPossibleMoves[i] == [4,7] or totalPossibleMoves[i] == [3,7] or totalPossibleMoves[i] == [2,7] or totalPossibleMoves[i] == [1,7] or totalPossibleMoves[i] == [0,7]:
                queenSidePossible = False # determines if queen side castling possible
            if totalPossibleMoves[i] == [4,7] or totalPossibleMoves[i] == [5,7] or totalPossibleMoves[i] == [6,7] or totalPossibleMoves[i] == [7,7]:
                kingSidePossible = False # determines if king side castling possible
         
    if turn == "white" and whiteKingMoved == False: 
     
        
        if queenSidePossible == True and board[3][0] == 0 and board[2][0] == 0 and board[1][0] == 0 and board[0][0] == 2 and whiteLeftRookMoved == False:
            possibleMoves.append([currentX-2, currentY]) # displays queen side castle possible move on board
        

        if kingSidePossible == True and board[5][0] == 0 and board[6][0] == 0 and board[7][0] == 2 and whiteRightRookMoved == False:
            possibleMoves.append([currentX+2, currentY]) # displays king side castle possible move on board
            
    elif turn == "black" and blackKingMoved == False:

        if queenSidePossible == True and board[3][7] == 0 and board[2][7] == 0 and board[1][7] == 0 and board[0][7] == -2 and blackLeftRookMoved == False:
            possibleMoves.append([currentX-2, currentY]) # displays queen side castle possible move on board
        if kingSidePossible == True and board[5][7] == 0 and board[6][7] == 0 and board[7][7] == -2 and blackRightRookMoved == False:
            possibleMoves.append([currentX+2, currentY]) # displays king side castle possible move on board




def kingPossibleMoves(board, currentSquare, turn, whiteKingMoved, blackKingMoved): # detects king possible moves

    
    possibleMoves = []

    currentX = currentSquare[0]
    currentY = currentSquare[1]

    

    possibleMoves.append([currentX, currentY+1]) # all default king moves
    possibleMoves.append([currentX, currentY-1])
    possibleMoves.append([currentX+1, currentY])
    possibleMoves.append([currentX-1, currentY])
    possibleMoves.append([currentX+1, currentY+1])
    possibleMoves.append([currentX+1, currentY-1])
    possibleMoves.append([currentX-1, currentY+1])
    possibleMoves.append([currentX-1, currentY-1])

    

    i = 0
    while i < len(possibleMoves): # removes positions that are outside of game board
        

        if possibleMoves[i][0] > 7 or possibleMoves[i][0] < 0:
            possibleMoves.pop(i)
            i = i - 1
            
        elif possibleMoves[i][1] > 7 or possibleMoves[i][1] < 0:
            possibleMoves.pop(i)
            i = i - 1

        if i >= 0:


            if turn == "white" and board[possibleMoves[i][0]][possibleMoves[i][1]] > 0: # removes white pieces on white turn
                possibleMoves.pop(i) # removes item entirely from list
                i = i - 1
            elif turn == "black" and board[possibleMoves[i][0]][possibleMoves[i][1]] < 0: # removes black pieces on black turn
                possibleMoves.pop(i)
                i = i - 1

        i = i + 1

    return possibleMoves
        



def promotion(board, destinationSquare, promotionChoice): # performs promotion move (replaces pawn with chosen piece)
    board[destinationSquare[0]][destinationSquare[1]] = promotionChoice
    return board




def detectCheck(board, turn, whiteKingMoved, blackKingMoved): # detects if king in check position
    totalPossibleMoves = []
    check = False
    for x in range(8): # detect king position
        for y in range(8):
            if turn == "white" and board[x][y] == 6:
                kingPos = [x,y]
            elif turn == "black" and board[x][y] == -6:
                kingPos = [x,y]


    for x in range(8): # checks all possible moves of opposite colour to determine if king in check
        for y in range(8):
            if turn == "white":
                if board[x][y] < 0: # checks black pieces


                    
                    square = selectSquare(x, y)
                    piece = selectCurrentPiece(board, square)
                    moves = detectPossibleMoves(board, square, piece, "black", whiteKingMoved, blackKingMoved)


                    for i in range(len(moves)):
                        totalPossibleMoves.append(moves[i])
            else:
                if board[x][y] > 0: # checks white pieces
                    moves = []
                    square = selectSquare(x, y)
                    piece = selectCurrentPiece(board, square)
                    moves = detectPossibleMoves(board, square, piece, "white", whiteKingMoved, blackKingMoved)
                    for i in range(len(moves)):
                        totalPossibleMoves.append(moves[i])               

    for x in range(len(totalPossibleMoves)): # checks within totalPossibleMoves to see if King is under threat
        if totalPossibleMoves[x] == kingPos:
                check = True
                
    return check
                    

def detectCheckmate(board, turn, whiteKingMoved, blackKingMoved): # detects if king in checkmate position (no possible moves can be made)
    checkmate = True
    end = False
    whiteCapturedTemp = []
    blackCapturedTemp = []

    
    for x in range(8):
        for y in range(8):
            if turn == "white" and end == False:
                if board[x][y] > 0: # checks white pieces only
                    tempBoard = copy.deepcopy(board)
                    moves = []
                    square = selectSquare(x, y)
                    piece = selectCurrentPiece(board, square)
                    moves = detectPossibleMoves(board, square, piece, turn, whiteKingMoved, blackKingMoved)


                    for i in range(len(moves)):
                        destinationPiece = tempBoard[moves[i][0]][moves[i][1]]

                        if destinationPiece == 0: # simulates each possible move on board
                            move(square, moves[i], piece, tempBoard)
                        else:
                            capture(turn, square, moves[i], piece, tempBoard, whiteCapturedTemp, blackCapturedTemp)


                        check = detectCheck(tempBoard, turn, whiteKingMoved, blackKingMoved)
                        tempBoard = copy.deepcopy(board)


                        if check == False:
                            checkmate = False
                            end = True # ends loop when valid move found
                            break

                        
            elif turn == "black" and end == False:
                if board[x][y] < 0: # checks black pieces
                    tempBoard = copy.deepcopy(board)
                    moves = []
                    square = selectSquare(x, y)
                    piece = selectCurrentPiece(board, square)
                    moves = detectPossibleMoves(board, square, piece, turn, whiteKingMoved, blackKingMoved)

                    for i in range(len(moves)):
                        destinationPiece = board[moves[i][0]][moves[i][1]]
                        if destinationPiece == 0: # simulates each possible move on board
                            move(square, moves[i], piece, tempBoard) 
                        else:
                            capture(turn, square, moves[i], piece, tempBoard, whiteCapturedTemp, blackCapturedTemp)

                        check = detectCheck(tempBoard, turn, whiteKingMoved, blackKingMoved)


                        tempBoard = copy.deepcopy(board)


                        if check == False:
                            checkmate = False
                            end = True # ends loop when valid move found
                            break
                                
    return checkmate
             


def detectPossibleMoves(board, currentSquare, currentPiece, turn, whiteKingMoved, blackKingMoved): # determines which possible moves algorithm to run based on piece input
        

        if abs(currentPiece) == 1: # displays possible moves of current piece selected
                possibleMoves = pawnPossibleMoves(board, currentSquare, turn)
        elif abs(currentPiece) == 2:
                possibleMoves = rookPossibleMoves(board, currentSquare, turn)
        elif abs(currentPiece) == 3:
                possibleMoves = knightPossibleMoves(board, currentSquare, turn)
        elif abs(currentPiece) == 4:
                possibleMoves = bishopPossibleMoves(board, currentSquare, turn)
        elif abs(currentPiece) == 5:
                possibleMoves = queenPossibleMoves(board, currentSquare, turn)
        elif abs(currentPiece) == 6:
                possibleMoves = kingPossibleMoves(board, currentSquare, turn, whiteKingMoved, blackKingMoved)

        return possibleMoves



    



















    
