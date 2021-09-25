import pygame as pg
pg.init()

class Line():
    def __init__(self, split, startPos, scale):
        self.split = split
        if split:
            self.startPos1 = (startPos[0] - 20, startPos[1] + 6)
            self.startPos2 = (startPos[0] + 20, startPos[1] + 6)
            diffrence = scale * 25
            self.endPos1 = (self.startPos1[0] - diffrence, self.startPos1[1] + 40)
            self.endPos2 = (self.startPos2[0] + diffrence, self.startPos2[1] + 40)
        else:
            self.startPos = (startPos[0] + 1, startPos[1] + 6)
            self.endPos = (self.startPos[0], self.startPos[1] + 40)

    def render(self, scr):
        if not self.split:
            pg.draw.line(scr, (0, 0, 0), self.startPos, self.endPos, 1)
        else:
            pg.draw.aaline(scr, (0, 0, 0), self.startPos1, self.endPos1)
            pg.draw.aaline(scr, (0, 0, 0), self.startPos2, self.endPos2)
            # pg.draw.line(scr, (0, 0, 0), (self.startPos[0] - 20, self.startPos[1]), (self.startPos[0] - 50, self.startPos[1] + 40), 2)
            # pg.draw.line(scr, (0, 0, 0), (self.startPos[0] + 20, self.startPos[1]), (self.startPos[0] + 50, self.startPos[1] + 40), 2)
