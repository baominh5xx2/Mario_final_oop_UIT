import pygame as pg
"""
    Một lớp đại diện cho các đối tượng nền trong trò chơi.

    Thuộc tính
    ----------
    rect : pygame.Rect
        Hình chữ nhật đại diện cho vị trí và kích thước của đối tượng nền.
    image : pygame.Surface
        Hình ảnh sẽ được hiển thị cho đối tượng nền.
    type : str
        Loại của đối tượng, mặc định là 'BGObject'.

    Phương thức
    ----------
    render(core):
        Hiển thị đối tượng nền lên màn hình.
    """

class BGObject(object):
    def __init__(self, x, y, image):
        self.rect = pg.Rect(x, y, 32, 32)
        self.image = image
        self.type = 'BGObject'

    def render(self, core):
        core.screen.blit(self.image, core.get_map().get_camera().apply(self))
