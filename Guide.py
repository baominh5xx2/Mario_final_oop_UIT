import pygame as pg
from Text import Text
from Const import *
"""
    Một lớp để quản lý hướng dẫn của trò chơi.

    Thuộc tính
    ----------
    screen : pygame.Surface
        Bề mặt hiển thị của hướng dẫn.
    is_showing : bool
        Trạng thái hiển thị của hướng dẫn.
    guide_text : list
        Danh sách các dòng văn bản hướng dẫn.
    texts : list
        Danh sách các đối tượng văn bản để hiển thị.
    guide_image : pygame.Surface
        Hình ảnh hướng dẫn.
    guide_image_rect : pygame.Rect
        Hình chữ nhật đại diện cho vị trí và kích thước của hình ảnh hướng dẫn.

    Phương thức
    ----------
    render(core):
        Hiển thị hướng dẫn lên màn hình.
    show(core):
        Hiển thị hướng dẫn và xử lý đầu vào từ người dùng.
    hide(core):
        Ẩn hướng dẫn.
    """
class Guide:
    def __init__(self, screen):
        self.screen = screen
        self.is_showing = False  # Flag to check the display state of the guide screen
        self.guide_text = [
            "Game Instructions:",
            "Left Arrow Key: Move Left",
            "Right Arrow Key: Move Right",
            "Up Arrow Key: Jump"
        ]
        self.texts = []
        y = 70
        for line in self.guide_text:
            text = Text(line, 20, (WINDOW_W / 2, y), font='Emulogic', textcolor=(0, 0, 0))
            self.texts.append(text)
            y += 50
        
        # Load the image
        self.guide_image = pg.image.load('images/menu.png').convert_alpha()
        
        # Scale the image to the size of the screen
        self.guide_image = pg.transform.scale(self.guide_image, (WINDOW_W, WINDOW_H))
        
        # Calculate the center position for the image
        self.guide_image_rect = self.guide_image.get_rect(center=(WINDOW_W / 2, WINDOW_H / 2))
        
        # Create a button to toggle sound
    def render(self, core):
        self.screen.fill((0, 0, 0))  # Black background
        self.screen.blit(self.guide_image, (0, 0))  # Draw the image to fit the entire screen
        for text in self.texts:
            text.render(core)
        pg.display.flip()

    def show(self, core):
        self.is_showing = True
        while self.is_showing:
            self.render(core)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_showing = False
                    core.run = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.is_showing = False
            core.clock.tick(60)
