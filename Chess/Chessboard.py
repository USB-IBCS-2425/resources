from Button import*
from Cell import*

class Chessboard():

    def __init__(self, win):
        self.cells = []
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    color = "white"
                else:
                    color = "grey"
                self.cells.append(Cell(win, (j, i), color))

        self.currentPiece = None
        self.potentMoves = []
        self.castleB = True
        self.move = False
        self.whoMove = "white"
        self.check = False

    def setWhoMove(self, pl):
        self.whoMove = pl
        self.move = False

    def getPotentMoves(self):
        return self.potentMoves

    def getAllCells(self):
        return self.cells

    def selectCell(self, p):
        self.move = False

        for c in self.cells:
            if c.isClicked(p):
                if c in self.potentMoves:
                    self.move = True
                    if self.currentPiece.pieceColor == "white":
                        self.whoMove = "black"
                    else:
                        self.whoMove = "white"
                    c.unHMove()
                    self.potentMoves.remove(c)
                    c.updatePiece(self.currentPiece.piece)
                    if c.getCoord()[1] == 7:
                        if self.currentPiece.piece == "pawn":
                            c.updatePiece("queen")
                    if c.getCoord()[1] == 0:
                        if self.currentPiece.piece == "pawnW":
                            c.updatePiece("queenW")
                    self.currentPiece.empty()
                elif c.highlighted:
                    c.unHighlight()
                    self.currentPiece = None
                elif c.pieceColor == self.whoMove:
                    c.highlight()
                    self.currentPiece = c
                else:
                    c.highlight()
        for cel in self.cells:
            if not cel == self.currentPiece:
                if cel.highlighted:
                    cel.unHighlight()
        for m in self.potentMoves:
            m.unHMove()
        self.potentMoves.clear()

    def checkCheck(self):
        checkMoves = []
        for mov in self.potentMoves:
            checkF = False
            for piece in ["pawn", "bishop", "rook", "knight", "queen", "king"]:
                if checkF:
                    break
                color = self.currentPiece.pieceColor
                #pawn
                if piece == "pawn":
                    if color == "black":
                        forward = 1
                    else:
                        forward = -1
                        
                    curCoord = mov.coord
                    forCoord = (curCoord[0], curCoord[1] + forward)
                    
                    capCoord = (forCoord[0]+1, forCoord[1])
                    capCoord2 = (forCoord[0]-1, forCoord[1])
                    capInd = capCoord[0] + capCoord[1]*8
                    capInd2 = capCoord2[0] + capCoord2[1]*8
                    if color == "black":
                        if self.cells[capInd].piece == "pawnW" or self.cells[capInd2].piece == "pawnW":
                            checkMoves.append(mov)
                            mov.unHMove()
                            checkF = True
                            break       
                    if color == "white":
                        if self.cells[capInd].piece == "pawn" or self.cells[capInd2].piece == "pawn":
                            checkMoves.append(mov)
                            mov.unHMove()
                            checkF = True
                            break
                #knight
                if piece == "knight":
                    captures = []
                    curCoord = mov.coord
                    captures.append((curCoord[0]+1,curCoord[1]-2))
                    captures.append((curCoord[0]+1,curCoord[1]+2))
                    captures.append((curCoord[0]-1,curCoord[1]-2))
                    captures.append((curCoord[0]-1,curCoord[1]+2))
                    captures.append((curCoord[0]+2,curCoord[1]-1))
                    captures.append((curCoord[0]+2,curCoord[1]+1))
                    captures.append((curCoord[0]-2,curCoord[1]-1))
                    captures.append((curCoord[0]-2,curCoord[1]+1))
                    for c in captures:
                        if checkF:
                            break
                        if c[0] >= 0:
                            if c[0] < 8:
                               if c[1] >= 0:
                                   if c[1] < 8:
                                       ind = c[0] + c[1]*8
                                       destCell = self.cells[ind]
                                       if color == "black":
                                           if destCell.piece == "knightW":
                                               checkMoves.append(mov)
                                               mov.unHMove()
                                               checkF = True
                                               break
                                       else:
                                           if destCell.piece == "knight":
                                               checkMoves.append(mov)
                                               mov.unHMove()
                                               checkF = True
                                               break
                #rook
                if piece == "rook" or piece == "queen":
                    curCoord = mov.coord
                    #up
                    for i in range(7):
                        if curCoord[1] + i + 1 > 7:
                            break
                        destCoord = (curCoord[0], curCoord[1] + i + 1)
                        destInd = destCoord[0] + destCoord[1]*8
                        destCell = self.cells[destInd]
                        if not destCell.piece == "":
                            if destCell.pieceColor != color:
                                if destCell.piece == "queen" or destCell.piece == "queenW" or destCell.piece == "rook" or destCell.piece == "rookW":
                                    checkMoves.append(mov)
                                    mov.unHMove()
                                    checkF = True
                                    break
                                break
                            else:
                                break
                    #down
                    for i in range(7):
                        if curCoord[1] - i - 1 < 0:
                            break
                        destCoord = (curCoord[0], curCoord[1] - i - 1)
                        destInd = destCoord[0] + destCoord[1]*8
                        destCell = self.cells[destInd]
                        if not destCell.piece == "":
                            if destCell.pieceColor != color:
                                if destCell.piece == "queen" or destCell.piece == "queenW" or destCell.piece == "rook" or destCell.piece == "rookW":
                                    checkMoves.append(mov)
                                    mov.unHMove()
                                    checkF = True
                                    break
                                break
                            else:
                                break
                    #right
                    for i in range(7):
                        if curCoord[0] + i + 1 > 7:
                            break
                        destCoord = (curCoord[0] + i + 1, curCoord[1])
                        destInd = destCoord[0] + destCoord[1]*8
                        destCell = self.cells[destInd]
                        if not destCell.piece == "":
                            if destCell.pieceColor != color:
                                if destCell.piece == "queen" or destCell.piece == "queenW" or destCell.piece == "rook" or destCell.piece == "rookW":
                                    checkMoves.append(mov)
                                    mov.unHMove()
                                    checkF = True
                                    break
                                break
                            else:
                                break
                    #left
                    for i in range(7):
                        if curCoord[0] - i - 1 < 0:
                            break
                        destCoord = (curCoord[0] - i - 1, curCoord[1])
                        destInd = destCoord[0] + destCoord[1]*8
                        destCell = self.cells[destInd]
                        if not destCell.piece == "":
                            if destCell.pieceColor != color:
                                if destCell.piece == "queen" or destCell.piece == "queenW" or destCell.piece == "rook" or destCell.piece == "rookW":
                                    checkMoves.append(mov)
                                    mov.unHMove()
                                    checkF = True
                                    break
                                break
                            else:
                                break
                #bishop
                if piece == "bishop" or piece == "queen":
                    curCoord = mov.coord
                    #upRight
                    for i in range(7):
                        if curCoord[0] + i + 1 > 7 or curCoord[1] - i - 1 < 0:
                            break
                        destCoord = (curCoord[0] + i + 1, curCoord[1] - i - 1)
                        destInd = destCoord[0] + destCoord[1]*8
                        destCell = self.cells[destInd]
                        if not destCell.piece == "":
                            if destCell.pieceColor != color:
                                if destCell.piece == "queen" or destCell.piece == "queenW" or destCell.piece == "bishop" or destCell.piece == "bishopW":
                                    checkMoves.append(mov)
                                    mov.unHMove()
                                    checkF = True
                                    break
                                break
                            else:
                                break
                    #upLeft
                    for i in range(7):
                        if curCoord[0] - i - 1 < 0 or curCoord[1] - i - 1 < 0:
                            break
                        destCoord = (curCoord[0] - i - 1, curCoord[1] - i - 1)
                        destInd = destCoord[0] + destCoord[1]*8
                        destCell = self.cells[destInd]
                        if not destCell.piece == "":
                            if destCell.pieceColor != color:
                                if destCell.piece == "queen" or destCell.piece == "queenW" or destCell.piece == "bishop" or destCell.piece == "bishopW":
                                    checkMoves.append(mov)
                                    mov.unHMove()
                                    checkF = True
                                    break
                                break
                            else:
                                break
                    #downLeft
                    for i in range(7):
                        if curCoord[0] - i - 1 < 0 or curCoord[1] + i + 1 > 7:
                            break
                        destCoord = (curCoord[0] - i - 1, curCoord[1] + i + 1)
                        destInd = destCoord[0] + destCoord[1]*8
                        destCell = self.cells[destInd]
                        if not destCell.piece == "":
                            if destCell.pieceColor != color:
                                if destCell.piece == "queen" or destCell.piece == "queenW" or destCell.piece == "bishop" or destCell.piece == "bishopW":
                                    checkMoves.append(mov)
                                    mov.unHMove()
                                    checkF = True
                                    break
                                break
                            else:
                                break
                    #downRight
                    for i in range(7):
                        if curCoord[0] + i + 1 > 7 or curCoord[1] + i + 1 > 7:
                            break
                        destCoord = (curCoord[0] + i + 1, curCoord[1] + i + 1)
                        destInd = destCoord[0] + destCoord[1]*8
                        destCell = self.cells[destInd]
                        if not destCell.piece == "":
                            if destCell.pieceColor != color:
                                if destCell.piece == "queen" or destCell.piece == "queenW" or destCell.piece == "bishop" or destCell.piece == "bishopW":
                                    checkMoves.append(mov)
                                    mov.unHMove()
                                    checkF = True
                                    break
                                break
                            else:
                                break
            if checkF:
                self.check = True
                
        for c in checkMoves:
            self.potentMoves.remove(c)


    def checkMoves(self):
        if not self.currentPiece == None:

            #PAWN MOVE
            if self.currentPiece.piece == "pawn" or self.currentPiece.piece == "pawnW":
                if self.currentPiece.piece == "pawn":
                    forward = 1
                    start = 1
                    color = "black"
                else:
                    forward = -1
                    start = 6
                    color = "white"

                curCoord = (self.currentPiece.getCoord())
                forCoord = (curCoord[0], curCoord[1] + forward)
                
                #capture coordinate?
                capCoord = (forCoord[0]+1, forCoord[1])
                capCoord2 = (forCoord[0]-1, forCoord[1])
                capInd = capCoord[0] + capCoord[1]*8
                capInd2 = capCoord2[0] + capCoord2[1]*8
                if color == "black":
                    if self.cells[capInd].pieceColor == "white":
                        self.potentMoves.append(self.cells[capInd])
                        self.cells[capInd].hMove()
                    if self.cells[capInd2].pieceColor == "white":
                        self.potentMoves.append(self.cells[capInd2])
                        self.cells[capInd2].hMove()

                if color == "white":
                    if self.cells[capInd].pieceColor == "black":
                        self.potentMoves.append(self.cells[capInd])
                        self.cells[capInd].hMove()
                    if self.cells[capInd2].pieceColor == "black":
                        self.potentMoves.append(self.cells[capInd2])
                        self.cells[capInd2].hMove()
                    
                ind = forCoord[0] + forCoord[1]*8
                frontCell = self.cells[ind]
                if frontCell.piece == "":
                    #first move option
                    if curCoord[1] == start:
                        firstMovCoord = (curCoord[0], curCoord[1] + 2*forward)
                        indfirstMov = firstMovCoord[0] + firstMovCoord[1]*8
                        firstMovCell = self.cells[indfirstMov]
                        if firstMovCell.piece == "":
                            firstMovCell.hMove()
                            self.potentMoves.append(firstMovCell)
                    frontCell.hMove()
                    self.potentMoves.append(frontCell)

            #KNIGHT MOVE
            if self.currentPiece.piece == "knight" or self.currentPiece.piece == "knightW":
                destinationList = []
                curCoord = (self.currentPiece.getCoord())
                destinationList.append((curCoord[0]+1,curCoord[1]-2))
                destinationList.append((curCoord[0]+1,curCoord[1]+2))
                destinationList.append((curCoord[0]-1,curCoord[1]-2))
                destinationList.append((curCoord[0]-1,curCoord[1]+2))
                destinationList.append((curCoord[0]+2,curCoord[1]-1))
                destinationList.append((curCoord[0]+2,curCoord[1]+1))
                destinationList.append((curCoord[0]-2,curCoord[1]-1))
                destinationList.append((curCoord[0]-2,curCoord[1]+1))
                for d in destinationList:
                    if d[0] >= 0:
                        if d[0] < 8:
                           if d[1] >= 0:
                               if d[1] < 8:
                                   ind = d[0] + d[1]*8
                                   destCell = self.cells[ind]
                                   if destCell.piece == "":
                                       destCell.hMove()
                                       self.potentMoves.append(destCell)
                                   elif destCell.pieceColor != self.currentPiece.pieceColor:
                                       destCell.hMove()
                                       self.potentMoves.append(destCell)
            #BISHOP MOVE ... and queen
            if self.currentPiece.piece == "bishop" or self.currentPiece.piece == "bishopW" or self.currentPiece.piece == "queen" or self.currentPiece.piece == "queenW":
                curCoord = (self.currentPiece.getCoord())
                #diagonal down right
                for i in range(7):
                    if curCoord[0] + i + 1 > 7 or curCoord[1] + i + 1 > 7:
                        break
                    destCoord = (curCoord[0] + i + 1, curCoord[1] + i + 1)
                    destInd = destCoord[0] + destCoord[1]*8
                    destCell = self.cells[destInd]
                    if not destCell.piece == "":
                        if destCell.pieceColor != self.currentPiece.pieceColor:
                            destCell.hMove()
                            self.potentMoves.append(destCell)
                            break
                        else:
                            break
                    else:
                        destCell.hMove()
                        self.potentMoves.append(destCell)
                #diagonal up left
                for i in range(7):
                    if curCoord[0] - i -1 < 0 or curCoord[1] - i - 1 < 0:
                        break
                    destCoord = (curCoord[0] - i - 1, curCoord[1] - i - 1)
                    destInd = destCoord[0] + destCoord[1]*8
                    destCell = self.cells[destInd]
                    if not destCell.piece == "":
                        if destCell.pieceColor != self.currentPiece.pieceColor:
                            destCell.hMove()
                            self.potentMoves.append(destCell)
                            break
                        else:
                            break
                    else:
                        destCell.hMove()
                        self.potentMoves.append(destCell)
                #diagonal up right
                for i in range(7):
                    if curCoord[0] + i + 1 > 7 or curCoord[1] - i - 1 < 0:
                        break
                    destCoord = (curCoord[0] + i + 1, curCoord[1] - i - 1)
                    destInd = destCoord[0] + destCoord[1]*8
                    destCell = self.cells[destInd]
                    if not destCell.piece == "":
                        if destCell.pieceColor != self.currentPiece.pieceColor:
                            destCell.hMove()
                            self.potentMoves.append(destCell)
                            break
                        else:
                            break
                    else:
                        destCell.hMove()
                        self.potentMoves.append(destCell)
                #diagonal down left
                for i in range(7):
                    if curCoord[0] - i - 1 < 0 or curCoord[1] + i + 1 > 7:
                        break
                    destCoord = (curCoord[0] - i - 1, curCoord[1] + i + 1)
                    destInd = destCoord[0] + destCoord[1]*8
                    destCell = self.cells[destInd]
                    if not destCell.piece == "":
                        if destCell.pieceColor != self.currentPiece.pieceColor:
                            destCell.hMove()
                            self.potentMoves.append(destCell)
                            break
                        else:
                            break
                    else:
                        destCell.hMove()
                        self.potentMoves.append(destCell)
            #ROOK MOVE ... and queen
            if self.currentPiece.piece == "rook" or self.currentPiece.piece == "rookW" or self.currentPiece.piece == "queen" or self.currentPiece.piece == "queenW":
                curCoord = (self.currentPiece.getCoord())
                #up
                for i in range(7):
                    if curCoord[1] + i + 1 > 7:
                        break
                    destCoord = (curCoord[0], curCoord[1] + i + 1)
                    destInd = destCoord[0] + destCoord[1]*8
                    destCell = self.cells[destInd]
                    if not destCell.piece == "":
                        if destCell.pieceColor != self.currentPiece.pieceColor:
                            destCell.hMove()
                            self.potentMoves.append(destCell)
                            break
                        else:
                            break
                    else:
                        destCell.hMove()
                        self.potentMoves.append(destCell)
                #down
                for i in range(7):
                    if curCoord[1] - i - 1 < 0:
                        break
                    destCoord = (curCoord[0], curCoord[1] - i - 1)
                    destInd = destCoord[0] + destCoord[1]*8
                    destCell = self.cells[destInd]
                    if not destCell.piece == "":
                        if destCell.pieceColor != self.currentPiece.pieceColor:
                            destCell.hMove()
                            self.potentMoves.append(destCell)
                            break
                        else:
                            break
                    else:
                        destCell.hMove()
                        self.potentMoves.append(destCell)
                #right
                for i in range(7):
                    if curCoord[0] + i + 1 > 7:
                        break
                    destCoord = (curCoord[0] + i + 1, curCoord[1])
                    destInd = destCoord[0] + destCoord[1]*8
                    destCell = self.cells[destInd]
                    if not destCell.piece == "":
                        if destCell.pieceColor != self.currentPiece.pieceColor:
                            destCell.hMove()
                            self.potentMoves.append(destCell)
                            break
                        else:
                            break
                    else:
                        destCell.hMove()
                        self.potentMoves.append(destCell)
                #left
                for i in range(7):
                    if curCoord[0] - i - 1 < 0:
                        break
                    destCoord = (curCoord[0] - i - 1, curCoord[1])
                    destInd = destCoord[0] + destCoord[1]*8
                    destCell = self.cells[destInd]
                    if not destCell.piece == "":
                        if destCell.pieceColor != self.currentPiece.pieceColor:
                            destCell.hMove()
                            self.potentMoves.append(destCell)
                            break
                        else:
                            break
                    else:
                        destCell.hMove()
                        self.potentMoves.append(destCell)

            #KING MOVE
            if self.currentPiece.piece == "king" or self.currentPiece.piece == "kingW":
                # add moves to list of potential moves
                destinationList = []
                curCoord = (self.currentPiece.getCoord())
                destinationList.append((curCoord[0]+1,curCoord[1]-1))
                destinationList.append((curCoord[0]+1,curCoord[1]+1))
                destinationList.append((curCoord[0]-1,curCoord[1]-1))
                destinationList.append((curCoord[0]-1,curCoord[1]+1))
                destinationList.append((curCoord[0],curCoord[1]-1))
                destinationList.append((curCoord[0],curCoord[1]+1))
                destinationList.append((curCoord[0]-1,curCoord[1]))
                destinationList.append((curCoord[0]+1,curCoord[1]))
                for d in destinationList:
                    if d[0] >= 0:
                        if d[0] < 8:
                           if d[1] >= 0:
                               if d[1] < 8:
                                   ind = d[0] + d[1]*8
                                   destCell = self.cells[ind]
                                   if destCell.piece == "":
                                       destCell.hMove()
                                       self.potentMoves.append(destCell)
                                   elif destCell.pieceColor != self.currentPiece.pieceColor:
                                       destCell.hMove()
                                       self.potentMoves.append(destCell)

                # remove moves from list of potential moves that put the king in check
                self.checkCheck()
                # check for check"

                '''For all potential moves, have the king "act as
                    a particular piece". For example: it pretends to be a knight.
                    Try to move as that knight. If it could capture an opponent's
                    knight then it would have been in check.'''         
        
        return True


    '''def checked(self):
        if self.whoMove == "white":
            k = "kingW"
        else:
            k = "king"

        for c in self.cells:
            if c.piece == k:
                self.currentPiece = c
                self.potentMoves = [c]
                if self.check:
                    return True
                
        return False'''
                    


