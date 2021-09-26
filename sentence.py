from text import Text

class Sentence(Text):
    def __init__(self, text, pos, index, boolean):
        self.index = index
        self.boolean = boolean
        self.pos = pos
        if text != "":
            if self.isElemental(text):
                color = 'blue'
            else:
                color = 'black'
            if boolean:
                self.renderedText = Text(text + " : T", color, True, True)
            else:
                self.renderedText = Text(text + " : F", color, True, True)
            self.realPos = [self.pos[0] - (self.renderedText.width // 2), self.pos[1]]
        else:
            self.renderedText = Text(" ", 'black', True, False)
            self.realPos = [self.pos[0], self.pos[1]]
        if index:
            self.renderedIndex = Text(str(self.index), 'red', True, False)

    def update(self, newText):
        self.textParsed = self.parse(newText)
        self.renderedText = Text(self.textParsed, 'black', True, False)
        self.realPos = [self.pos[0] - (self.renderedText.width // 2), self.pos[1]]
    
    def isElemental(self, text):
        phrases = [">", "<", ".", ",", "-"]
        symbols = [" → ", " ↔ ", " ∨ ", " ∧ ", "¬"]
        if any(i in phrases for i in text):
            return False
        else:
            return True
    
    def render(self, scr):
        if self.index:
            scr.blit(self.renderedIndex.text, (self.realPos[0] - 20, self.realPos[1]))
        scr.blit(self.renderedText.text, self.realPos)
