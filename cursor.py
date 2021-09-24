
class Cursor():
    def __init__(self, pos, char, scr):
        self.pos = pos
        self.char = char
        self.realPos = [self.pos[0] - (self.char.get_width() // 2), self.pos[1]]
        self.scr = scr

    def render(self):
        self.scr.blit(self.char, self.pos)
