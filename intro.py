import pygame
import sys

import numpy as np
from logic import matrizProblem

pygame.init()

# ------ CONTS
background_color = (251, 247, 245)
WHITE = (250, 250, 250)
SMOKE = (160, 160, 160)
SIZE = (460, 560)
INITIAL_X = 30
INITIAL_y = 80
blockSize = 44
# Crear ventana
screen = pygame.display.set_mode(SIZE)

pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
myfont = pygame.font.SysFont('Curier new', 30)
img = pygame.image.load('icon.ico')
pygame.display.set_icon(img)
pygame.display.set_caption("SUDOKU SOLVER")

matriz = matrizProblem()
clock = pygame.time.Clock()
# Create TextInput-object
buffer = 5


def insert(screen, position):
    i, j = position[0], position[1]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                try:
                    if(matriz[i-1][j-1] != 0):
                        return
                except:
                    print("{} {}".format(i, j))
                    return
                if(event.key == 48):  # checking with 0
                    matriz[i][j] = event.key - 48
                    pygame.draw.rect(screen, WHITE, (
                        position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    pygame.display.update()
                    return
                if(0 < event.key - 48 < 10):  # We are checking for valid input
                    pygame.draw.rect(screen, (0, 0, 0), (
                        position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    value = myfont.render(
                        str(event.key-48), False, (0, 0, 0))
                    screen.blit(value, (position[0]*50 + 15, position[1]*50))
                    matriz[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return


def drawGrid() -> None:
    for x in range(INITIAL_X, blockSize*9, blockSize):
        for y in range(INITIAL_y, blockSize*10, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, SMOKE, rect, 1)

    for i in range(4):
        pygame.draw.line(screen, SMOKE, (INITIAL_X, INITIAL_y+blockSize*3*i),
                         (INITIAL_X+blockSize*9, INITIAL_y+blockSize*3*i), 5)

    for i in range(4):
        pygame.draw.line(screen, SMOKE, (INITIAL_X+blockSize*3*i, INITIAL_y),
                         (INITIAL_X+blockSize*3*i, INITIAL_y+blockSize*9,), 5)


def insertValues() -> None:
    for i in range(9):
        for k in range(9):
            if(matriz[i][k] == 0):

                pass
            else:
                textsurface = myfont.render(
                    '{}'.format(matriz[i][k]), False, (0, 0, 0))
                screen.blit(textsurface, (INITIAL_X+18 +
                            blockSize*i, INITIAL_y+14+blockSize*k))


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            print(pos)
            insert(screen, (pos[0]//44, (int(pos[1]*0.84))//44))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --------- Fill background --------
    screen.fill(WHITE)

    # --------- Drawing grid --------
    drawGrid()

    # --------- Starting the game --------
    insertValues()
    # --------- Writing title and footer--------
    textsurface = myfont.render('SUDOKU', False, (0, 0, 0))
    screen.blit(textsurface, (185, 35))

    textsurface = myfont.render('Press "S" to solve', False, (0, 0, 0))
    screen.blit(textsurface, (60, 510))
    # --------- Update scope --------
    pygame.display.flip()
    clock.tick(30)
