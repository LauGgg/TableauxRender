
class End():
    def __init__(self, char, pos):
        self.char = char
        self.pos = (pos[0] - (char.width // 2), pos[1])
    
    def render(self, scr):
        scr.blit(self.char.text, self.pos)
