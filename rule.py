from text import Text
import math

class Rule():
    def __init__(self, text, line):
        symbols = {">": "→", "<": "↔", ".": "∨", ",": "∧", "-": "¬"}
        self.text = symbols[text[0:1]] + text[1:2].capitalize() + " på " + text[2:3]
        self.textRendered = Text(self.text, 'pink', False, False)
        if not line.split:
            self.pos = [line.startPos[0] + 8, line.startPos[1] + 8]
        else:
            v = math.atan(line.difference / 40)
            x = line.difference * 0.4
            self.pos = [line.startPos2[0] - 12 + int((math.tan(v) * 25)), line.startPos2[1] - 6]
    
    def render(self, scr):
        scr.blit(self.textRendered.text, self.pos)
