import pygame, sys
from board import Graphic
from pygame.locals import *
from settings import *
from sudoku import Sudoku
import random

pygame.init()
fps = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku")

def main():
    sudoku_board = Sudoku()
    graphic = Graphic(sudoku_board.board)
    yInit = 250
    offsetInit = 50
    pressed_cords = (None,None)
    pressed = False
    
    while True:
        screen.fill(LIGHT_GRAY)
        graphic.draw_cell(screen,xMARGIN,yMARGIN)
        graphic.draw_button(screen,BUTTON_X_MARGIN,yMARGIN)
        graphic.draw_text(screen,BUTTON_X_MARGIN,yInit,"RESET",LIGHT_GRAY,DARK_GRAY)
        graphic.draw_text(screen,BUTTON_X_MARGIN,yInit+offsetInit,"NEW GAME",LIGHT_GRAY,DARK_GRAY)
        graphic.draw_text(screen,BUTTON_X_MARGIN,yInit+(offsetInit*2),"SOLVE SUDOKU",LIGHT_GRAY,DARK_GRAY)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for row in range(9):
                    for col in range(9):
                        x = col * (CELL_SIZE + GAP) + xMARGIN
                        y = row * (CELL_SIZE + GAP) + yMARGIN
                        rect = pygame.Rect(x,y,CELL_SIZE,CELL_SIZE)
                        if rect.collidepoint(mouse_pos):
                            pressed_cords = (col,row)
                            pressed = True
                            print((col,row))

        if pressed:
            x = pressed_cords[0] * (CELL_SIZE + GAP) + xMARGIN
            y = pressed_cords[1] * (CELL_SIZE + GAP) + yMARGIN
            pressed_rect = pygame.Rect(x,y,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,(0,255,0),pressed_rect)
            
            number_text = graphic.font2.render(str(graphic.grid_numbers[pressed_cords[0]][pressed_cords[1]]), True, BLACK)
            text_rect = number_text.get_rect(center=(x + (CELL_SIZE//3)  + GAP + BOARDER_THICK, y + (CELL_SIZE//2)))
            screen.blit(number_text, text_rect)
            
            
        pygame.display.update()
        fps.tick(FPS)

if __name__ == '__main__':
    main()
