import pygame
import os
pygame.init()
pygame.font.init()

from GameEngine import *
from Network import *

import copy
 

screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height]) # sets display window size


colour1 = (0,0,0) # black
colour2 = (255, 255, 255) # white
colour3 = (150, 220, 248) # teal
colour4 = (179, 0, 0) # red
colour5 = (21, 96, 130) # turquoise
colour6 = (82, 148, 212) # blue


titleFont = pygame.font.Font('freesansbold.ttf', 70) # initializes fonts
buttonFont = pygame.font.Font('freesansbold.ttf', 40)
mediumFont = pygame.font.Font('freesansbold.ttf', 30)
smallFont = pygame.font.Font('freesansbold.ttf', 20)
smallerFont = pygame.font.Font('freesansbold.ttf', 15)

displayMoves = True

files = ["a", "b", "c", "d", "e", "f", "g", "h"]
state = "mainMenu"


class Button:
    def __init__(self, colour, x, y, height, width, text, font, fontColour): # initializes new button object
        self.colour = colour
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        self.font = font
        self.fontColour = fontColour


    def draw(self):  # draws button onto screen
        buttonRect = pygame.draw.rect(screen, self.colour, (self.x - (self.width // 2), self.y - (self.height // 2), self.width, self.height))
        text = self.font.render(self.text, True, self.fontColour)
        textRect = text.get_rect(center = (self.x, self.y))
        screen.blit(text, textRect)
        return buttonRect
    
    def changeColour(self, newColour): # changes button object colour
        self.colour = newColour
        pygame.draw.rect(screen, self.colour, (self.x - (self.width // 2), self.y - (self.height // 2), self.width, self.height))

class Title: # displays text inside button
    def __init__(self, text, font, colour, x, y):
        self.text = text
        self.font = font
        self.colour = colour
        self.x = x
        self.y = y

    def display(self):
        title = self.font.render(self.text, True, self.colour)
        titleRect = title.get_rect()
        titleRect.center = (self.x, self.y)
        screen.blit(title, titleRect)

class Box:
    def __init__(self, colour, x, y, width, height, text, textColour, font): # initializes new box object
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textColour = textColour
        self.font = font



    def draw(self): # draws box onto screen
        boxRect = pygame.draw.rect(screen, self.colour, ((self.x, self.y, self.width, self.height)))
        return boxRect
    
    def textInsert(self): # displays text inside box
        text1 = self.font.render(self.text, self.font, self.textColour)
        text1Rect = text1.get_rect(center = ((self.width // 2) + self.x, self.height // 2 + self.y)) # centres text
        screen.blit(text1, text1Rect)

def drawBoard(): # displays chess board template on screen
    y = 400 - (80 * 3.75)


    for i in range(4):
        x = (screen_width //2) - (80 * 4)
        for i in range(4):
            pygame.draw.rect(screen, colour2, ((x, y, 80, 80)))
            x = x + 160

        x = ((screen_width //2) - (80*3))
        for i in range(4):
            pygame.draw.rect(screen, colour6, ((x, y, 80, 80)))
            x = x + 160

        y = y + 160

    y = 400 - (80 * 2.75)

    for i in range(4):
        x = (screen_width //2) - (80 * 4)
        
        
        for i in range(4):
            pygame.draw.rect(screen, colour6, ((x, y, 80, 80)))
            x = x + 160

        x = ((screen_width //2) - (80*3))
        for i in range(4):
            pygame.draw.rect(screen, colour2, ((x, y, 80, 80)))
            x = x + 160

        y = y + 160


    # rank and file labels 

    fileALabel = mediumFont.render("a", 1, colour1)
    fileALabelRect = fileALabel.get_rect(center = (420, 760)) # centres text
    screen.blit(fileALabel, fileALabelRect)

    fileBLabel = mediumFont.render("b", 1, colour1)
    fileBLabelRect = fileBLabel.get_rect(center = (500, 760)) # centres text
    screen.blit(fileBLabel, fileBLabelRect)

    fileCLabel = mediumFont.render("c", 1, colour1)
    fileCLabelRect = fileCLabel.get_rect(center = (580, 760)) # centres text
    screen.blit(fileCLabel, fileCLabelRect)

    fileDLabel = mediumFont.render("d", 1, colour1)
    fileDLabelRect = fileDLabel.get_rect(center = (660, 760)) # centres text
    screen.blit(fileDLabel, fileDLabelRect)

    fileELabel = mediumFont.render("e", 1, colour1)
    fileELabelRect = fileELabel.get_rect(center = (740, 760)) # centres text
    screen.blit(fileELabel, fileELabelRect)

    fileFLabel = mediumFont.render("f", 1, colour1)
    fileFLabelRect = fileFLabel.get_rect(center = (820, 760)) # centres text
    screen.blit(fileFLabel, fileFLabelRect)

    fileGLabel = mediumFont.render("g", 1, colour1)
    fileGLabelRect = fileGLabel.get_rect(center = (900, 760)) # centres text
    screen.blit(fileGLabel, fileGLabelRect)

    fileHLabel = mediumFont.render("h", 1, colour1)
    fileHLabelRect = fileHLabel.get_rect(center = (980, 760)) # centres text
    screen.blit(fileHLabel, fileHLabelRect)


    # rank labels

    rank1Label = mediumFont.render("1", 1, colour1)
    rank1LabelRect = rank1Label.get_rect(center = (360, 705))
    screen.blit(rank1Label, rank1LabelRect)

    rank2Label = mediumFont.render("2", 1, colour1)
    rank2LabelRect = rank2Label.get_rect(center = (360, 625))
    screen.blit(rank2Label, rank2LabelRect)

    rank3Label = mediumFont.render("3", 1, colour1)
    rank3LabelRect = rank3Label.get_rect(center = (360, 545))
    screen.blit(rank3Label, rank3LabelRect)

    rank4Label = mediumFont.render("4", 1, colour1)
    rank4LabelRect = rank4Label.get_rect(center = (360, 465))
    screen.blit(rank4Label, rank4LabelRect)

    rank5Label = mediumFont.render("5", 1, colour1)
    rank5LabelRect = rank5Label.get_rect(center = (360, 385))
    screen.blit(rank5Label, rank5LabelRect)

    rank6Label = mediumFont.render("6", 1, colour1)
    rank6LabelRect = rank6Label.get_rect(center = (360, 305))
    screen.blit(rank6Label, rank6LabelRect)

    rank7Label = mediumFont.render("7", 1, colour1)
    rank7LabelRect = rank7Label.get_rect(center = (360, 225))
    screen.blit(rank7Label, rank7LabelRect)

    rank8Label = mediumFont.render("8", 1, colour1)
    rank8LabelRect = rank8Label.get_rect(center = (360, 145))
    screen.blit(rank8Label, rank8LabelRect)





def loadImage(name):
    base_dir = os.path.dirname(__file__)
    return os.path.join(base_dir, "../assets/images", name)

    

def updateBoard(board): # updates board with piece states
    drawBoard() # resets board contents
    for x in range(8):
        for y in range(8):
            rank = -80*y + 680 + 20
            file = 80*x + 420

            if board[x][y] == 1:
                img = pygame.image.load(loadImage("white pawn.png"))
                imgRect = img.get_rect(center = (file, rank))
                screen.blit(img, imgRect)


            elif board[x][y] == -1:
                img = pygame.image.load(loadImage("black pawn.png"))
                imgRect = img.get_rect(center = (file, rank))
                screen.blit(img, imgRect)
                
            elif board[x][y] == 2:
                img = pygame.image.load(loadImage("white rook.png"))
                imgRect = img.get_rect(center = (file, rank))
                screen.blit(img, imgRect)

            elif board[x][y] == -2:
                img = pygame.image.load(loadImage("black rook.png"))
                imgRect = img.get_rect(center = (file, rank))
                screen.blit(img, imgRect)

            elif board[x][y] == 3:
                img = pygame.image.load(loadImage("white knight.png"))
                imgRect = img.get_rect(center = (file, rank))
                screen.blit(img, imgRect)

            elif board[x][y] == -3:
                img = pygame.image.load(loadImage("black knight.png"))
                imgRect = img.get_rect(center = (file, rank))
                screen.blit(img, imgRect)


            elif board[x][y] == 4:
                img = pygame.image.load(loadImage("white bishop.png"))
                imgRect = img.get_rect(center = (file, rank))
                screen.blit(img, imgRect)

            elif board[x][y] == -4:
                img = pygame.image.load(loadImage("black bishop.png"))
                imgRect = img.get_rect(center = (file, rank))
                screen.blit(img, imgRect)


            elif board[x][y] == 5:
                img = pygame.image.load(loadImage("white queen.png"))
                imgRect = img.get_rect(center = (file, rank))
                screen.blit(img, imgRect)

            elif board[x][y] == -5:
                img = pygame.image.load(loadImage("black queen.png"))
                imgRect = img.get_rect(center = (file, rank))
                screen.blit(img, imgRect)


            elif board[x][y] == 6:
                img = pygame.image.load(loadImage("white king.png"))
                imgRect = img.get_rect(center = (file, rank))
                screen.blit(img, imgRect)

            elif board[x][y] == -6:
                img = pygame.image.load(loadImage("black king.png"))
                imgRect = img.get_rect(center = (file, rank))
                screen.blit(img, imgRect)



def capturedPieces(whiteCaptured, blackCaptured):

    capturedPieces1Box = Box(colour5, 35, 100, 300, 200, 0, 0, 0) # redraws captured pieces boxes, to reset contents
    capturedPieces1Box.draw()

    capturedPieces2Box = Box(colour5, 35, screen_height-250, 300, 200, 0, 0, 0)
    capturedPieces2Box.draw()

    whitePawnsCaptured = 0 # initializing captured piece counters to zero
    whiteRooksCaptured = 0
    whiteKnightsCaptured = 0
    whiteBishopsCaptured = 0
    whiteQueenCaptured = 0
    whiteKingCaptured = 0

    blackPawnsCaptured = 0
    blackRooksCaptured = 0
    blackKnightsCaptured = 0
    blackBishopsCaptured = 0
    blackQueenCaptured = 0
    blackKingCaptured = 0


    for i in range(len(whiteCaptured)): # counts how many of each black piece captured by white
        if abs(whiteCaptured[i]) == 1:
            blackPawnsCaptured = blackPawnsCaptured + 1
        elif abs(whiteCaptured[i]) == 2:
            blackRooksCaptured = blackRooksCaptured + 1
        elif abs(whiteCaptured[i]) == 3:
            blackKnightsCaptured = blackKnightsCaptured + 1
        elif abs(whiteCaptured[i]) == 4:
            blackBishopsCaptured = blackBishopsCaptured + 1
        elif abs(whiteCaptured[i]) == 5:
            blackQueenCaptured = blackQueenCaptured + 1
        elif abs(whiteCaptured[i]) == 6:
            blackKingCaptured = blackKingCaptured + 1

    for i in range(len(blackCaptured)): # counts how many of each white piece captured by black
        if abs(blackCaptured[i]) == 1:
            whitePawnsCaptured = whitePawnsCaptured + 1
        elif abs(blackCaptured[i]) == 2:
            whiteRooksCaptured = whiteRooksCaptured + 1
        elif abs(blackCaptured[i]) == 3:
            whiteKnightsCaptured = whiteKnightsCaptured + 1
        elif abs(blackCaptured[i]) == 4:
            whiteBishopsCaptured = whiteBishopsCaptured + 1
        elif abs(blackCaptured[i]) == 5:
            whiteQueenCaptured = whiteQueenCaptured + 1
        elif abs(blackCaptured[i]) == 6:
            whiteKingCaptured = whiteKingCaptured + 1

    
    blackPawnsText = smallFont.render(f"{blackPawnsCaptured} x", smallFont, colour2)
    blackPawnsTextRect = blackPawnsText.get_rect(center = (90, 140)) # centres text
    screen.blit(blackPawnsText, blackPawnsTextRect)

    blackPawnIcon = pygame.image.load(loadImage("black pawn.png"))
    blackPawnIconRect = blackPawnIcon.get_rect(center= (150, 140))
    screen.blit(blackPawnIcon, blackPawnIconRect)

    blackKnightsText = smallFont.render(f"{blackKnightsCaptured} x", smallFont, colour2)
    blackKnightsTextRect = blackKnightsText.get_rect(center = (90, 200)) # centres text
    screen.blit(blackKnightsText, blackKnightsTextRect)

    blackKnightIcon = pygame.image.load(loadImage("black knight.png"))
    blackKnightIconRect = blackKnightIcon.get_rect(center=(150, 200))
    screen.blit(blackKnightIcon, blackKnightIconRect)

    
    blackBishopsText = smallFont.render(f"{blackBishopsCaptured} x", smallFont, colour2)
    blackBishopsTextRect = blackBishopsText.get_rect(center = (90, 260)) # centres text
    screen.blit(blackBishopsText, blackBishopsTextRect)

    blackBishopIcon = pygame.image.load(loadImage("black bishop.png"))
    blackBishopIconRect = blackBishopIcon.get_rect(center=(150, 260))
    screen.blit(blackBishopIcon, blackBishopIconRect)

    blackRookText = smallFont.render(f"{blackRooksCaptured} x", smallFont, colour2)
    blackRookTextRect = blackRookText.get_rect(center = (220, 170)) # centres text
    screen.blit(blackRookText, blackRookTextRect)

    blackRookIcon = pygame.image.load(loadImage("black rook.png"))
    blackRookIconRect = blackRookIcon.get_rect(center=(270, 170))
    screen.blit(blackRookIcon, blackRookIconRect)

    blackQueenText = smallFont.render(f"{blackQueenCaptured} x", smallFont, colour2)
    blackQueenTextRect = blackQueenText.get_rect(center = (220, 230)) # centres text
    screen.blit(blackQueenText, blackQueenTextRect)

    blackQueenIcon = pygame.image.load(loadImage("black queen.png"))
    blackQueenIconRect = blackQueenIcon.get_rect(center=(270, 230))
    screen.blit(blackQueenIcon, blackQueenIconRect)

    whitePawnsText = smallFont.render(f"{whitePawnsCaptured} x", smallFont, colour2)
    whitePawnsTextRect = whitePawnsText.get_rect(center = (90, 590)) # centres text
    screen.blit(whitePawnsText, whitePawnsTextRect)
    
    whitePawnIcon = pygame.image.load(loadImage("white pawn.png"))
    whitePawnIconRect = whitePawnIcon.get_rect(center= (150,590))
    screen.blit(whitePawnIcon, whitePawnIconRect)

    whiteKnightsText = smallFont.render(f"{whiteKnightsCaptured} x", smallFont, colour2)
    whiteKnightsTextRect = whiteKnightsText.get_rect(center = (90, 650)) # centres text
    screen.blit(whiteKnightsText, whiteKnightsTextRect)

    whiteKnightIcon = pygame.image.load(loadImage("white knight.png"))
    whiteKnightIconRect = whiteKnightIcon.get_rect(center=(150, 650))
    screen.blit(whiteKnightIcon, whiteKnightIconRect)

    whiteBishopsText = smallFont.render(f"{whiteBishopsCaptured} x", smallFont, colour2)
    whiteBishopsTextRect = whiteBishopsText.get_rect(center = (90, 710)) # centres text
    screen.blit(whiteBishopsText, whiteBishopsTextRect)

    whiteBishopIcon = pygame.image.load(loadImage("white bishop.png"))
    whiteBishopIconRect = whiteBishopIcon.get_rect(center=(150, 710))
    screen.blit(whiteBishopIcon, whiteBishopIconRect)

    whiteRookText = smallFont.render(f"{whiteRooksCaptured} x", smallFont, colour2)
    whiteRookTextRect = whiteRookText.get_rect(center = (220, 620)) # centres text
    screen.blit(whiteRookText, whiteRookTextRect)

    whiteRookIcon = pygame.image.load(loadImage("white rook.png"))
    whiteRookIconRect = whiteRookIcon.get_rect(center= (270, 620))
    screen.blit(whiteRookIcon, whiteRookIconRect)
    
    whiteQueenText = smallFont.render(f"{whiteQueenCaptured} x", smallFont, colour2)
    whiteQueenTextRect = whiteQueenText.get_rect(center = (220, 680)) # centres text
    screen.blit(whiteQueenText, whiteQueenTextRect)

    whiteQueenIcon = pygame.image.load(loadImage("white queen.png"))
    whiteQueenIconRect = whiteQueenIcon.get_rect(center=(270, 680))
    screen.blit(whiteQueenIcon, whiteQueenIconRect)





def displayMovelog(moveLogList):
    moveLogBox = Box(colour5, 1075, 100, 280, 640, "", "", "") # redraws move log list, to reset contents
    moveLogBox.draw()

    

    x = 1080
    y = 120
    num = 1
    count = 1
    column = 1
    for i in range(len(moveLogList)):

        move = moveLogList[i]
        if i % 2 == 0: # displays white moves from list in white
            moveText = smallFont.render(f"{num}. {move}", 1, colour2)
            moveTextRect = moveText.get_rect(midleft=(x,y))
            screen.blit(moveText, moveTextRect)
        
        else: # displays black moves from list in black
            moveText = smallFont.render(f"{num}. {move}", 1, colour1)
            moveTextRect = moveText.get_rect(midleft=(x,y))
            screen.blit(moveText, moveTextRect)

        y = y + 30 # starts new line for each move
        num = num + 1
        count = count + 1
        

        if count > 21: # starts new column if current column fills up
            x = x + 90
            y = 120
            count = 1
            column = column + 1

        if column > 3: # erases box and starts again if three columns fill up
            moveLogBox = Box(colour5, 1075, 100, 280, 640, "", "", "")
            moveLogBox.draw()
            count = 1
            column = 1
            x = 1080
            y = 120



            
def displayGameUpdate(turn, promote, destinationSquare, whiteCheck, blackCheck, valid, winner):
    gameUpdateBox = Box(colour5, 35, 320, 300, 130, "", "", "") # redraws box, resetting contents
    gameUpdateBox.draw()

    titleText = smallFont.render("Game Updates", 1, colour1) # displays box text
    titleTextRect = titleText.get_rect(center = (185, 340))
    screen.blit(titleText, titleTextRect)

    if promote == True: # displays promotion menu

        promoteText1 = smallFont.render("Select piece to promote", 1, colour2) # promotion subtitle
        promoteText1Rect = promoteText1.get_rect(center = (180, 370))
        screen.blit(promoteText1, promoteText1Rect)

        promoteText2 = smallFont.render("pawn to:", 1, colour2)
        promoteText2Rect = promoteText2.get_rect(center = (180, 390))
        screen.blit(promoteText2, promoteText2Rect)

        if turn == "white":
            newSize = (50,50) # defines new icon size
            whiteKnight = pygame.image.load(loadImage("white knight.png")) 
            whiteKnightIcon = pygame.transform.scale(whiteKnight, newSize)
            whiteKnightIconRect = whiteKnightIcon.get_rect(center=(90, 420))
            screen.blit(whiteKnightIcon, whiteKnightIconRect) # displays knight icon

            whiteBishop = pygame.image.load(loadImage("white bishop.png"))
            whiteBishopIcon = pygame.transform.scale(whiteBishop, newSize)
            whiteBishopIconRect = whiteBishopIcon.get_rect(center=(150, 420))
            screen.blit(whiteBishopIcon, whiteBishopIconRect) # displays bishop icon


            whiteRook= pygame.image.load(loadImage("white rook.png"))
            whiteRookIcon = pygame.transform.scale(whiteRook, newSize)
            whiteRookIconRect = whiteRookIcon.get_rect(center=(210, 420))
            screen.blit(whiteRookIcon, whiteRookIconRect) # displays rook icon

            whiteQueen = pygame.image.load(loadImage("white queen.png"))
            whiteQueenIcon = pygame.transform.scale(whiteQueen, newSize)
            whiteQueenIconRect = whiteQueenIcon.get_rect(center=(270, 420))
            screen.blit(whiteQueenIcon, whiteQueenIconRect) # displays queen icon
            pygame.display.update()

            promotionChoice = 1
            while promotionChoice < 2 or promotionChoice > 5:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # only process left mouse clicks
                        pos = pygame.mouse.get_pos() # obtain mouse click position
                        if whiteKnightIconRect.collidepoint(pos): # determine which piece has been selected
                            promotionChoice = 3
                        elif whiteBishopIconRect.collidepoint(pos):
                            promotionChoice = 4
                        elif whiteRookIconRect.collidepoint(pos):
                            promotionChoice = 2
                        elif whiteQueenIconRect.collidepoint(pos):
                            promotionChoice = 5
                        else:
                            promotionChoice = -1
                            break

                         # promote pawn on board to the promotionChoice
                        return promotionChoice
        else:
            newSize = (50,50) # defines new icon size
            blackKnight = pygame.image.load(loadImage("black knight.png"))
            blackKnightIcon = pygame.transform.scale(blackKnight, newSize)
            blackKnightIconRect = blackKnightIcon.get_rect(center=(90, 420))
            screen.blit(blackKnightIcon, blackKnightIconRect) # displays knight icon

            blackBishop = pygame.image.load(loadImage("black bishop.png"))
            blackBishopIcon = pygame.transform.scale(blackBishop, newSize)
            blackBishopIconRect = blackBishopIcon.get_rect(center=(150, 420))
            screen.blit(blackBishopIcon, blackBishopIconRect) # displays bishop icon

            blackRook= pygame.image.load(loadImage("black rook.png"))
            blackRookIcon = pygame.transform.scale(blackRook, newSize)
            blackRookIconRect = blackRookIcon.get_rect(center=(210, 420))
            screen.blit(blackRookIcon, blackRookIconRect) # displays rook icon

            blackQueen = pygame.image.load(loadImage("black queen.png"))
            blackQueenIcon = pygame.transform.scale(blackQueen, newSize)
            blackQueenIconRect = blackQueenIcon.get_rect(center=(270, 420))
            screen.blit(blackQueenIcon, blackQueenIconRect) # displays queen icon
            pygame.display.update()

            promotionChoice = -1
            while promotionChoice > -2 or promotionChoice < -5:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # only process left mouse clicks
                        pos = pygame.mouse.get_pos() # obtain mouse click position
                        if blackKnightIconRect.collidepoint(pos): # determine which piece has been selected
                            promotionChoice = -3
                        elif blackBishopIconRect.collidepoint(pos):
                            promotionChoice = -4
                        elif blackRookIconRect.collidepoint(pos):
                            promotionChoice = -2
                        elif blackQueenIconRect.collidepoint(pos):
                            promotionChoice = -5
                        else:
                            promotionChoice = 1
                            break

                        promotion(board, destinationSquare, promotionChoice) # promote pawn on board to the promotionChoice
                        return promotionChoice


    if turn == "white" and valid == False:
            validText = smallFont.render("Move invalid!", 1, colour2) # displays invalid message for white moves
            validTextRect = validText.get_rect(center = (180, 390))
            screen.blit(validText, validTextRect)
    elif turn == "black" and valid == False:
            validText = smallFont.render("Move invalid!", 1, colour1) # displays invalid message for black moves
            validTextRect = validText.get_rect(center = (180, 390))
            screen.blit(validText, validTextRect)
    
    
    if whiteCheck == True:
        checkText = smallFont.render("White is in check!", 1, colour2) # displays check message for white
        checkTextRect = checkText.get_rect(center = (180, 390))
        screen.blit(checkText, checkTextRect)
    elif blackCheck == True:
        checkText = smallFont.render("Black is in check!", 1, colour1) # displays check message for black
        checkTextRect = checkText.get_rect(center = (180, 390))
        screen.blit(checkText, checkTextRect)


    if winner == "white": # white wins message
        winnerText1 = smallFont.render("Black is in checkmate!", 1, colour2)
        winnerText1Rect = winnerText1.get_rect(center = (180, 390))
        screen.blit(winnerText1, winnerText1Rect)

        winnerText2 = smallFont.render("White wins!", 1, colour2)
        winnerText2Rect = winnerText2.get_rect(center = (180, 430))
        screen.blit(winnerText2, winnerText2Rect)

    elif winner == "black": # black wins message
        winnerText1 = smallFont.render("White is in checkmate!", 1, colour1)
        winnerText1Rect = winnerText1.get_rect(center = (180, 390))
        screen.blit(winnerText1, winnerText1Rect)

        winnerText2 = smallFont.render("Black wins!", 1, colour1)
        winnerText2Rect = winnerText2.get_rect(center = (180, 430))
        screen.blit(winnerText2, winnerText2Rect)

    elif winner == "stalemate": # draw message
        winnerText1 = smallFont.render("Stalemate!", 1, colour2)
        winnerText1Rect = winnerText1.get_rect(center = (180, 390))
        screen.blit(winnerText1, winnerText1Rect)

        winnerText2 = smallFont.render("Draw!", 1, colour1)
        winnerText2Rect = winnerText2.get_rect(center = (180, 430))
        screen.blit(winnerText2, winnerText2Rect)

    pygame.display.update()





        
def gameLoop(gameFinished, board, turn, network, state):
    whiteKingMoved = False # defines variables at start of new game
    blackKingMoved = False
    whiteLeftRookMoved = False
    whiteRightRookMoved = False
    blackLeftRookMoved = False
    blackRightRookMoved = False
    whiteCaptured = []
    blackCaptured = []
    movelogList = []
    

    displayGameUpdate(turn, False, [0,0], False, False, True, 0) # displays blank game update box


    while gameFinished == False:
        displayMovelog(movelogList) # displays blank move log box
        updateBoard(board) # displays pieces in starting position on board
        capturedPieces(whiteCaptured, blackCaptured) # displays blank captured piece boxes
        pygame.display.flip()

        if turn == "white":
            currentPiece = -1
            valid = False
            promotionMove = False
            promotionChoice = 0

            
            while valid == False:
                boardPossibleMoves = []
                possibleMoves = []
                currentPiece = -1
                destinationPiece = 1
                
                updateBoard(board)
                pygame.display.flip()

                while currentPiece <= 0: # piece selection


                    for event in pygame.event.get(): # scans and handles events in game loop
                         x = pygame.mouse.get_pos()[0]
                         y = pygame.mouse.get_pos()[1]
                         
                         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (x > 380 and x < 1020) and (y > 100 and y < 740): # detects left click within board boundary


                            xInput = int((x-380)/(1020-380) * 8 // 1)
                            yInput = int((y-740)/(100-740) * 8 // 1)

    
                            currentSquare = selectSquare(xInput, yInput) # returns coordinates of selected square
                            currentPiece = selectCurrentPiece(board, currentSquare)

                boardX = 80*xInput + 420
                boardY = -80*yInput + 700

                leftX = boardX - 39 # calculates board boundaries
                rightX = boardX + 37
                topY = boardY - 39
                bottomY = boardY + 37

                # highlights selected piece box
                pygame.draw.line(screen, colour5, (leftX, bottomY), (rightX, bottomY),5) # bottom horizontal
                pygame.draw.line(screen, colour5, (leftX, topY), (rightX, topY),5) # top horizontal
                pygame.draw.line(screen, colour5, (leftX, bottomY), (leftX, topY),5) # left vertical
                pygame.draw.line(screen, colour5, (rightX, bottomY), (rightX, topY),5) # right vertical
                pygame.display.update()

                possibleMoves = detectPossibleMoves(board, currentSquare, currentPiece, turn, whiteKingMoved, blackKingMoved) # detects selected piece's possible moves
                if currentPiece == 6: # determines whether king can castle
                    determineCastle(board, currentSquare, turn, possibleMoves, whiteKingMoved, blackKingMoved, whiteLeftRookMoved, whiteRightRookMoved, blackLeftRookMoved, blackRightRookMoved)


                for i in range(len(possibleMoves)):  # calculates board position of possible moves
                    arrayX = possibleMoves[i][0]
                    arrayY = possibleMoves[i][1]

                    boardX = 80*arrayX + 420
                    boardY = -80*arrayY + 700

                    boardPossibleMoves.append([boardX, boardY])
                
                if displayMoves == True:
                    for i in range(len(boardPossibleMoves)): # display of possible moves on screen
                        if board[(boardPossibleMoves[i][0] - 420)//80][(boardPossibleMoves[i][1] - 700)//-80] != 0:


                            leftX = boardPossibleMoves[i][0] - 39
                            rightX = boardPossibleMoves[i][0] + 37
                            topY = boardPossibleMoves[i][1] - 39
                            bottomY = boardPossibleMoves[i][1] + 37
                            
                            #highlights possible pieces to capture
                            pygame.draw.line(screen, colour4, (leftX, bottomY), (rightX, bottomY),5) # bottom horizontal
                            pygame.draw.line(screen, colour4, (leftX, topY), (rightX, topY),5) # top horizontal
                            pygame.draw.line(screen, colour4, (leftX, bottomY), (leftX, topY),5) # left vertical
                            pygame.draw.line(screen, colour4, (rightX, bottomY), (rightX, topY),5) # right vertical
                            
                        else:
                            # displays empty possible move square
                            pygame.draw.circle(screen, colour1, (boardPossibleMoves[i][0], boardPossibleMoves[i][1]), 15)



                        pygame.display.update()



                while destinationPiece > 0: # selecting piece destination
                    for event in pygame.event.get(): # scans and handles events in game loop
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (x > 380 and x < 1020) and (y > 100 and y < 740): # detects left click within board boundary

                                xInput = int((x-380)/(1020-380) * 8 // 1)
                                yInput = int((y-740)/(100-740) * 8 // 1)

                                destinationSquare = selectSquare(xInput, yInput) # select destination square based on mouse input


                                if destinationSquare == currentSquare:
                                    valid = False
                                    destinationPiece = -1 # resets loop and allows player to deselect piece
                                    break

                                destinationPiece = selectDestination(board, destinationSquare)

                                
                                tempBoard = copy.deepcopy(board) # creates copy of board
                                tempWhiteCaptured = copy.deepcopy(whiteCaptured)
                                tempBlackCaptured = copy.deepcopy(blackCaptured)

                                if destinationPiece == 0: # simulates move on temporary copy of board
                                    tempBoard = move(currentSquare, destinationSquare, currentPiece, tempBoard)
                                else:
                                    tempBoard = capture(turn, currentSquare, destinationSquare, currentPiece, tempBoard, tempWhiteCaptured, tempBlackCaptured)

                                check = detectCheck(tempBoard, turn, whiteKingMoved, blackKingMoved) # determines whether attempted move puts player into check
                                valid = validate(destinationSquare, possibleMoves, check)

                                if valid == False:
                                    displayGameUpdate(turn, False, 0, 0, 0, False, 0) # displays move invalid message


            if destinationPiece == 0: # updates board
                captureMove = False
                board = move(currentSquare, destinationSquare, currentPiece, board)
                moveNotation = findMoveNotation(files, currentPiece, currentSquare, destinationSquare, captureMove, promotionMove, promotionChoice) # generates current move's notation

                if currentPiece == 6 and (destinationSquare[0] - currentSquare[0]) == -2:
                    castle(board, turn, "queenside")
                    moveNotation = "0-0-0" # queen side castle move notation
                elif currentPiece == 6 and (destinationSquare[0] - currentSquare[0]) == 2:
                    castle(board, turn, "kingside")
                    moveNotation = "0-0" # king side castle move notation

                
            else:
                captureMove = True
                board = capture(turn, currentSquare, destinationSquare, currentPiece, board, whiteCaptured, blackCaptured)
                moveNotation = findMoveNotation(files, currentPiece, currentSquare, destinationSquare, captureMove, promotionMove, promotionChoice) # generates current move's notation


            if currentPiece == 6:
                whiteKingMoved = True # determines whether white king has moved
            elif currentPiece == 2 and currentSquare == [0,0]:
                whiteLeftRookMoved = True # determines whether left white rook has moved
            elif currentPiece == 2 and currentSquare == [7,0]:
                whiteRightRookMoved = True # determines whether right white rook has moved

            if currentPiece == 1 and destinationSquare[1] == 7:
                promotionMove = True
                promotionChoice = displayGameUpdate("white", True, destinationSquare, False, False, False, 0) # will promote on board
                board = promotion(board, destinationSquare, promotionChoice)
                moveNotation = findMoveNotation(files, currentPiece, currentSquare, destinationSquare, captureMove, promotionMove, promotionChoice) # generates move notation for promotion



            movelogList.append(moveNotation)
            displayMovelog(movelogList)          

            
            capturedPieces(whiteCaptured, blackCaptured)
            updateBoard(board)
    
            pygame.display.flip()

            turn = "black" # determines whether move puts other player into check
            blackCheck = detectCheck(board, turn, whiteKingMoved, blackKingMoved)
            blackCheckmate = detectCheckmate(board, turn, whiteKingMoved, blackKingMoved)
            displayGameUpdate(turn, False, 0, False, blackCheck, True, 0)

            if state == "LANboard":
               
                network.serverSend(board, moveNotation, blackCheck, whiteCaptured) # sends game information
                
                whiteCheckmate = detectCheckmate(board, "white", whiteKingMoved, blackKingMoved)
                if blackCheckmate == True:
                    if blackCheck == False or whiteCheckmate == True: # detects stalemate position
                        winner = "stalemate"
                    else: # detects white win position
                        winner = "white"

                    if state == "LANBoard":
                        Network.serverEnd() # terminates network connection during LAN game

                    gameFinished = True # set to true to end game loop
                    endState =  [winner, movelogList, whiteCaptured, blackCaptured]  
                    return endState # returns final game state
                
                board = network.serverReceiveBoard() # waits for opponent to act on sent move, and send back response
                moveMade = network.serverReceiveMovelog()
                whiteCheck = network.serverReceiveCheck()
                blackCaptured = network.serverReceiveCaptured()  


                for i in range(len(blackCaptured)):
                    blackCaptured[i] = int(blackCaptured[i])

                movelogList.append(moveMade)

                
                updateBoard(board)
                capturedPieces(whiteCaptured, blackCaptured)
                displayMovelog(movelogList) # displays and updates screen with received opponent response on screen
                displayGameUpdate(turn, False, 0, whiteCheck, False, True, 0)
                pygame.display.update()
                pygame.display.flip()

                whiteCheckmate = detectCheckmate(board, "white", whiteKingMoved, blackKingMoved) # detects if player in checkmate
                whiteCheck = detectCheck(board, "white", whiteKingMoved, blackKingMoved)
                
                if whiteCheckmate == True:
                    blackCheckmate = detectCheckmate(board, "black", whiteKingMoved, blackKingMoved) # checks for stalemate conditions (both players in check)
                    if blackCheckmate == True or whiteCheck == False:
                        winner = "stalemate"
                    else:
                        winner = "black"
                    gameFinished = True # set to true to end game loop
                    network.serverEnd() # terminates network connection

                    endState = [winner, movelogList, whiteCaptured, blackCaptured]
                    return endState # ends game loop and returns final game state

                turn = "white"

            blackCheckmate = detectCheckmate(board, "black", whiteKingMoved, blackKingMoved) # determines whether opponent in checkmate
            blackCheck = detectCheck(board, "black", whiteKingMoved, blackKingMoved)
            whiteCheckmate = detectCheckmate(board, "white", whiteKingMoved, blackKingMoved) # determines whether player in checkmate as well as opponent


            if blackCheckmate == True:
                if blackCheck == False or whiteCheckmate == True: # detects stalemate position
                    winner = "stalemate"
                else: # detects white win position
                    winner = "white"

                if state == "LANBoard":
                    Network.serverEnd() # terminates network connection during LAN game

                gameFinished = True # set to true to end game loop
                endState =  [winner, movelogList, whiteCaptured, blackCaptured]  
                return endState # returns final game state




                    

        elif turn == "black":
            currentPiece = 1
            valid = False
            promotionMove = False
            promotionChoice = 0
            

            while valid == False:
                possibleMoves = []
                boardPossibleMoves = []
                currentPiece = 1
                destinationPiece = -1

                updateBoard(board)
                pygame.display.flip()

                
                while currentPiece >= 0: # select current piece
                    for event in pygame.event.get(): # scans and handles events in game loop
                         x = pygame.mouse.get_pos()[0]
                         y = pygame.mouse.get_pos()[1]
                         
                         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (x > 380 and x < 1020) and (y > 80 and y < 720): # detects left click within board boundary
    
                            xInput = int((x-380)/(1020-380) * 8 // 1) # converts mouse click coordinates into square position
                            yInput = int((y-740)/(100-740) * 8 // 1)
 
                            currentSquare = selectSquare(xInput, yInput) # returns coordinates of selected square
                            currentPiece = selectCurrentPiece(board, currentSquare)

                boardX = 80*xInput + 420
                boardY = -80*yInput + 700

                leftX = boardX - 39
                rightX = boardX + 37
                topY = boardY - 39
                bottomY = boardY + 37

                # highlights selected piece box

                pygame.draw.line(screen, colour5, (leftX, bottomY), (rightX, bottomY),5) # bottom horizontal
                pygame.draw.line(screen, colour5, (leftX, topY), (rightX, topY),5) # top horizontal
                pygame.draw.line(screen, colour5, (leftX, bottomY), (leftX, topY),5) # left vertical
                pygame.draw.line(screen, colour5, (rightX, bottomY), (rightX, topY),5) # right vertical
                pygame.display.update()

                    
                possibleMoves = detectPossibleMoves(board, currentSquare, currentPiece, turn, whiteKingMoved, blackKingMoved)
                if currentPiece == -6:
                    determineCastle(board, currentSquare, turn, possibleMoves, whiteKingMoved, blackKingMoved, whiteLeftRookMoved, whiteRightRookMoved, blackLeftRookMoved, blackRightRookMoved)

                for i in range(len(possibleMoves)):
                    arrayX = possibleMoves[i][0]
                    arrayY = possibleMoves[i][1]

                    boardX = 80*arrayX + 420
                    boardY = -80*arrayY + 700 

                    boardPossibleMoves.append([boardX, boardY])
                
                if displayMoves == True:
                    for i in range(len(boardPossibleMoves)): # draws dot or highlights possible move squars
                        if board[(boardPossibleMoves[i][0] - 420)//80][(boardPossibleMoves[i][1] - 700)//-80] != 0:


                            leftX = boardPossibleMoves[i][0] - 39
                            rightX = boardPossibleMoves[i][0] + 37
                            topY = boardPossibleMoves[i][1] - 39
                            bottomY = boardPossibleMoves[i][1] + 37

                            # highlights possible pieces to capture

                            pygame.draw.line(screen, colour4, (leftX, bottomY), (rightX, bottomY),5) # bottom horizontal
                            pygame.draw.line(screen, colour4, (leftX, topY), (rightX, topY),5) # top horizontal
                            pygame.draw.line(screen, colour4, (leftX, bottomY), (leftX, topY),5) # left vertical
                            pygame.draw.line(screen, colour4, (rightX, bottomY), (rightX, topY),5) # right vertical
                        else:
                            # displays empty possible move square
                            pygame.draw.circle(screen, colour1, (boardPossibleMoves[i][0], boardPossibleMoves[i][1]), 15)

                        pygame.display.update()

                

                while destinationPiece < 0: # destination selection loop
                    for event in pygame.event.get(): # scans and handles events in game loop
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (x > 380 and x < 1020) and (y > 80 and y < 720): # detects left click within board boundary


                                xInput = int((x-380)/(1020-380) * 8 // 1)
                                yInput = int((y-740)/(100-740) * 8 // 1)

                                
                    
                                destinationSquare = selectSquare(xInput, yInput) # select destination square based on mouse input

                                if destinationSquare == currentSquare:
                                    valid = False
                                    destinationPiece = 1 # allows player to deselect piece
                                    break


                                destinationPiece = selectDestination(board, destinationSquare)
  

                                tempBoard = copy.deepcopy(board) # creates copy of board
                                tempWhiteCaptured = copy.deepcopy(whiteCaptured)
                                tempBlackCaptured = copy.deepcopy(blackCaptured)

                                if destinationPiece == 0: # simulates move on temporary copy of board
                                    tempBoard = move(currentSquare, destinationSquare, currentPiece, tempBoard)
                                else:
                                    tempBoard = capture(turn, currentSquare, destinationSquare, currentPiece, tempBoard, tempWhiteCaptured, tempBlackCaptured)

                                check = detectCheck(tempBoard, turn, whiteKingMoved, blackKingMoved) # determines whether attempted move puts player into check
                                valid = validate(destinationSquare, possibleMoves, check)

                                if valid == False:
                                    displayGameUpdate(turn, False, 0, 0, 0, False, 0) # displays move invalid message
            


            if destinationPiece == 0: # updates board
                captureMove = False
                board = move(currentSquare, destinationSquare, currentPiece, board)
                moveNotation = findMoveNotation(files, currentPiece, currentSquare, destinationSquare, captureMove, promotionMove, promotionChoice) # generates current move's notation

                if currentPiece == -6 and (destinationSquare[0] - currentSquare[0]) == -2:
                    castle(board, turn, "queenside")
                    moveNotation = "0-0-0" # queen side castle move notation
                elif currentPiece == -6 and (destinationSquare[0] - currentSquare[0]) == 2:
                    castle(board, turn, "kingside")
                    moveNotation = "0-0" # king side castle move notation
            else:
                captureMove = True
                board = capture(turn, currentSquare, destinationSquare, currentPiece, board, whiteCaptured, blackCaptured)
                moveNotation = findMoveNotation(files, currentPiece, currentSquare, destinationSquare, captureMove, promotionMove, promotionChoice) # generates current move's notation

            if currentPiece == -6:
                blackKingMoved = True # determines whether black king has moved
            elif currentPiece == -2 and currentSquare == [0,7]:
                blackLeftRookMoved = True # determines whether left black rook has moved
            elif currentPiece == -2 and currentSquare == [7,7]:
                blackRightRookMoved = True # determines whether right black rook has moved

            if currentPiece == -1 and destinationSquare[1] == 0:
                promotionMove = True
                promotionChoice = displayGameUpdate("black", True, destinationSquare, False, False, True, 0) # will promote on board
                board = promotion(board, destinationSquare, promotionChoice)
                moveNotation = findMoveNotation(files, currentPiece, currentSquare, destinationSquare, captureMove, promotionMove, promotionChoice) # generates move notation for promotion


            movelogList.append(moveNotation)
            displayMovelog(movelogList)
            capturedPieces(whiteCaptured, blackCaptured)
            updateBoard(board)
            pygame.display.flip()

            turn = "white" # determines whether move puts other player into check
            check = detectCheck(board, turn, whiteKingMoved, blackKingMoved)
            displayGameUpdate(turn, False, 0, check, False, True, 0)



            whiteCheckmate = detectCheckmate(board, "white", whiteKingMoved, blackKingMoved) # detects if opponent in checkmate
            whiteCheck = detectCheck(board, "white", whiteKingMoved, blackKingMoved)

            if whiteCheckmate == True:
                if whiteCheck == False or blackCheckmate == True: # detects stalemate position
                    winner = "stalemate"
                else: # detects black win position
                    winner = "black"

                gameFinished = True
                endState =  [winner, movelogList, whiteCaptured, blackCaptured]  # returns end game state
                return endState 





running = True # GUI loop
while running:
    screen.fill(colour3) # background colour (colour3)

    if state == "mainMenu":
        
        mainMenuTitle = Title('Multiplayer Chess', titleFont, colour1, screen_width // 2, 130) # displays title
        mainMenuTitle.display()

        # displays menu buttons on screen
        button1 = Button(colour5, screen_width//2, 300, 75, 700, 'Player vs Player', buttonFont, colour2)
        button1Rect = button1.draw()
        button2 = Button(colour5, screen_width//2, 400, 75, 700, 'LAN Player vs Player', buttonFont, colour2)
        button2Rect = button2.draw()
        button3 = Button(colour5, screen_width//2, 500, 75, 700, 'Chess Tutorial', buttonFont, colour2)
        button3Rect = button3.draw()
        button4 = Button(colour5, screen_width//2, 600, 75, 700, 'Settings', buttonFont, colour2)
        button4Rect = button4.draw()
        button5 = Button(colour5, 145, 710, 75, 200, 'Quit', buttonFont, colour2)
        button5Rect = button5.draw()

        
        
    elif state == "singleBoard":

        board = [[2, 1, 0, 0, 0, 0, -1, -2], # defines game variables
                [3, 1, 0, 0, 0 , 0, -1, -3],
                [4, 1, 0, 0, 0, 0, -1, -4],
                [5, 1, 0, 0, 0, 0, -1, -5],
                [6, 1, 0, 0, 0, 0, -1, -6],
                [4, 1, 0, 0, 0, 0, -1, -4],
                [3, 1, 0, 0, 0, 0, -1, -3],
                [2, 1, 0, 0, 0, 0, -1, -2]]
        
        turn = "white"
        capturedPiece = 0
        gameFinished = False
        whiteCaptured = []
        blackCaptured = []

        network = 0
        screen.fill(colour3)

        # displays GUI features on screen

        capturedPieces1SubtitleBox = Box(colour5, 65, 30, 240, 50, "Black Captured Pieces", colour2, smallFont)
        capturedPieces1SubtitleBox.draw()
        capturedPieces1SubtitleBox.textInsert()

        capturedPieces1Box = Box(colour5, 35, 100, 300, 200, 0, 0, 0)
        capturedPieces1Box.draw()

        capturedPieces2SubtitleBox = Box(colour5, 65, screen_height-320, 240, 50, "White Captured Pieces", colour2, smallFont)
        capturedPieces2SubtitleBox.draw()
        capturedPieces2SubtitleBox.textInsert()

        capturedPieces2Box = Box(colour5, 35, screen_height-250, 300, 200, 0, 0, 0)
        capturedPieces2Box.draw()

        moveLogBox = Box(colour5, 1075, 100, 280, 640, "", "", "")
        moveLogBox.draw()


        drawBoard()        
        updateBoard(board) # sets pieces to original position

        if gameFinished == False:
            endState = gameLoop(gameFinished, board, turn, network, state) # starts game loop
        gameFinished = True

        winner = endState[0]
        movelogList = endState[1]
        whiteCaptured = endState[2]
        blackCaptured = endState[3]

        displayGameUpdate("black", False, [0,0], False, False, True, winner) # displays final game state
        displayMovelog(movelogList)
        capturedPieces(whiteCaptured, blackCaptured)

        quitGameButton = Button(colour5, screen_width//2, 45, 50, 250, 'Return to Main Menu', smallFont, colour2)
        quitGameButtonRect = quitGameButton.draw()
        pygame.display.update()

        buttonClicked = False
        while buttonClicked == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    buttonClicked = True
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # detects left click on quit button
                    pos = pygame.mouse.get_pos()
                    if quitGameButtonRect.collidepoint(pos):
                        buttonClicked = True
                        state = "mainMenu"
                        board = [[2, 1, 0, 0, 0, 0, -1, -2], # resets game information for new game
                                [3, 1, 0, 0, 0 , 0, -1, -3],
                                [4, 1, 0, 0, 0, 0, -1, -4],
                                [5, 1, 0, 0, 0, 0, -1, -5],
                                [6, 1, 0, 0, 0, 0, -1, -6],
                                [4, 1, 0, 0, 0, 0, -1, -4],
                                [3, 1, 0, 0, 0, 0, -1, -3],
                                [2, 1, 0, 0, 0, 0, -1, -2]]
                        whiteCaptured = []
                        blackCaptured = []
                        movelogList = []
                        gameFinished = False


    elif state == "LANboard":

        board = [[2, 1, 0, 0, 0, 0, -1, -2], # defines game variables
                [3, 1, 0, 0, 0 , 0, -1, -3],
                [4, 1, 0, 0, 0, 0, -1, -4],
                [5, 1, 0, 0, 0, 0, -1, -5],
                [6, 1, 0, 0, 0, 0, -1, -6],
                [4, 1, 0, 0, 0, 0, -1, -4],
                [3, 1, 0, 0, 0, 0, -1, -3],
                [2, 1, 0, 0, 0, 0, -1, -2]]
        
        turn = "white"
        capturedPiece = 0
        gameFinished = False
        whiteCaptured = []
        blackCaptured = []

        # displays game GUI

        screen.fill(colour3)

        capturedPieces1SubtitleBox = Box(colour5, 65, 30, 240, 50, "Black Captured Pieces", colour2, smallFont)
        capturedPieces1SubtitleBox.draw()
        capturedPieces1SubtitleBox.textInsert()

        capturedPieces1Box = Box(colour5, 35, 100, 300, 200, 0, 0, 0)
        capturedPieces1Box.draw()

        capturedPieces2SubtitleBox = Box(colour5, 65, screen_height-320, 240, 50, "White Captured Pieces", colour2, smallFont)
        capturedPieces2SubtitleBox.draw()
        capturedPieces2SubtitleBox.textInsert()

        capturedPieces2Box = Box(colour5, 35, screen_height-250, 300, 200, 0, 0, 0)
        capturedPieces2Box.draw()

        drawBoard()

        moveLogBox = Box(colour5, 1075, 100, 280, 640, "", "", "")
        moveLogBox.draw()

        
        
        updateBoard(board) # sets pieces to original position
        

        pygame.display.update()

        if gameFinished == False:
            network = Network() # instantiates network class
            IPAddr = network.serverIP() # generates IP address

            inputBox = pygame.Rect(450, 30, 500, 30) 
            text = "Enter Game Code On Other Device: " + IPAddr
            pygame.draw.rect(screen, colour5, inputBox) # displays IP display box
            text_surface = smallFont.render(text, True, colour2) 
            screen.blit(text_surface, (inputBox.x+5, inputBox.y+5)) # displays IP address in box
            pygame.display.flip()



            network.serverConnect(IPAddr) # begins network connection, listening for client
            network.serverReceiveTest() # receives network test byte

            text = "Connection Made - Game Starting"
            pygame.draw.rect(screen, colour5, inputBox) # displays IP display box again
            text_surface = smallFont.render(text, True, colour2) 
            screen.blit(text_surface, (inputBox.x+5, inputBox.y+5)) # displays IP address in box

            endState = gameLoop(gameFinished, board, turn, network, state) # begins game loop

        winner = endState[0]
        movelogList = endState[1]
        whiteCaptured = endState[2]
        blackCaptured = endState[3]

        displayGameUpdate("black", False, [0,0], False, False, True, winner) # displays winner message
        displayMovelog(movelogList) # displays final move log
        capturedPieces(whiteCaptured, blackCaptured) # displays final captured pieces

        quitGameButton = Button(colour5, screen_width//2, 40, 50, 250, 'Return to Main Menu', smallFont, colour2) # displays quit button to exit to main menu
        quitGameButtonRect = quitGameButton.draw()
        pygame.display.update()

        buttonClicked = False
        while buttonClicked == False:
            for event in pygame.event.get(): # user input detection loop
                if event.type == pygame.QUIT:
                    buttonClicked = True
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos() # detects left mouse click position
                    if quitGameButtonRect.collidepoint(pos): # determines if mouse click on quit button position
                        buttonClicked = True
                        state = "mainMenu"
                        board = [[2, 1, 0, 0, 0, 0, -1, -2], # sets board, captured pieces and move log to original states to reset game
                                [3, 1, 0, 0, 0 , 0, -1, -3],
                                [4, 1, 0, 0, 0, 0, -1, -4],
                                [5, 1, 0, 0, 0, 0, -1, -5],
                                [6, 1, 0, 0, 0, 0, -1, -6],
                                [4, 1, 0, 0, 0, 0, -1, -4],
                                [3, 1, 0, 0, 0, 0, -1, -3],
                                [2, 1, 0, 0, 0, 0, -1, -2]]
                        whiteCaptured = []
                        blackCaptured = []
                        movelogList = []
                        gameFinished = False # to ensure game loop can restart
                





    elif state == "tutorial":
        screen.fill(colour3) # sets background colour

        tutorialMenuTitle = Title('Tutorial', titleFont, colour1, screen_width//2, 130)
        tutorialMenuTitle.display() # displays tutorial title

        pieceMovementsButton = Button(colour5, screen_width//2 - 300, 400, 200, 500, 'Piece Movements', buttonFont, colour2)
        pieceMovementsButtonRect = pieceMovementsButton.draw() # displays piece movements button

        chessRulesButton = Button(colour5, screen_width//2 + 300, 400, 200, 500, 'Basic Rules', buttonFont, colour2)
        chessRulesButtonRect = chessRulesButton.draw() # displays basic rules button

        returnToMenuButton = Button(colour5, screen_width//2 - 500, 710, 65, 320, 'Return to Menu', buttonFont, colour2)
        returnToMenuButtonRect = returnToMenuButton.draw() # displays quit button

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # detects user inputs
                pos = pygame.mouse.get_pos()
                if pieceMovementsButtonRect.collidepoint(pos): # detects if piece movements button selected
                    state = "pieceMovementsTutorial"
                    
                elif chessRulesButtonRect.collidepoint(pos): # detects if rules button selected
                    state = "chessRulesTutorial"

                elif returnToMenuButtonRect.collidepoint(pos): # detects if return to menu button selected
                    state = "mainMenu"

    elif state == "pieceMovementsTutorial":
        screen.fill(colour3)

        pieceMovementsTitle = Title('Piece Movements', titleFont, colour1, screen_width//2, 130)
        pieceMovementsTitle.display() # displays title

        # display of piece icons on screen
        img = pygame.image.load(loadImage("white pawn.png"))
        imgRect = img.get_rect(center = (200, 250))
        screen.blit(img, imgRect)

        img = pygame.image.load(loadImage("white knight.png"))
        imgRect = img.get_rect(center = (200, 315))
        screen.blit(img, imgRect)

        img = pygame.image.load(loadImage("white bishop.png"))
        imgRect = img.get_rect(center = (200, 380))
        screen.blit(img, imgRect)

    
        img = pygame.image.load(loadImage("white rook.png"))
        imgRect = img.get_rect(center = (200, 445))
        screen.blit(img, imgRect)

        img = pygame.image.load(loadImage("white queen.png"))
        imgRect = img.get_rect(center = (200, 510))
        screen.blit(img, imgRect)

        img = pygame.image.load(loadImage("white king.png"))
        imgRect = img.get_rect(center = (200, 575))
        screen.blit(img, imgRect)

        # display of text outlining piece movements
        
        pawnText = smallFont.render("Pawns can only move in the forwards direction and cannot jump over pieces. One square normally, two squares on", True, colour1)
        pawnTextRect = pawnText.get_rect(midleft = (230, 240))
        screen.blit(pawnText, pawnTextRect)

        pawnText2 = smallFont.render("their first move. Pawns can only capture if there is an opponent's piece in one of the forward diagonal squares.", True, colour1)
        pawnText2Rect = pawnText2.get_rect(midleft = (230, 260))
        screen.blit(pawnText2, pawnText2Rect)

        knightText = smallFont.render("Knights move in an L-shape. One square vertically, two squares horizontally or two squares vertically, one square", True, colour1)
        knightTextRect = knightText.get_rect(midleft = (230, 305))
        screen.blit(knightText, knightTextRect)

        knightText2 = smallFont.render("horizontally. Knights are the only piece that can jump over other pieces.", True, colour1)
        knightText2Rect = knightText2.get_rect(midleft = (230, 325))
        screen.blit(knightText2, knightText2Rect)

        bishopText = smallFont.render("Bishops move an unlimited number of squares diagonally. They cannot jump over pieces", True, colour1)
        bishopTextRect = bishopText.get_rect(midleft = (230, 380))
        screen.blit(bishopText, bishopTextRect)

        rookText = smallFont.render("Rooks move an unlimited number of squares in the horizontally or vertically. They cannot jump over pieces", True, colour1)
        rookTextRect = rookText.get_rect(midleft = (230, 445))
        screen.blit(rookText, rookTextRect)

        queenText = smallFont.render("The queen moves an unlimited number of squares in the horizontally, vertically or diagonally. They cannot", True, colour1)
        queenTextRect = queenText.get_rect(midleft = (230, 500))
        screen.blit(queenText, queenTextRect)

        queenText2 = smallFont.render("jump over pieces", True, colour1)
        queenText2Rect = queenText2.get_rect(midleft = (230, 520))
        screen.blit(queenText2, queenText2Rect)

        kingText = smallFont.render("The king moves one square horizontally, vertically or diagonally.", True, colour1)
        kingTextRect = kingText.get_rect(midleft = (230, 575))
        screen.blit(kingText, kingTextRect)

        returnToMenuButton = Button(colour5, screen_width//2 - 400, 710, 65, 480, 'Return to Tutorial Menu', buttonFont, colour2)
        returnToMenuButtonRect = returnToMenuButton.draw() # displays return to tutorial menu button

    elif state == "chessRulesTutorial":
        screen.fill(colour3) # set background colour

        chessRulesTitle = Title('Chess Rules', titleFont, colour1, screen_width//2, 130)
        chessRulesTitle.display() # display title

        # code below displays text outlining chess rules

        line1Text = smallFont.render("Chess is played on an 8x8 board. White moves first, followed by Black; then moves alternate.", True, colour1)
        line1TextRect = line1Text.get_rect(midleft = (200, 250))
        screen.blit(line1Text, line1TextRect)

        line2Text = smallFont.render("The objective of the game is to checkmate the opponent's king.", True, colour1)
        line2TextRect = line2Text.get_rect(midleft = (200, 270))
        screen.blit(line2Text, line2TextRect)

        checkmateSubheading = smallFont.render("Check and Checkmate:", True, colour1)
        checkmateSubheadingRect = checkmateSubheading.get_rect(midleft = (200, 310))
        screen.blit(checkmateSubheading, checkmateSubheadingRect)

        line3Text = smallFont.render("When a player's king is under attack by one of the opponent's pieces, the player is in 'check'.", True, colour1)
        line3TextRect = line3Text.get_rect(midleft = (200, 340))
        screen.blit(line3Text, line3TextRect)

        line4Text = smallFont.render("If in check, the player must always move out of check. This is achieved by either capturing the", True, colour1)
        line4TextRect = line4Text.get_rect(midleft = (200, 360))
        screen.blit(line4Text, line4TextRect)

        line5Text = smallFont.render("attacking piece or moving a piece to protect the king.", True, colour1)
        line5TextRect = line4Text.get_rect(midleft = (200, 380))
        screen.blit(line5Text, line5TextRect)

        line6Text = smallFont.render("If the player is in check and cannot move out of the check position, then they are in checkmate.", True, colour1)
        line6TextRect = line6Text.get_rect(midleft = (200, 400))
        screen.blit(line6Text, line6TextRect)

        winnerSubheading = smallFont.render("Winning:", True, colour1)
        winnerSubheadingRect = winnerSubheading.get_rect(midleft = (200, 440))
        screen.blit(winnerSubheading, winnerSubheadingRect)

        line7Text = smallFont.render("The winner is the player who checkmates the opponent's king.", True, colour1)
        line7TextRect = line7Text.get_rect(midleft = (200, 470))
        screen.blit(line7Text, line7TextRect)

        line8Text = smallFont.render("If both players are in checkmate, then a 'stalemate' has occured. This is a draw.", True, colour1)
        line8TextRect = line8Text.get_rect(midleft = (200, 490))
        screen.blit(line8Text, line8TextRect)

        specialMovesSubheading = smallFont.render("Special Moves:", True, colour1)
        specialMovesSubheadingRect = specialMovesSubheading.get_rect(midleft = (200, 520))
        screen.blit(specialMovesSubheading, specialMovesSubheadingRect)

        line9Text = smallFont.render("Castling - This is when the king moves two squares left or right, whilst the rook on that side moves", True, colour1)
        line9TextRect = line9Text.get_rect(midleft = (200, 550))
        screen.blit(line9Text, line9TextRect)

        line10Text = smallFont.render("to the opposite side of the king. This is only possible when the king and rook haven't moved.", True, colour1)
        line10TextRect = line10Text.get_rect(midleft = (302, 570))
        screen.blit(line10Text, line10TextRect)

        line11Text = smallFont.render("The king may not castle out of, through or into check.", True, colour1)
        line11TextRect = line11Text.get_rect(midleft = (302, 590))
        screen.blit(line11Text, line11TextRect)

        line12Text = smallFont.render("Promotion - This is when a pawn reaches the end of the board and must be exchanged for either a knight,", True, colour1)
        line12TextRect = line12Text.get_rect(midleft = (200, 610))
        screen.blit(line12Text, line12TextRect)

        line13Text = smallFont.render("bishop, rook or queen.", True, colour1)
        line13TextRect = line13Text.get_rect(midleft = (320, 630))
        screen.blit(line13Text, line13TextRect)

        returnToMenuButton = Button(colour5, screen_width//2 - 400, 710, 65, 480, 'Return to Tutorial Menu', buttonFont, colour2)
        returnToMenuButtonRect = returnToMenuButton.draw() # displays return to tutorial button
    
        
    elif state == "settings":

        # menu page title
        settingsMenuTitle = Title('Settings', titleFont, colour1, screen_width // 2, 130)
        settingsMenuTitle.display()

        # colour settings subtitle
        colourSettingsSubTitle = Title('Colour Settings', buttonFont, colour1, screen_width//2 - 360, 250)
        colourSettingsSubTitle.display()

        # colour settings buttons
        defaultColourButton = Button(colour5, screen_width//2 - 300, 325, 65, 450, 'Default (Light Mode)', buttonFont, colour2)
        defaultColourButtonRect = defaultColourButton.draw()

        darkColourButton = Button(colour5, screen_width//2 + 300, 325, 65, 450, 'Dark Mode', buttonFont, colour2)
        darkColourButtonRect = darkColourButton.draw()

        # display moves subtitle

        displayMovesSubtitle = Title('Display Possible Moves?', buttonFont, colour1, screen_width//2 - 275, 470)
        displayMovesSubtitle.display()

        # display moves buttons

        yesDisplayMovesButton = Button(colour5, screen_width//2 - 300, 550, 65, 450, 'Yes', buttonFont, colour2)
        yesDisplayMovesButtonRect = yesDisplayMovesButton.draw()

        noDisplayMovesButton = Button(colour5, screen_width//2 + 300, 550, 65, 450, 'No', buttonFont, colour2)
        noDisplayMovesButtonRect = noDisplayMovesButton.draw()

        # return to menu button

        returnToMenuButton = Button(colour5, screen_width//2 - 500, 710, 65, 320, 'Return to Menu', buttonFont, colour2)
        returnToMenuButtonRect = returnToMenuButton.draw()





    for event in pygame.event.get(): # scans and handles events in game loop
        if event.type == pygame.QUIT:
            running = False
        elif state == "mainMenu" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # main menu button selection loop
            pos = pygame.mouse.get_pos()
            if button1Rect.collidepoint(pos): # local game option
                state = "singleBoard"
            elif button2Rect.collidepoint(pos): # LAN game option
                state = "LANboard"
            elif button3Rect.collidepoint(pos): # chess tutorial option
                state = "tutorial"
            elif button4Rect.collidepoint(pos): # settings option
                state = "settings"
            elif button5Rect.collidepoint(pos): # quit game option
                running = False

        elif state == "tutorial" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if returnToMenuButtonRect.collidepoint(pos): # return to main menu button
                state = "mainMenu"

        elif state == "chessRulesTutorial" or state == "pieceMovementsTutorial" or state == "openingsTutorial":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if returnToMenuButtonRect.collidepoint(pos): # return to tutorial menu button
                    state = "tutorial"
        
        elif state == "settings" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if defaultColourButtonRect.collidepoint(pos): # light mode
                
                colour1 = (0,0,0) # black
                colour2 = (255, 255, 255) # white
                colour3 = (150, 220, 248) # teal
                colour4 = (179, 0, 0) # red
                colour5 = (21, 96, 130) # turquoise
                colour6 = (82, 148, 212) # blue


            elif darkColourButtonRect.collidepoint(pos): # dark mode

                colour1 = (0,0,0) # black
                colour2 = (188,204,220) # light grey
                colour3 = (72,101,129) # blue-grey
                colour4 = (179, 0, 0) # red
                colour5 = (16,42,67) # dark blue
                colour6 = (130,154,177) # darker grey

            elif yesDisplayMovesButtonRect.collidepoint(pos):
                displayMoves = True # set display possible moves to true
            elif noDisplayMovesButtonRect.collidepoint(pos):
                displayMoves = False # set display possible moves to false

            elif returnToMenuButtonRect.collidepoint(pos):
                state = "mainMenu" # return to main menu

        elif state == "singleBoard" and gameFinished == True and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

            if quitGameButtonRect.collidepoint(pos): # return to main menu button
                state = "mainMenu"


    pygame.display.flip() # updates screen with contents
    pygame.display.update()

pygame.quit() # exits pygame at end of game loop