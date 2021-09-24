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

clock = pg.time.Clock()

cursor = Cursor(pos, FONT.render("I", True, BLACK), scr)

inp = ""
lastInp = ""
inpRender = Sentence(inp, (width // 2, 8), False)

cents = []
index = 1

n = 0

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
            elif event.key == pg.K_BACKSPACE and inp != "":
                inp = inp[:-1]
            elif event.key == pg.K_RETURN:
                if inp != "":
                    cents.append(Sentence(inp, pos, index))
                    index += 1
                    pos[1] += 22
                    inp = ""
                    lastInp = inp
                    inpRender.update("")

            else:
                inp += event.unicode

    scr.fill((255,255,255))

    inpRender.render(scr)
    if inp != "" and inp != lastInp:
        lastInp = inp
        inpRender.update(inp)
    for cent in cents:
        cent.render(scr)

    n += 1
    if n < 20:
        cursor.render()
    else:
        if n == 39:
            n = 0

    clock.tick(30)
    pg.display.update()
