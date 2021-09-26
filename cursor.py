
class Cursor():
    def __init__(self, pos, char, scr):
        self.char = char
        self.pos = [pos[0] - (self.char.width // 2), pos[1]]
        self.scr = scr

    def update(self, pos):
        self.pos = [pos[0] - (self.char.width // 2), pos[1]]

    def render(self):
        self.scr.blit(self.char.text, self.pos)
