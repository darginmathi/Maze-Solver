from cell import Cell
import time
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None): # x1, y1 == Margin
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        if seed:
            random.seed(seed)
        
        # calls to create cells when a Maze object is created
        
        self._create_cells()
        
        self._break_walls_r(0, 0)
                
        self._reset_visited()
                
                
    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                column.append(cell)
            self._cells.append(column)
            
        self._break_entrance_and_exit()
            
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
            
    # will be used in _create_cells() to create entry and exit.
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
    
    
    # create a random Maze    
        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            
            # adds unvisited cells to list
            
            if i+1 < self._num_cols and not self._cells[i+1][j].visited:
                to_visit.append([i+1, j])
            if i-1 >= 0 and not self._cells[i-1][j].visited:
                to_visit.append([i-1, j])
            if j+1 < self._num_rows and not self._cells[i][j+1].visited:
                to_visit.append([i, j+1])
            if j-1 >= 0 and not self._cells[i][j-1].visited:
                to_visit.append([i, j-1])

            # break if no where to go

            if not to_visit:
                self._draw_cell(i, j)
                return
            
            # rng choose where to go
            
            rng = random.choice(to_visit)
            k, l = rng[0], rng[1]
            
            # break walls by checking the direction
            
            if i > k:
                # left
                self._cells[i][j].has_left_wall = False
                self._cells[k][l].has_right_wall = False
            elif i < k:
                # right
                self._cells[i][j].has_right_wall = False
                self._cells[k][l].has_left_wall = False
            elif j > l:
                # bot
                self._cells[i][j].has_bottom_wall = False
                self._cells[k][l].has_top_wall = False
            elif j < l:
                #top
                self._cells[i][j].has_top_wall = False
                self._cells[k][l].has_bottom_wall = False
            
            self._draw_cell(i, j)
            # recursion
                
            self._break_walls_r(k, l)
            
    def _reset_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False        
            
    # helper method used in create_cells()
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        
        self._cells[i][j].draw(x1, y1, x2, y2)
        
        self._animate()
        
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
        