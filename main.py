import pygame as pg
import random
import settings
import tile
import pygame.freetype
import menu

pg.init()
pg.mixer.init()
pg.mixer.set_num_channels(30)


class Game:
    def __init__(self):
        self.b = 1
        self.window = pg.display.set_mode([settings.WIDTH, settings.HEIGHT])
        self.tile_fit_distance = 0
        self.tile_fit = settings.WIDTH // settings.DISTANCE_BETWEEN_LINES
        self.choice = []
        for tale_f in range(self.tile_fit):
            self.choice.append(self.tile_fit_distance)
            self.tile_fit_distance += settings.DISTANCE_BETWEEN_LINES
        self.tale_spawn = pg.USEREVENT
        pg.time.set_timer(self.tale_spawn, 500)
        self.tiles = []
        self.clock = pg.time.Clock()
        self.number = 0
        self.text = pg.freetype.Font("pianotiles/font.ttf", 25)
        self.pressed_times = 0
        self.selected = settings.CHRISTMAS_TREE_NOTES
        self.result = 0
        self.result_text = ""
        self.menu = menu.Menu(self)
        self.menu_game = 1

    def events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.b -= 1
            if event.type == self.tale_spawn and len(self.selected) > self.number and self.result == 0:
                tile_1 = tile.Tile(random.choice(self.choice), -270, 1, self.selected[self.number], 0, self.number)
                self.tiles.append(tile_1)
                self.number += 1
            if event.type == pg.MOUSEBUTTONDOWN:
                for tile_ in self.tiles:
                    if tile_.rect.collidepoint(event.pos) and not tile_.clicked:
                        tile_.click()
                        if self.pressed_times < tile_.num:
                            self.result = 1
                            self.result_text = "Game over"
                        self.pressed_times += 1
                if self.result == 1:
                    self.menu_game = 1

    def paint(self):
        self.window.fill([255, 255, 255])
        text_to_render = str(f"{self.pressed_times}-{len(self.selected)}")
        distance = settings.DISTANCE_BETWEEN_LINES
        for line in range(settings.NUMBER_OF_LINES):
            pg.draw.line(self.window, [255, 0, 0], [distance, 0], [distance, settings.HEIGHT])
            distance += settings.DISTANCE_BETWEEN_LINES
        if self.result == 0:
            for tile_p in self.tiles:
                tile_p.paint(self.window, tile_p.rect.center)
        if self.result == 1:
            self.text.render_to(self.window, [150, settings.HEIGHT // 2], self.result_text, [0, 0, 255])
        self.text.render_to(self.window, [settings.WIDTH - 100, 10], text_to_render, [0, 0, 255])

    def movement(self):
        tile_1 = None
        if self.result == 0:
            for tile_1 in self.tiles:
                tile_1.movement()
                if tile_1.rect.y > 600 and not tile_1.clicked:
                    self.result = 1
                    self.result_text = "Game over"
            if self.pressed_times == len(self.selected) and tile_1.rect.y > 600:
                self.result = 1
                self.result_text = "GG win"

    def start(self):
        while self.b == 1:
            if self.menu_game == 0:
                self.paint()
                self.events()
                self.movement()
            else:
                self.menu.paint()
                self.menu.movement()
                self.menu.events()
            pg.display.update()
            self.clock.tick(80)


game = Game()
game.start()
