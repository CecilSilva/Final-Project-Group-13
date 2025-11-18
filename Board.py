from Cell import Cell
import pygame
from sudoku_generator import generate_sudoku
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height-80
        self.cols = 9
        self.rows = 9
        self.difficulty = difficulty
        self.board = generate_sudoku(9, self.difficulty)
        self.screen = screen
        self.board_cells = [[Cell(self.board[a][b], a, b, screen) for b in range(9)] for a in range(9)]
        # Constructor for the Board class.
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy medium, or hard.

    def draw(self):
        cell_size_w = self.width / 9
        cell_size_h = self.height / 9


        # Draw cells
        for a in range(0, self.cols):
            for b in range(0, self.rows):
                self.board_cells[a][b].draw()




        for i in range (10):#veritcal line
            #Thick lines
            if i%3 == 0:
                thickness = 5
            else:
                thickness = 2

            pygame.draw.line(self.screen, (0,0,0), (i*cell_size_w, 0), (i*cell_size_w, self.width), thickness)

            pygame.draw.line(self.screen, (0,0,0), (0, i*cell_size_h), (self.height, i*cell_size_h), thickness)




            if Cell.selectedcellpos:
                x = Cell.selectedcellpos[1]*cell_size_h
                y = Cell.selectedcellpos[0]*cell_size_w
                rect = pygame.Rect(x, y, cell_size_w, cell_size_h)
                pygame.draw.rect(self.screen, (176, 2, 28), rect, 4)

            # else:
            #     if self.editable:
            #         background = (184, 249, 252)
            #         pygame.draw.rect(self.screen, background, cell_rect)
            #     else:
            #         background = (255, 255, 255)
            #         pygame.draw.rect(self.screen, background, cell_rect)





        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.



    def select(self, row, col):

        self.selectedcell = self.board_cells[row][col]
        pass


        # Marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.

    def click(self, x, y):
        if 0 < x < self.width and 0 < y < self.height:
            print(y, x)
            print(y // 60, x // 60)
            return (y // 60, x // 60)
        else: return None


        pass
    # 	If a tuple of (x,y) coordinates is within the displayed board,
    # this function returns a tuple of the (row, col) of the cell which was clicked.
    # Otherwise, this function returns None.

    def clear(self):
        if self.selectedcell.editable:
            self.selectedcell.value = ""
            self.selectedcell.sketched_value = None

        pass
    # 	Clears the value cell.
    # Note that the user can only remove the cell values and
    # sketched values that are filled by themselves.

    def sketch(self, value):
        self.selectedcell.set_sketched_value(value)
        pass
        # Sets the sketched value of the current selected cell equal to the user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.

    def place_number(self, value):
        self.selectedcell.value = value

    # 	Sets the value of the current selected cell equal to the user entered value.
    # Called when the user presses the Enter key.

    def reset_to_original(self):
        for list in self.board_cells:
            for cell in list:
                if cell.editable:
                    cell.value = 0

    # 	Resets all cells in the board to their original values
    # (0 if cleared, otherwise the corresponding digit).


    def is_full(self):
        for list in self.board_cells:

            for cell in list:
                if cell.value == 0 or cell.value == "":
                    return False
        return True

        # Returns a Boolean value indicating whether the board is full or not.

    def update_board(self):
        for a in range (len(self.board_cells)):
            for b in range (len(self.board_cells)):
                if self.board[a][b] != self.board_cells[b][a].value:
                    self.board[a][b] = self.board_cells[b][a].value



        # Updates the underlying 2D board with the values in all cells.

    def find_empty(self):
        for a in range (self.board_cells):
            for b in range (self.board_cells):
                if self.board_cells[a][b].value == "" or self.board_cells[a][b].value == 0:
                    return (a, b)

        # Finds an empty cell and returns its row and col as a tuple (x,y).


    def check_board(self):

        self.update_board()
        for list in self.board_cells:
            for cell in list:
                if cell.value == "":
                    cell.value = 0
        sum = 0
        #count must equal 45 (1+2+3+4... per row)
        for b in range (len(self.board_cells)):
            sum = 0
            for a in range (len(self.board_cells)):#check all columns

                sum += self.board_cells[a][b].value
            if sum != 45:
                return False

        for b in range (len(self.board_cells)):#check all rows
            sum = 0
            for c in range (len(self.board_cells)):
                sum += self.board_cells[b][c].value
            if sum != 45:
                return False

        #boxcount = 0
        for d in range (3):

            for a in range (3):#check all boxes now
                sum = 0
                # boxcount += 1
                #print(f"box{boxcount}")
                for b in range (a*3, a*3+3):
                    for c in range (d*3, d*3+3):

                        sum += self.board_cells[b][c].value
                if sum != 45:
                    return False
        return True









    # Check whether the Sudoku board is solved correctly.
