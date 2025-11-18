import pygame
pygame.init()
from Board import *

pygame.init()


width = 540
height = 620
screen2 = pygame.display.set_mode((width, height))

difficulty = 2
board = Board(width,height, screen2, difficulty)




#game
running = True
game_over = False

while running:
    if not game_over:
        screen2.fill((255, 255, 255))
        button_rect1 = pygame.Rect(50, 560, 125, 40)
        button_rect2 = pygame.Rect(207, 560, 125, 40)
        button_rect3 = pygame.Rect(365, 560, 125, 40)
        pygame.draw.rect(screen2, (255, 212, 105), button_rect1,border_radius=50)
        pygame.draw.rect(screen2, (255, 212, 105), button_rect2, border_radius=50)
        pygame.draw.rect(screen2, (255, 212, 105), button_rect3, border_radius=50)
        font = pygame.font.SysFont(None, 35)
        text_surface1 = font.render("Reset", True, (0, 0, 0))
        text_surface2 = font.render("Restart", True, (0, 0, 0))
        text_surface3 = font.render("Quit", True, (0, 0, 0))

        text_rect1 = text_surface1.get_rect(center=button_rect1.center)
        text_rect2 = text_surface2.get_rect(center=button_rect2.center)
        text_rect3 = text_surface3.get_rect(center=button_rect3.center)

        screen2.blit(text_surface1, text_rect1)
        screen2.blit(text_surface2, text_rect2)
        screen2.blit(text_surface3, text_rect3)

        board.draw()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


        elif event.type == pygame.MOUSEBUTTONDOWN:  # mous click
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[1] <= 540:
                Cell.selectedcellpos = board.click(mouse_pos[0], mouse_pos[1])
                board.select(Cell.selectedcellpos[0], Cell.selectedcellpos[1])

        if event.type == pygame.KEYDOWN:
            if Cell.selectedcellpos:
                if event.type == pygame.KEYDOWN:
                    if Cell.selectedcellpos[0] >= 1:
                        if event.key == pygame.K_UP:
                            Cell.selectedcellpos = Cell.selectedcellpos[0]-1, Cell.selectedcellpos[1]
                            board.select(Cell.selectedcellpos[0], Cell.selectedcellpos[1])
                    if Cell.selectedcellpos[0] <= 7:
                        if event.key == pygame.K_DOWN:
                            Cell.selectedcellpos = Cell.selectedcellpos[0] + 1, Cell.selectedcellpos[1]
                            board.select(Cell.selectedcellpos[0], Cell.selectedcellpos[1])
                    if Cell.selectedcellpos[1] <= 7:
                        if event.key == pygame.K_RIGHT:
                            Cell.selectedcellpos = Cell.selectedcellpos[0], Cell.selectedcellpos[1] + 1
                            board.select(Cell.selectedcellpos[0], Cell.selectedcellpos[1])
                    if Cell.selectedcellpos[1] >= 1:
                        if event.key == pygame.K_LEFT:
                            Cell.selectedcellpos = Cell.selectedcellpos[0], Cell.selectedcellpos[1] - 1
                            board.select(Cell.selectedcellpos[0], Cell.selectedcellpos[1])






                    if board.selectedcell.editable:
                        if event.key == pygame.K_1:
                            board.sketch(1)
                        elif event.key == pygame.K_2:
                            board.sketch(2)
                        elif event.key == pygame.K_3:
                            board.sketch(3)
                        elif event.key == pygame.K_4:
                            board.sketch(4)
                        elif event.key == pygame.K_5:
                            board.sketch(5)
                        elif event.key == pygame.K_6:
                            board.sketch(6)
                        elif event.key == pygame.K_7:
                            board.sketch(7)
                        elif event.key == pygame.K_8:
                            board.sketch(8)
                        elif event.key == pygame.K_9:
                            board.sketch(9)

                    if board.selectedcell.editable:
                        if board.selectedcell.sketched_value:
                            if event.key == pygame.K_KP_ENTER or event.key == pygame:
                                board.place_number(board.selectedcell.sketched_value)
                                board.selectedcell.sketched_value = None
                        if event.key == pygame.K_DELETE:
                                board.clear()
            else:
                Cell.selectedcellpos = ((height-80)//Cell.cell_size//2, width//60//2)
                board.select(Cell.selectedcellpos[0], Cell.selectedcellpos[1])
        if board.is_full():
            if board.check_board():

                font = pygame.font.SysFont(None, 50)
                game_over = True
                text = font.render("You Won!", True, (255, 0, 0))
                screen2.fill((255, 255, 255))
                screen2.blit(text, (width / 3, height // 2))


            else:
                font = pygame.font.SysFont(None, 50)
                game_over = True
                text = font.render("Game Over!", True, (255, 0, 0))
                screen2.fill((255, 255, 255))
                screen2.blit(text, (width/3, height//2))













        pygame.display.update()

