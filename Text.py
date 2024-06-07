import pygame as pg
"""
    Lớp để quản lý văn bản trong trò chơi.

    Thuộc tính
    ----------
    text : str
        Văn bản cần hiển thị.
    size : int
        Kích thước của font chữ.
    position : tuple
        Vị trí của văn bản.
    font : str
        Font chữ của văn bản.
    textcolor : tuple
        Màu sắc của văn bản.
    font : pygame.font.Font
        Đối tượng font chữ của pygame.
    surface : pygame.Surface
        Bề mặt hiển thị của văn bản.
    rect : pygame.Rect
        Hình chữ nhật đại diện cho vị trí và kích thước của văn bản.

    Phương thức
    ----------
    render(core):
        Hiển thị văn bản lên màn hình.
    render_in_game(core):
        Hiển thị văn bản lên màn hình trong trò chơi.
    """
class Text(object):
    def __init__(self, text, fontsize, rectcenter, font='Emulogic', textcolor=(255, 255, 255)):
        self.font = pg.font.Font('fonts/emulogic.ttf', fontsize)
        self.text = self.font.render(text, False, textcolor)
        self.rect = self.text.get_rect(center=rectcenter)
        self.y_offset = 0

    def update(self, core):
        self.rect.y -= 1
        self.y_offset -= 1

        if self.y_offset == -100:
            core.get_map().remove_text(self)

    def render(self, core):
        core.screen.blit(self.text, self.rect)

    def render_in_game(self, core):
        core.screen.blit(self.text, core.get_map().get_camera().apply(self))
