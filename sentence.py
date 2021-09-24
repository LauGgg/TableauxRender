import pygame as pg

class Text():
    pg.init()
    FONT = pg.font.Font("seguisym.ttf", 18)
    # INDEXFONT = pg.font.Font("seguisym.ttf", 12)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

class Sentence(Text):
    def __init__(self, text, pos, index):
        self.text = text
        self.index = index
        self.textParsed = self.parse(text)
        print(self.textParsed)
        self.renderedText = self.FONT.render(self.textParsed, True, self.BLACK)
        self.renderedIndex = self.FONT.render(str(self.index), True, self.RED)
        self.pos = pos
        self.realPos = [self.pos[0] - (self.renderedText.get_width() / 2), pos[1]]

    def parse(self, text):
        # ∧	∨ ⬌ ⭢ ⭤	 ⮕	→ ↔ ⇾ ¬
        phrases = [">", "<", ".", ",", "-"]
        symbols = ["→", "↔", " ∨ ", " ∧ ", "¬"]
        newText = text

        for i, phrase in enumerate(phrases):
            newText = newText.replace(phrase, symbols[i])
            newText.replace(phrase, symbols[i])
        return newText
    
    def render(self, frame):
        frame.blit(self.renderedIndex, (self.realPos[0] - 20, self.realPos[1]))
        frame.blit(self.renderedText, self.realPos)
