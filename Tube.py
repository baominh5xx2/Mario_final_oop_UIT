import pygame as pg
"""
    Lớp đại diện cho ống trong trò chơi.

    Thuộc tính
    ----------
    rect : pygame.Rect
        Hình chữ nhật đại diện cho vị trí và kích thước của ống.
    image : pygame.Surface
        Hình ảnh của ống.

    Phương thức
    ----------
    render(core):
        Hiển thị ống lên màn hình.
    """

class Tube(pg.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pg.image.load('images/tube.png').convert_alpha()
        length = (12 - y_pos) * 32
        self.image = self.image.subsurface(0, 0, 64, length)
        self.rect = pg.Rect(x_pos * 32, y_pos * 32, 64, length)

    def render(self, core):
        core.screen.blit(self.image, core.get_map().get_camera().apply(self))
