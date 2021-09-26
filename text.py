import pygame as pg
pg.init()

class Text():
    FONT_LG = pg.font.Font("seguisym.ttf", 18)
    FONT_SM = pg.font.Font("seguisym.ttf", 14)
    COLOR = {'black': (0, 0, 0), 'blue': (0, 0, 255), 'red': (255, 0, 0), 'pink': (255, 80, 180)}
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    PINK = (255, 113, 194)

    def __init__(self, text, color, large, parse):
        text = text
        if parse:
            text = self.parse(text)
        if large:
            self.text = self.FONT_LG.render(text, True, self.COLOR[color])
        else:
            self.text = self.FONT_SM.render(text, True, self.COLOR[color])
        self.width = self.text.get_width()
    
    def parse(self, text):
        phrases = [">", "<", ".", ",", "-"]
        symbols = ["→", "↔", " ∨ ", " ∧ ", "¬"]
        newText = text
        for i, phrase in enumerate(phrases):
            newText = newText.replace(phrase, symbols[i])
        return newText
