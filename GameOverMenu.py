import pygame as pg
from Text import Text
from Const import WINDOW_W, WINDOW_H

class GameOverMenu:
    def __init__(self, core):
        self.core = core
        self.text = Text('Game Over', 32, (WINDOW_W // 2, WINDOW_H // 2))

        self.display_time = 2000  
        self.start_time = None

    def start(self):
        self.start_time = pg.time.get_ticks()

    def update(self, core):
        if pg.time.get_ticks() - self.start_time > self.display_time:
            core.reset_to_menu()

    def render(self, core):
        core.screen.fill((0, 0, 0))
        self.text.render(core)
        pg.display.flip()
