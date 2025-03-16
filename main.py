from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    
    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    d = Cell(win)
    d.has_right_wall = False
    d.draw(125, 125, 200, 200)

    e = Cell(win)
    e.has_bottom_wall = False
    e.draw(225, 225, 250, 250)

    f = Cell(win)
    f.has_top_wall = False
    f.draw(300, 300, 500, 500)
    
    g = Cell(win)
    g.has_top_wall = False
    g.draw(50, 10, 200, 500)
    
    c.draw_move(d)
    e.draw_move(f, True)
    
    
    win.wait_for_close()
    
    
if __name__ == "__main__": 
    main()