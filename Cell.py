import pygame

class Cell:
    selectedcellpos = None
    cell_size = 60

    def __init__(self, value, row, col, screen):
        self.value = value
        if self.value == 0:
            self.value = ""
        self.row = row
        self.col = col
        self.screen = screen

        self.editable = False
        self.sketched_value = None



        #Constructor for the Cell class

    def set_cell_value(self, value):
        self.value = value #Setter for this cell’s value




    def set_sketched_value(self, value):
        self.sketched_value = value#Setter for this cell’s sketched value




    def draw(self):





        #Define size of cell
        #Calculate coordinates of top left corner of cell
        self.x = self.col * self.cell_size
        self.y = self.row * self.cell_size
        #Draw background rectangle
        if self.value == "":
            self.editable = True

        if self.editable:
             background = (184, 249, 252)
        else:
             border = (0, 0, 0) #Border color
        cell_rect = pygame.Rect(self.x, self.y, self.cell_size, self.cell_size)  # Rectangle in the cell







        #Drawing the numbers



        if self.editable:
            pygame.draw.rect(self.screen, background, (self.x, self.y, self.cell_size, self.cell_size))

        if self.sketched_value != None and self.editable:
            font = pygame.font.SysFont(None, 35)
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (self.x + 5, self.y + 5))








        #draws number
        font = pygame.font.SysFont(None, 40)
        number_text = font.render(str(self.value), True, (0, 0, 0))
        text_rect = number_text.get_rect(center=cell_rect.center)
        self.screen.blit(number_text, text_rect)

        # Draws this cell, along with the value inside it.
        # If this cell has a nonzero value, that value is displayed.
        # Otherwise, no value is displayed in the cell.
        # The cell is outlined red if it is currently selected.
