import pygame, sys
from settings import *
from pygame.locals import *
import random

pygame.init()

class Graphic:
    def __init__(self,sudoku_board):
        self.font = pygame.font.Font(FONT_NAME,FONT_SIZE)
        self.font2 = pygame.font.Font(FONT_NAME,20)
        self.grid_numbers = sudoku_board

    def draw_cell(self,win,xS,yS):
        for row in range(9):
            for col in range(9):
                x = col * (CELL_SIZE + GAP)
                y = row * (CELL_SIZE + GAP)
                pygame.draw.rect(win,DARK_GRAY,(xS+x,yS+y,CELL_SIZE,CELL_SIZE),1)
                
                if row % 3 ==0:
                    pygame.draw.line(win,BLACK,(xS+x,yS+y),(xS+x+CELL_SIZE,yS+y),BOARDER_THICK)
                if row == 8:
                    pygame.draw.line(win,BLACK,(xS+x,yS+y+CELL_SIZE),(xS+x+CELL_SIZE,yS+y+CELL_SIZE),BOARDER_THICK)
            
                if col % 3 ==0:
                    pygame.draw.line(win,BLACK,(xS+x,yS+y),(xS+x,yS+y+CELL_SIZE),BOARDER_THICK)
                if col == 8:
                    pygame.draw.line(win,BLACK,(xS+x+CELL_SIZE,yS+y),(xS+x+CELL_SIZE,yS+y+CELL_SIZE),BOARDER_THICK)

                number_text = self.font2.render(str(self.grid_numbers[col][row]), True, BLACK)

                text_rect = number_text.get_rect(center=(x + (CELL_SIZE//2) + CELL_SIZE + GAP + BOARDER_THICK, y + (CELL_SIZE//2)+CELL_SIZE-BOARDER_THICK-GAP-CELL_NUMBER))
                win.blit(number_text, text_rect)

        
    def draw_button(self,win,xS,yS):
        num = 0
        for row in range(3):
            for col in range(3):
                num+= 1
                x = col * (BUTTON_SIZE + BUTTON_GAP)
                y = row * (BUTTON_SIZE + BUTTON_GAP)
                pygame.draw.rect(win,DARK_GRAY,(xS+x,yS+y,BUTTON_SIZE,BUTTON_SIZE),BUTTON_BORDER)
                
                number_text = self.font.render(str(num), True, BLACK)
                text_rect = number_text.get_rect(center=(x + (BUTTON_X_MARGIN) + BUTTON_SIZE//2, y + (BUTTON_SIZE//2)+(BUTTON_SIZE//2)-BUTTON_BORDER-GAP))
                win.blit(number_text, text_rect)


    def draw_text(self,win,x,y,name,fg,bg):
        text = self.font.render(name,False,fg,bg)
        textRect = text.get_rect()
        textRect.left = x
        textRect.top = y
        win.blit(text,textRect)
        
