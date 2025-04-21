from graphics import*
from OBoard import*
from Cell import*
from Button import*

def initialPieces(cb):
    
    cb.cells[27].updatePiece("white")
    cb.cells[28].updatePiece("black")
    cb.cells[35].updatePiece("black")
    cb.cells[36].updatePiece("white")

def main():

    win = GraphWin("Chess", 1000, 800)
    
    ob = OBoard(win)
    
    quiButton = Button(win, "Exit", 60, Point(870, 220))
    turnT = Text(Point(850, 400), "white plays")
    turnT.draw(win)
    startButton = Button(win, "", 60, Point(850, 100))
    startT = Text(Point(850, 100), "START")
    startT.draw(win)
    checkT = Text(Point(850,550), "")
    checkT.draw(win)

    while True:
        m1 = win.getMouse()
        if quiButton.isClicked(m1):
            win.close()
            exit()

        if startButton.isClicked(m1):

            startT.setText("RESTART")
                     
            restart = True
            break

    initialPieces(ob)
    
    while True:
        turnT.setText(ob.whoMove + " plays")
        mov = ob.checkMoves()
        m1 = win.getMouse()

        if quiButton.isClicked(m1):
            win.close()
            break

        if restart:
            if startButton.isClicked(m1):
                for i in range(64):
                    ob.cells[i].empty()
                initialPieces(ob)
                ob.setWhoMove("black")
                turnT.setText(ob.whoMove + " plays")

        for c in mov:
            if c.isClicked(m1):
                ob.place(c)
                break
        for c in mov:
            c.unHighlight()
        
                    

if __name__ == "__main__":
    main()
