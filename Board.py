import pygame

#CONSTANTS
CHESSGREEN = [155,205,155]
CHESSWHITE = [238,232,205]
CHESSBROWN = [139,115,85]
CHESSGRAY = [128,128,128]
CHESSCYAN = [0,238,238]
BLACK = [0,0,0]

#CLASSES
class Pawn:
    def __init__(self,x,y, col):
        self.x = 160+ x *180
        self.y = 160+ y *180
        self.col = col

    def draw(self):
        colour(self.col,self.x,self.y,50)
    

#METHODS
def drawSquare (c,x,y,w,o):
    pygame.draw.rect(screen,c,(x,y,w,w),o)

def colour (colour,x,y,r):
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
a = Pawn(0,0,CHESSCYAN)

screen = pygame.display.set_mode((1280, 960)) #setting length and width
clock = pygame.time.Clock()
running = True

rows, cols = (5, 5)
boardMatrix = [[0] * cols] * rows

screen.fill(CHESSBROWN)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    
    # RENDER YOUR GAME HERE
    drawBoard()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60


pygame.quit()


