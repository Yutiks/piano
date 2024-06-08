import settings as sett
import pygame as pg
import pygame.freetype


class Menu:
    def __init__(self, game):
        self.game = game
        self.font = pg.freetype.Font("pianotiles/font.ttf", 25)
        self.options_colors = {0: [0, 255, 0], 1: [255, 255, 255], 2: [255, 255, 255]}
        self.melody = {0: sett.CHRISTMAS_TREE_NOTES, 1: sett.MORNING_NOTES, 2: sett.BIRCH_NOTES}
        self.choice = 0

    def paint(self):
        self.game.window.blit(sett.MENU, [0, 0])
        self.font.render_to(self.game.window, [60, 200], "CHRISTMAS TREE", self.options_colors[0])
        self.font.render_to(self.game.window, [130, 300], "MORNING", self.options_colors[1])
        self.font.render_to(self.game.window, [150, 400], "BIRCH", self.options_colors[2])

    def events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.game.b -= 1
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and self.choice > 0:
                    self.choice -= 1
                elif event.key == pg.K_DOWN and self.choice < 2:
                    self.choice += 1
                if event.key == pg.K_RETURN:
                    self.game.result = 0
                    self.game.tiles = []
                    self.game.number = 0
                    self.game.pressed_times = 0
                    self.game.menu_game = 0
            for option in range(3):
                if self.choice == option:
                    self.options_colors[option] = [0, 255, 0]
                    self.game.selected = self.melody[option]
                else:
                    self.options_colors[option] = [255, 255, 255]

    def movement(self):
        pass
