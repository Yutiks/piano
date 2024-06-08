import pygame as pg
import pygame.freetype
import settings


class Tile:
    def __init__(self, x, y, tile_length, name_of_tile, clicked, num):
        if tile_length == 1:
            self.image = settings.SHORT_TILE
        if tile_length == 2:
            self.image = settings.LONG_TILE
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = pg.Rect([x, y], [width, height])
        self.speed_y = settings.SPEED_Y
        self.name = name_of_tile
        self.length = tile_length
        self.sound = pg.mixer.Sound(f"pianotiles/Sounds/{name_of_tile}.ogg")
        self.clicked = clicked
        self.pressed_times = 0
        self.text = pg.freetype.Font("pianotiles/font.ttf", 25)
        self.num = num

    def paint(self, window, coordinate):
        window.blit(self.image, self.rect)
        self.text.render_to(window, coordinate, self.name, [255, 255, 255])

    def movement(self):
        self.rect.y += self.speed_y

    def click(self):
        if self.clicked == 0:
            self.image = settings.SHORT_TILE_PRESSED if self.length == 1 else settings.LONG_TILE_PRESSED
            self.sound.play()
            self.clicked = 1
