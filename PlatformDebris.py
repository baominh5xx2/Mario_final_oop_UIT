import pygame as pg

from Const import *
"""
    Lớp đại diện cho các mảnh vỡ của nền tảng trong trò chơi.

    Thuộc tính
    ----------
    rect : pygame.Rect
        Hình chữ nhật đại diện cho vị trí và kích thước của mảnh vỡ.
    image : pygame.Surface
        Hình ảnh của mảnh vỡ.
    x_vel : float
        Vận tốc theo trục x của mảnh vỡ.
    y_vel : float
        Vận tốc theo trục y của mảnh vỡ.

    Phương thức
    ----------
    update(core):
        Cập nhật trạng thái của mảnh vỡ.
    render(core):
        Hiển thị mảnh vỡ lên màn hình.
    """

class PlatformDebris(object):
    def __init__(self, x_pos, y_pos):
        self.image = pg.image.load('images/block_debris0.png').convert_alpha()

        # 4 different parts
        self.rectangles = [
            pg.Rect(x_pos - 20, y_pos + 16, 16, 16),
            pg.Rect(x_pos - 20, y_pos - 16, 16, 16),
            pg.Rect(x_pos + 20, y_pos + 16, 16, 16),
            pg.Rect(x_pos + 20, y_pos - 16, 16, 16)
        ]
        self.y_vel = -4
        self.rect = None

    def update(self, core):
        self.y_vel += GRAVITY * FALL_MULTIPLIER

        for i in range(len(self.rectangles)):
            self.rectangles[i].y += self.y_vel
            if i < 2:
                self.rectangles[i].x -= 1
            else:
                self.rectangles[i].x += 1

        if self.rectangles[1].y > core.get_map().mapSize[1] * 32:
            core.get_map().debris.remove(self)

    def render(self, core):
        for rect in self.rectangles:
            self.rect = rect
            core.screen.blit(self.image, core.get_map().get_camera().apply(self))
