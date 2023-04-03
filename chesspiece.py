import pygame

#CLASSES
class Piece:
    """Piece is a super class of the chess pieces, x and y are the current board coordinates while colour is either black or white, (defined by an integer, 0 or 1)"""
    
    board = [[0 for i in range(8)] for j in range(8)]
    
    def __init__(self,x,y,col):
        self.x = 220 + x * 120
        self.y = 180 + y * 120

        Piece.board[self.x][self.y] = self
        self.col = col

    def getCoords(self):
        #Will return the pixel position of the Piece
        return (self.x,self.y)
    
    def setCoords(self, x, y):
        #Update the pixel position of the Piece
        self.x = 160+ x *180
        self.y = 160+ y *180

    def getBoardCoords(self):
        #Will return the board position of the Piece
        return (self.x/180-160,self.y/180-160)
    
    def possibleMoves(self):
        return
    
    def draw(self,screen,colour):
        pygame.draw.circle(screen,colour,(self.getCoords()),50)
    
    def collision(self, other)->bool:
        if not other.isinstance(Piece):
            raise TypeError("Other is not a Piece")
        
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def getTeam(self):
        return self.col


class Pawn(Piece):
    def possibleMoves(self):
        possMove

        for i in range(2):
            if not self.collision:
                possMove += [0,i]
            #else: if 


        if self.getTeam(): #if on white team
            if self.y == 2: #if its on the starting position
                return [[0,1],[0,2]]
            return [[0,1]]
        else:
            if self.y == 7: #if its on the starting position
                return [[0,-1],[0,-2]]
            return [[0,-1]]
    
        




if __name__ == '__main__':
    print("Im doing something in TestFile")

