import pygame as pg

class Text():
    pg.init()
    FONT = pg.font.Font("seguisym.ttf", 18)
    # INDEXFONT = pg.font.Font("seguisym.ttf", 12)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)

class Sentence(Text):
    def __init__(self, text, pos, index, boolean):
        self.textParsed = self.parse(text)
        self.index = index
        self.boolean = boolean
        self.pos = pos
        if text != "":
            if self.isElemental(text):
                color = self.BLUE
            else:
                color = self.BLACK
            if boolean:
                self.renderedText = self.FONT.render(self.textParsed + " : T", True, color)
            else:
                self.renderedText = self.FONT.render(self.textParsed + " : F", True, color)
            self.realPos = [self.pos[0] - (self.renderedText.get_width() // 2), self.pos[1]]
        else:
            self.renderedText = self.FONT.render(" ", True, self.BLACK)
            self.realPos = [self.pos[0], self.pos[1]]
        if index:
            self.renderedIndex = self.FONT.render(str(self.index), True, self.RED)

    def update(self, newText):
        self.textParsed = self.parse(newText)
        self.renderedText = self.FONT.render(self.textParsed, True, self.BLACK)
        self.realPos = [self.pos[0] - (self.renderedText.get_width() // 2), self.pos[1]]
    
    def isElemental(self, text):
        phrases = [">", "<", ".", ",", "-"]
        symbols = [" → ", " ↔ ", " ∨ ", " ∧ ", "¬"]
        if any(i in phrases for i in text):
            return False
        else:
            return True

    def parse(self, text):
        phrases = [">", "<", ".", ",", "-"]
        symbols = ["→", "↔", " ∨ ", " ∧ ", "¬"]
        newText = text
        for i, phrase in enumerate(phrases):
            newText = newText.replace(phrase, symbols[i])
        return newText
    
    def render(self, scr):
        if self.index:
            scr.blit(self.renderedIndex, (self.realPos[0] - 20, self.realPos[1]))
        scr.blit(self.renderedText, self.realPos)
