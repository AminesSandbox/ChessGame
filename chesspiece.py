import pygame

#CLASSES
class Piece:
    def __init__(self,x,y, col):
        self.x = 240+ x *180
        self.y = 60+ y *120
        self.col = col

    def getCoords(self):
        #Will return the pixel position of the Piece
        return (self.x,self.y)
    
    def setCoords(self, x, y):
        #Update the pixel position of the Piece
        self.x = 160+ x *180
        self.y = 160+ y *180

    def getBoardCoords(self):
        #Will return the pixel position of the Piece
        return (self.x/180-160,self.y/180-160)
    
    def drawCirc (self,screen,colour,r):
        pygame.draw.circle(screen,colour,(self.x,self.y),r)
        


if __name__ == '__main__':
    print("Im doing something in TestFile")

