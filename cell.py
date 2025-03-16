from graphics import Line, Point


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        
        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        
            
    def draw_move(self, to_cell, undo=False):
        mid_x_s = abs(self._x2 - self._x1) // 2 + self._x1
        mid_y_s = abs(self._y2 - self._y1) // 2 + self._y1
        mid_x = abs(to_cell._x2 - to_cell._x1) // 2 + to_cell._x1
        mid_y = abs(to_cell._y2 - to_cell._y1) // 2 + to_cell._y1
        colour = "grey" if undo else "red"
        self._win.draw_line(Line(Point(mid_x_s, mid_y_s), Point(mid_x, mid_y)), fill_colour = colour)