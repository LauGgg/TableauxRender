import pygame as pg

class Text():
    pg.init()
    FONT = pg.font.Font("seguisym.ttf", 18)
    # INDEXFONT = pg.font.Font("seguisym.ttf", 12)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

class Sentence(Text):
    def __init__(self, text, pos, index):
        self.textParsed = self.parse(text)
        self.renderedText = self.FONT.render(self.textParsed, True, self.BLACK)
        self.index = index
        if index:
            self.renderedIndex = self.FONT.render(str(self.index), True, self.RED)
        self.pos = pos
        self.realPos = [self.pos[0] - (self.renderedText.get_width() // 2), self.pos[1]]

    def update(self, newText):
        self.textParsed = self.parse(newText)
        self.renderedText = self.FONT.render(self.textParsed, True, self.BLACK)
        self.realPos = [self.pos[0] - (self.renderedText.get_width() // 2), self.pos[1]]

    def parse(self, text):
        phrases = [">", "<", ".", ",", "-"]
        symbols = ["→", "↔", " ∨ ", " ∧ ", "¬"]
        newText = text
        for i, phrase in enumerate(phrases):
            newText = newText.replace(phrase, symbols[i])
            newText.replace(phrase, symbols[i])
        return newText
    
    def render(self, scr):
        if self.index:
            scr.blit(self.renderedIndex, (self.realPos[0] - 20, self.realPos[1]))
        scr.blit(self.renderedText, self.realPos)
