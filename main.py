import pygame as pg
from cursor import Cursor
from sentence import Sentence

pg.init()

FONT = pg.font.Font("seguisym.ttf", 18)
BLACK = (0, 0, 0)

height = 900
width = 800

pos = [width // 2, 40]

scr = pg.display.set_mode((width, height))
scr.fill((106,190,48))
pg.display.update()

run = True

cursor = Cursor(width // 2, 70)

inp = ""

cents = []
index = 1

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
            elif event.key == pg.K_RETURN:
                if inp != "":
                    cents.append(Sentence(inp, pos, index))
                    index += 1
                    pos[1] += 50
                    inp = ""
            else:
                inp += event.unicode
    scr.fill((255,255,255))

    if inp != "":
        renderedText = FONT.render(inp, True, BLACK)
        realPos = [pos[0] - (renderedText.get_width() / 2), pos[1] - 40]
        scr.blit(renderedText, realPos)

        pass

    for cent in cents:
        cent.render(scr)

    pg.display.update()
