import pygame

class Cell:
    selectedcellpos = None


    def __init__(self, value, row, col, screen):
        self.value = value
        if self.value == 0:
            self.value = ""
        self.row = row
        self.col = col
        self.screen = screen
        self.cell_size = 60
        self.editable = False


        #Constructor for the Cell class

    def set_cell_value(self, value):
        self.value = value #Setter for this cell’s value




    def set_sketched_value(self, value):
        self.sketched_value = value#Setter for this cell’s sketched value




    def draw(self):






        #Define size of cell
        #Calculate coordinates of top left corner of cell
        x = self.col * self.cell_size
        y = self.row * self.cell_size
        #Draw background rectangle
        if self.value == "":
            self.editable = True

        if self.editable:
            border = (97, 231, 255)
        else:
            border = (0, 0, 0) #Border color
        cell_rect = pygame.Rect(x, y, self.cell_size, self.cell_size)  # Rectangle in the cell

        #Selecting cell mechanism
        if Cell.selectedcellpos:
            if self.row == Cell.selectedcellpos[0] and self.col == Cell.selectedcellpos[1]:
                border = (252, 16, 0)



        #Drawing the numbers
        font = pygame.font.SysFont(None, 30)
        number_text = font.render(str(self.value), True, (0,0,0))
        text_rect = number_text.get_rect(center=cell_rect.center)

        pygame.draw.rect(self.screen, border, cell_rect, 3)
        self.screen.blit(number_text, text_rect)




        pass


        # Draws this cell, along with the value inside it.
        # If this cell has a nonzero value, that value is displayed.
        # Otherwise, no value is displayed in the cell.
        # The cell is outlined red if it is currently selected.
