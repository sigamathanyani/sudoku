import pygame, sys
from board import Graphic
from pygame.locals import *
from settings import *

pygame.init()
fps = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku")

def main():
    graphic = Graphic()
    yInit = 250
    offsetInit = 50
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

        pygame.display.update()
        fps.tick(FPS)

if __name__ == '__main__':
    main()
