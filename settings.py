import pygame as pg

WIDTH = 400
HEIGHT = 600


CHRISTMAS_TREE_NOTES = ["c4", "a4", "a4", "g4", "a4", "f4", "c4", "c4", "c4", "a4", "a4", "a-4", "g4", "c5",
                        "c5", "d4", "d4", "a-4", "a-4", "a4", "g4", "f4", "c4", "a4", "a4", "g4", "a4", "f4"]
CHRISTMAS_TREE_DURATION = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
                           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]

BIRCH_NOTES = ["a4", "a4", "a4", "a4", "g4", "f4", "f4", "e4", "d4",
               "a4", "a4", "c5", "a4", "g4", "g4", "f4", "f4", "e4", "d4",
               "e4", "f4", "g4", "f4", "f4", "e4", "d4",
               "e4", "f4", "g4", "f4", "f4", "e4", "d4"]
BIRCH_DURATION = [1, 1, 1, 1, 2, 1, 1, 2, 2,
                  1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
                  2, 1, 2, 1, 1, 2, 2,
                  2, 1, 2, 1, 1, 2, 2]

MORNING_NOTES = ["c5", "a4", "g4", "f4", "g4", "a4", "c5", "a4", "f4", "g4", "a4", "g4", "a4", "c5", "a4",
                 "c5", "d5", "a4", "d5", "c5", "a4", "f4", "c4", "a3", "g3", "f3", ]
MORNING_DURATION = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

# LINES -->
NUMBER_OF_LINES = 3
DISTANCE_BETWEEN_LINES = 100

# TILES -->
LONG_TILE = pg.image.load("pianotiles/long_tile.png")
LONG_TILE = pg.transform.scale(LONG_TILE, [DISTANCE_BETWEEN_LINES, DISTANCE_BETWEEN_LINES * 2.7])

LONG_TILE_PRESSED = pg.image.load("pianotiles/long_tile_pressed.png")
LONG_TILE_PRESSED = pg.transform.scale(LONG_TILE_PRESSED, [DISTANCE_BETWEEN_LINES, DISTANCE_BETWEEN_LINES * 2.7])

SHORT_TILE = pg.image.load("pianotiles/short_tile.png")
SHORT_TILE = pg.transform.scale(SHORT_TILE, [DISTANCE_BETWEEN_LINES, DISTANCE_BETWEEN_LINES * 1.7])

SHORT_TILE_PRESSED = pg.image.load("pianotiles/short_tile_pressed.png")
SHORT_TILE_PRESSED = pg.transform.scale(SHORT_TILE_PRESSED, [DISTANCE_BETWEEN_LINES, DISTANCE_BETWEEN_LINES * 1.7])

# SPEED -->
SPEED_Y = 6

MENU = pg.image.load("pianotiles/menu.jpg")
MENU = pg.transform.scale(MENU, [WIDTH, HEIGHT])
