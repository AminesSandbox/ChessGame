import pygame

#CLASSES
class Piece:
    """Piece is a super class of the chess pieces, x and y are the current board coordinates while colour is either black or white, (defined by an integer, 0 or 1)"""
    
    board = [[None for i in range(8)] for j in range(8)] #coords go from 0,0 (top left) to 7,7 (bottom right) [y,x]
    
    def __init__(self,x,y,col):
        self.x = x
        self.y = y

        Piece.board[y][x] = self # must do -1 bc indices must be from 0 to 7
        self.col = col

    def getCoords(self):
        """Will return the pixel position of the Piece"""
        return (220 + self.x * 120, 180 + self.y * 120)
    
    def setCoords(self, x, y):
        """Update the board position of the Piece"""
        self.x = x
        self.y = y

    def getBoardCoords(self):
        """Will return the board position of the Piece"""
        return (self.x, self.y)
    
    def possibleMoves(self):
        return
    
    def draw(self,screen,colour):
        pygame.draw.circle(screen,colour,(self.getCoords()),50)
    
    def collision(self, increment)->bool:
        """Checks if there will be a collision with a piece when hcecking a tentative move"""
        if Piece.board[self.y + increment[1]][self.x + increment[0]] != None:
            return True
        else:
            return False

    def getTeam(self):
        """Returns current Piece's team colour"""
        return self.col


class Pawn(Piece):
    def possibleMoves(self):
        possMove = list()
        movementincrement = 1 #Pawn can only move one square upwards on all moves but the first
        if self.y == 1 or self.y == 6:
            movementincrement = 2

        print(movementincrement)
        if self.getTeam():
            for i in range(1,movementincrement+1):
                print(self.collision([0,i]))
                print(i)
                if self.collision([0,i]):
                    print()
                    if Piece.board[self.y+i][self.x].getTeam() != self.getTeam():
                        possMove.append([0,i])
                    return possMove
                else:
                    possMove.append([0,i])
        else:
            for i in range(1,movementincrement):
                if self.collision([0,-i]):
                    if Piece.board[self.y-i][self.x].getTeam() != self.getTeam():
                        possMove.append([0,-i])
                    return possMove
                else:
                    possMove.append([0,-i])
        
        return possMove
        


if __name__ == '__main__':
    print("Im doing something in TestFile")
    b1 = Pawn(7,1,1)
    b2 = Pawn(7,3,1)
    for row in Piece.board:
        print(row)
    
    print(b1.possibleMoves())

