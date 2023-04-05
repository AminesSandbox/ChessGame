import pygame
import chesspiece

# CONSTANTS
CHESSGREEN = (155, 205, 155)
CHESSWHITE = (238, 232, 205)
CHESSBROWN = (139, 115, 85)
CHESSGRAY = (128, 128, 128)
CHESSCYAN = (0, 238, 238)
BLACK = (0, 0, 0)
YELLOW = (238, 230, 133)

screenLength = 1280
screenHeight = 960

# METHODS
def drawSquare(c, x, y, w, o):
    pygame.draw.rect(screen, c, (x, y, w, w), o)

def drawCircle(colour, x, y, r):
    pygame.draw.circle(screen, colour, (x, y), r)

def board ():
    mouse = pygame.mouse.get_pos()

    for i in range (160,1120,120):
        for j in range (0,961,120):
            if (i // 120) % 2 == (j // 120) % 2:
                drawSquare(CHESSGREEN, i, j , 120, 0)
            else:
                drawSquare(CHESSWHITE, i, j , 120, 0)

            drawSquare(CHESSBROWN,  i , j , 120, 1)  # Draw rectangle borders


def interact ():
    global yellowCoord
    mouse = pygame.mouse.get_pos()

    if  160 < mouse[0] < 1120 and event.type == pygame.MOUSEBUTTONUP:
        xCoord = (mouse[0] - 160 - 1) // 120 # subtracting 1 for border width
        yCoord = (mouse[1] - 1) // 120 # subtracting 1 for border width

        if (xCoord, yCoord) != yellowCoord:
            board() 
            yellowCoord = (xCoord, yCoord)
        
        drawSquare(YELLOW,xCoord * 120 + 160 , yCoord * 120 , 119, 0)
    else:
        board()

    drawSquare(BLACK, 160, 0, 959, 5)  # Draw External Border


# MAIN SCRIPT
pygame.init()  # initialize game

screen = pygame.display.set_mode((screenLength, screenHeight))  # setting length and width
clock = pygame.time.Clock()
running = True

screen.fill(CHESSBROWN)

board()
yellowCoord = None
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    mouse = pygame.mouse.get_pos()  # gets coord of the mouse

    click = pygame.mouse.get_pressed()  # click [0] would be = 1 if mouse is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            interact()


    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
