import pygame as pg
from cursor import Cursor
from sentence import Sentence
from line import Line
from end import End
from rule import Rule
from text import Text

pg.init()

height = 900
width = 800
scr = pg.display.set_mode((width, height))
clock = pg.time.Clock()

currPos = [width // 2, 60]
cursor = Cursor(currPos, Text("I", 'black', True, False), scr)
inp = ""
lastInp = "" 
boolean = True
# typing: true if typing sequence, false if inputting if sequence is true of false
typing = True
inpRender = Sentence(inp, (width // 2, 8), False, False)

cents = []
lines = []
ends = []
scale = 2
openBranches = [[currPos, 0]]
branch = 0
index = 1
waitingForWidth = False
ruleInput = False
ruleString = ""
rules = []

over = False
n = 0
run = True
while run:
    for event in pg.event.get():
        if over:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    pg.image.save(scr, "images/graph.png")
                    # scr.save("test.png")
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                if over:
                    run = False
                else:
                    over = True
            elif event.key == pg.K_BACKSPACE and inp != "":
                if typing:
                    inp = inp[:-1]
                else:
                    typing = True
                    inp = inp[:-1]
            elif event.key == pg.K_RIGHT:
                ends.append(End(Text("×", 'black', True, False), currPos))
                openBranches.pop(branch)
                if len(openBranches) == 0:
                    over = True
                    currPos = [0, 0]
                elif branch + 1 > len(openBranches):
                    branch = 0
                    currPos = openBranches[0][0]
                else:
                    currPos = openBranches[branch][0]
                cursor.update(currPos)

            elif event.key == pg.K_LEFT:
                ends.append(End(Text("o", 'black', True, False), currPos))
                openBranches.pop(branch)
                if len(openBranches) == 0:
                    over = True
                elif branch + 1 > len(openBranches):
                    branch = 0
                    currPos = openBranches[0][0]
                else:
                    currPos = openBranches[branch][0]
                cursor.update(currPos)

            elif event.key == pg.K_UP:
                if waitingForWidth == False:
                    waitingForWidth = True
                    scale = 2
                    newLine = Line(True, currPos, scale)
                    lines.append(newLine)
                else:
                    scale += 1
                    newLine = Line(True, currPos, scale)
                    lines[-1] = newLine

                # split in two
            elif event.key == pg.K_DOWN:
                if waitingForWidth == True:
                    scale -= 1
                    newLine = Line(True, currPos, scale)
                    lines[-1] = newLine
                else:
                    lines.append(Line(False, currPos, False))
                    currPos[1] += 42
                    cursor.update(currPos)
                    openBranches[branch][0] = currPos
                    ruleInput = True

            elif event.key == pg.K_RETURN:
                if waitingForWidth == True:
                    layers = openBranches[branch][1]
                    newLine = Line(True, currPos, scale)
                    openBranches[branch] = [[newLine.endPos1[0], newLine.endPos1[1]], layers + 1]
                    openBranches.insert(branch + 1, [[newLine.endPos2[0], newLine.endPos2[1]], layers + 1])
                    currPos = [newLine.endPos1[0], newLine.endPos1[1]]
                    cursor.update(currPos)
                    lines.append(newLine)
                    waitingForWidth = False
                    ruleInput = True

            elif event.key == pg.K_TAB:
                # switch branch
                if branch + 1 < len(openBranches):
                    branch += 1
                    currPos = openBranches[branch][0]
                else:
                    branch = 0
                    currPos = openBranches[0][0]
                cursor.update(currPos)

            elif event.key == pg.K_SPACE:
                if ruleInput:
                    rules.append(Rule(ruleString, lines[-1]))
                    ruleString = ""
                    ruleInput = False
                elif typing:
                    typing = False
                else:
                    if inp != "":
                        cents.append(Sentence(inp, currPos, index, boolean))
                        index += 1
                        currPos[1] += 22
                        cursor.update(currPos)
                        openBranches[branch][0] = currPos
                        inp = ""
                        lastInp = inp
                        inpRender.update("")
                        typing = True
            else:
                if ruleInput:
                    ruleString += event.unicode
                elif typing and not over:
                    inp += event.unicode
                else:
                    if event.key == pg.K_f:
                        boolean = False
                        inpRender.update(inpRender.textParsed + " : F")
                    else:
                        boolean = True
                        inpRender.update(inpRender.textParsed + " : T")

    scr.fill((255,255,255))
    if not over:
        pg.draw.line(scr, Text.COLOR['black'], [(width // 2) - 100, 38], [(width // 2) + 100, 38], 2)
        pg.draw.line(scr, Text.COLOR['black'], [(width // 2) - 85, 44], [(width // 2) + 85, 44], 2)
        n += 1
        if n < 20:
            cursor.render()
        else:
            if n == 39:
                n = 0

    inpRender.render(scr)

    if inp != "" and inp != lastInp:
        lastInp = inp
        inpRender.update(inp)
    for cent in cents:
        cent.render(scr)
    for line in lines:
        line.render(scr)
    for end in ends:
        end.render(scr)
    for rule in rules:
        rule.render(scr)
    clock.tick(30)
    pg.display.update()
