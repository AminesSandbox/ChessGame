import pygame

#CONSTANTS
BOARD_SIZE = 8

#CLASSES
class Piece:
    """Piece is a super class of the chess pieces, x and y are the current board coordinates while colour is either black or white, (defined by an integer, 0 or 1)"""
    
    board = [[None for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)] #coords go from 0,0 (top left) to 7,7 (bottom right) [y,x]
    lastMove = [None,None] #The games's last move this is used to check en-passant (Can be updated in future if want to play/rewind games in sequential order -> Stack)
    
    def __init__(self,x,y,col):
        self.x = x
        self.y = y

        self.prevLoc = [None,None]

        Piece.board[y][x] = self # must do -1 bc indices must be from 0 to 7
        self.col = col

        self.possMove = list() #current possible moves for the piece

    def __str__(self) -> str:
        if self.getTeam():
            return "White Piece"
        else:
            return "Black Piece"
    
    __repr__ = __str__ 

    def getCoords(self):
        """Will return the pixel position of the Piece"""
        return (220 + self.x * 120, 180 + self.y * 120)
    
    def setCoords(self, x, y):
        """Update the board position of the Piece from (0,0) to (7,7)"""
        prevLoc = [self.x,self.y]

        Piece.board[self.y][self.x] = None
        Piece.board[y][x] = self

        self.x = x
        self.y = y

    def movePiece(self, vec)->bool:
        """Moves selected piece by the given vector, returns boolean if succesful"""

        if vec not in self.possMove:
            return False

        Piece.board[self.y+ vec[1]][self.x+vec[0]] = self
        Piece.board[self.y][self.x] = None
    
        self.x += vec[0]
        self.y += vec[1]

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
    
    def prevMove(self):
        """Sends game's last Move"""
        return Piece.lastMove
    
    def death(self):
        """Removes a piece from the game"""
        Piece.board[self.y][self.x] = None


class Pawn(Piece):

    def __init__(self, x, y, col):
        super().__init__(x, y, col)

    def __str__(self) -> str:
        if self.getTeam():
            return "White Pawn"
        else:
            return "Black Pawn"
    
    __repr__ = __str__ 

    def possibleMoves(self)->list:
        """Returns a list of all possible moves a Pawn (white or black) can make"""

        movementincrement = 1 #Pawn can only move one square upwards on all moves but the first
        if self.y == 1 or self.y == BOARD_SIZE-2:
            movementincrement = 2

        if self.getTeam():
            for i in range(1,movementincrement+1): #First Pawn Move  
                if 0 <= self.y + i < BOARD_SIZE:
                    if not self.collision([0,i]):
                        self.possMove.append([0,i])
            
            if 0 <= self.y + 1 < BOARD_SIZE and 0 <= self.x + 1 < BOARD_SIZE and Piece.board[self.y+1][self.x+1].getTeam() != self.getTeam(): #for diagonal eating
                    self.possMove.append([1,1])
        else:
            for i in range(1,movementincrement+1): #First Pawn Move  
                if 0 <= self.y + i < BOARD_SIZE:
                    if not self.collision([0,-i]):
                        self.possMove.append([0,-i])
            
            if 0 <= self.y - 1 < BOARD_SIZE and 0 <= self.x - 1 < BOARD_SIZE and Piece.board[self.y-1][self.x-1].getTeam() != self.getTeam(): #for diagonal eating
                    self.possMove.append([-1,-1])
            
            if Piece.board[self.y][self.x+1]!= None and Piece.board[self.y][self.x+1].isinstance(Pawn): #En-Passant
                if Piece.board[self.y][self.x+1].getTeam() != 1 and Piece.board[self.y][self.x+1].prevMove == [0,2]:
                    self.possMove.append([-1,-1])

        return self.possMove
    


if __name__ == '__main__':
    print("Im doing something in TestFile")
    pList = list()
#    for i in range(8):
 #       pList.append(Pawn(i,7,1)) # 8 white pawns
  #  for i in range(8):
   #     pList.append(Pawn(i,1,0)) # 8 black pawns
    pList.append(Pawn(1,7,0)) # 8 white pawns
    pList.append(Pawn(0,6,1)) # 8 white pawns

    for row in Piece.board:
        print(row)
        
    pList[0].setCoords(0,0)
    print("")

    for row in Piece.board:
        print(row)
    
    print(pList[0].possibleMoves())

