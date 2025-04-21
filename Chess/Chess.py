from graphics import*
from Chessboard import*
from Cell import*
from Button import*

def initialPieces(cb):
    for i in range(8):
        cb.cells[8+i].updatePiece("pawn")
        cb.cells[48+i].updatePiece("pawnW")
                
    cb.cells[0].updatePiece("rook")
    cb.cells[7].updatePiece("rook")
    cb.cells[1].updatePiece("knight")
    cb.cells[6].updatePiece("knight")
    cb.cells[2].updatePiece("bishop")
    cb.cells[5].updatePiece("bishop")
    cb.cells[3].updatePiece("queen")
    cb.cells[4].updatePiece("king")

    cb.cells[56].updatePiece("rookW")
    cb.cells[63].updatePiece("rookW")
    cb.cells[57].updatePiece("knightW")
    cb.cells[62].updatePiece("knightW")
    cb.cells[58].updatePiece("bishopW")
    cb.cells[61].updatePiece("bishopW")
    cb.cells[59].updatePiece("queenW")
    cb.cells[60].updatePiece("kingW")



def main():

    win = GraphWin("Chess", 1000, 800)
    
    cb = Chessboard(win)
    
    quiButton = Button(win, "Exit", 60, Point(870, 220))
    turnT = Text(Point(850, 400), "White plays")
    turnT.draw(win)
    startButton = Button(win, "", 60, Point(850, 100))
    startT = Text(Point(850, 100), "START")
    startT.draw(win)
    checkT = Text(Point(850,550), "")
    checkT.draw(win)
                         
    restart = False
    
    while True:
    
        m1 = win.getMouse()
        cb.selectCell(m1)
        if cb.move:
            turnT.setText(cb.whoMove + " plays")
            
        cb.checkMoves()

        if quiButton.isClicked(m1):
            win.close()
            break

        if startButton.isClicked(m1):

            startT.setText("RESTART")
            initialPieces(cb)       
            restart = True

        if restart:
            if startButton.isClicked(m1):
                for i in range(64):
                    cb.cells[i].empty()
                initialPieces(cb)
                cb.setWhoMove("white")
                turnT.setText(cb.whoMove + " plays")
                    

if __name__ == "__main__":
    main()
