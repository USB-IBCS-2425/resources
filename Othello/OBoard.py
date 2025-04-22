from Button import*
from Cell import*

class OBoard():

    def __init__(self, win):
        self.cells = []
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    color = "white"
                else:
                    color = "grey"
                self.cells.append(Cell(win, (j, i), color))

        self.potentMoves = []
        self.whoMove = "black"

    def setWhoMove(self, pl):
        self.whoMove = pl

    def getPotentMoves(self):
        return self.potentMoves

    def getAllCells(self):
        return self.cells

    def findBestMove(self, moves):

        move = moves[0]
        
        return move

    def checkMoves(self):
        moves = []
        UL = [-1, -8]
        U = [0, -8]
        UR = [1, -8]
        L = [-1, 0]
        R = [1, 0]
        DL = [-1, 8]
        D = [0, 8]
        DR = [1, 8]
        directions = [UL, U, UR, L, R, DL, D, DR]
        for i in range(64):
            cell = self.cells[i]
            if cell.piece != "":
                if self.whoMove != cell.piece:
                    for d in directions:
                        if (i%8 != 0) or (d[0] == 0):
                            if (i%8 != 7) or (d[0] == 0):
                                newInd = i + d[0] + d[1]

                                if 0 <= newInd < 64:
                                    if self.cells[newInd].piece == "":
                                        
                                        checkForValid = False
                                        pos = i
                                        for j in range(6):
                                            
                                            pos = pos - d[0] - d[1]
                                            
                                            
                                            if (63 < pos):
                                                break
                                            elif (pos < 0):
                                                break
                                            elif self.cells[pos].piece == "":
                                                break
                                            elif self.cells[pos].piece == self.whoMove:
                                                checkForValid = True
                                                
                                                break
                                            elif (pos%8 == 0) and (d[0] != 0):
                                                break
                                            elif (pos%8 == 7) and (d[1] != 0):
                                                break
                                        if checkForValid:
                                            moves.append(self.cells[newInd])
        for m in moves:
            m.highlight()

        return moves

    def place(self, c):
        c.updatePiece(self.whoMove)
        toFlip = []
        ind = self.cells.index(c)
        UL = [-1, -8]
        U = [0, -8]
        UR = [1, -8]
        L = [-1, 0]
        R = [1, 0]
        DL = [-1, 8]
        D = [0, 8]
        DR = [1, 8]
        directions = [UL, U, UR, L, R, DL, D, DR]
        for d in directions:
            newInd = ind + d[0] + d[1]
            tempFlip = []
            for i in range(7):
                if (newInd%8 == 7) and (d[0] == -1):
                    break
                if (newInd%8 == 0) and (d[0] == 1):
                    break
                if 0 <= newInd < 64:
                    if (self.cells[newInd].piece != self.whoMove) and (self.cells[newInd].piece != ""):
                        tempFlip.append(newInd)
                    elif (self.cells[newInd].piece == self.whoMove):
                        for t in tempFlip:
                            toFlip.append(t)
                        break
                    else:
                        break
                    newInd = newInd + d[0] + d[1]

        if self.whoMove == "black":
            change = "white"
        else:
            change = "black"
        for f in toFlip:
            #print(f)
            self.cells[f].updatePiece(self.whoMove)
        self.whoMove = change
        
            
        
            
            


