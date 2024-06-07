import pygame as pg
from Text import Text
from Const import WINDOW_W, WINDOW_H
"""
    Lớp để quản lý menu kết thúc trò chơi.

    Thuộc tính
    ----------
    screen : pygame.Surface
        Bề mặt hiển thị của menu kết thúc trò chơi.
    font : pygame.font.Font
        Font chữ của menu kết thúc trò chơi.
    text : pygame.Surface
        Văn bản hiển thị trên menu kết thúc trò chơi.
    text_rect : pygame.Rect
        Hình chữ nhật đại diện cho vị trí và kích thước của văn bản.

    Phương thức
    ----------
    render():
        Hiển thị menu kết thúc trò chơi lên màn hình.
    """
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
