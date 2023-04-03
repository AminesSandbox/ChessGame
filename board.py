import pygame
from chesspiece import Pawn

#CONSTANTS
CHESSGREEN = [155,205,155]
CHESSWHITE = [238,232,205]
CHESSBROWN = [139,115,85]
CHESSGRAY = [128,128,128]
CHESSCYAN = [0,238,238]
BLACK = [0,0,0]

#DRAWING METHODS
def drawSquare (c,x,y,w,o):
    pygame.draw.rect(screen,c,(x,y,w,w),o)

def drawCirc (colour,x,y,r):
    pygame.draw.circle(screen,colour,(x,y),r)

def drawBoard(): 
    for i in range(8):
        for j in range(8):
            if (j%2 == 0 and i%2 == 0):
                drawSquare(CHESSGREEN, 160+i*120,j*120, 120,0)
            elif (j%2 == 1 and i%2 == 1):
                drawSquare(CHESSGREEN, 160+i*120,j*120, 120,0)
            else:
                drawSquare(CHESSWHITE, 160+i*120,j*120, 120,0)

            drawSquare(CHESSBROWN, 160+i*120,j*120, 120,1) #Draw rectangle borders           
    
    drawSquare(BLACK, 160,0, 959,5) #Draw External Border

#MAIN SCRIPT
pygame.init() # initialize game

screen = pygame.display.set_mode((1280, 960)) #setting length and width
clock = pygame.time.Clock()
running = True

rows, cols = (5, 5)
boardMatrix = [[0] * cols] * rows

pawn1 = Pawn(00,00,CHESSCYAN)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    
    screen.fill(CHESSBROWN)
    drawBoard()

    # RENDER YOUR GAME HERE
    drawCirc(CHESSCYAN,pawn1.getCoords()[0],pawn1.getCoords()[1],10)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60


pygame.quit()


