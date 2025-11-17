import pygame
from Cell import Cell  # import your Cell class
from sudoku_generator import generate_sudoku
pygame.init()

# Window size
WIDTH = 540
HEIGHT = 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test Cell.draw()")

# Clock for FPS
clock = pygame.time.Clock()
#This is where hte main program will run



# test_cell = Cell(5, 0, 0, screen)
# test_cell.selected = True  # optional, to see the red highlight

board = generate_sudoku(9, 20)
board_cells = [[Cell(board[a][b], a, b, screen) for b in range(9)] for a in range(9)]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:#mous click
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            Cell.selectedcellpos = (mouse_pos[1] // 60, mouse_pos[0] // 60)
            selectedcell = board_cells[Cell.selectedcellpos[0]][Cell.selectedcellpos[1]]
            print(Cell.selectedcellpos) #Prints (row, col) that your mouse is in

        if event.type == pygame.KEYDOWN:
            if selectedcell.editable:
                if event.key == pygame.K_1:
                    selectedcell.set_cell_value(1)
                elif event.key == pygame.K_2:
                    selectedcell.set_cell_value(2)
                elif event.key == pygame.K_3:
                    selectedcell.set_cell_value(3)
                elif event.key == pygame.K_4:
                    selectedcell.set_cell_value(4)
                elif event.key == pygame.K_5:
                    selectedcell.set_cell_value(5)
                elif event.key == pygame.K_6:
                    selectedcell.set_cell_value(6)
                elif event.key == pygame.K_7:
                    selectedcell.set_cell_value(7)
                elif event.key == pygame.K_8:
                    selectedcell.set_cell_value(8)
                elif event.key == pygame.K_9:
                    selectedcell.set_cell_value(9)











    # Fill screen with background color
    screen.fill((255, 255, 255))  # white background




    # Draw the cell


    for a in range(0, 9):
        for b in range(0, 9):

            value = board[a][b]
            board_cells[a][b].draw()


    # Update the display
    pygame.display.flip()
    clock.tick(30)  # 30 FPS