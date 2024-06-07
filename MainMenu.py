import pygame as pg

from Const import *
from Text import Text
"""
    Lớp để quản lý menu chính của trò chơi.

    Thuộc tính
    ----------
    screen : pygame.Surface
        Bề mặt hiển thị của menu chính.
    font : pygame.font.Font
        Font chữ của menu chính.
    options : list
        Danh sách các tùy chọn trong menu chính.
    selected_option : int
        Tùy chọn hiện đang được chọn.

    Phương thức
    ----------
    render():
        Hiển thị menu chính lên màn hình.
    navigate(direction):
        Điều hướng qua các tùy chọn trong menu chính.
    select():
        Chọn tùy chọn hiện tại.
    """
class MainMenu(object):
    def __init__(self):
        # Load the background image
        self.mainImage = pg.image.load(r'images/menu.png').convert_alpha()
        
        # Scale the background image to fit the entire screen
        self.mainImage = pg.transform.scale(self.mainImage, (WINDOW_W, WINDOW_H))
        
        # Load the additional image
        self.additionalImage = pg.image.load(r'images/mario_bro.png').convert_alpha()
        
        # Scale the additional image to desired size (e.g., 200x200 pixels)
        self.additionalImage = pg.transform.scale(self.additionalImage, (300, 200))
        
        # Calculate the center position for the additional image
        self.additionalImage_rect = self.additionalImage.get_rect(center=((WINDOW_W / 2), (WINDOW_H / 2)*0.65))
        
        # Initialize the text objects
        self.texts = []

        # Create text objects with centered positions
        self.texts.append(Text('1  PLAY GAME', 16, ((WINDOW_W / 2), (WINDOW_H / 2) + 40), textcolor=(0, 0, 0)))
        self.texts.append(Text('2  OPTIONS', 16, ((WINDOW_W / 2), (WINDOW_H / 2) + 60), textcolor=(0, 0, 0)))
        self.texts.append(Text('3  EXIT', 16, ((WINDOW_W / 2), (WINDOW_H / 2) + 80), textcolor=(0, 0, 0)))

    def update(self, core):
        pass

    def render(self, core):
        # Draw the background image to fit the entire screen
        core.screen.blit(self.mainImage, (0, 0))
        
        # Draw the additional image at the center of the screen
        core.screen.blit(self.additionalImage, self.additionalImage_rect.topleft)
        
        # Render each text
        for text in self.texts:
            text.render(core)
        
        # Update the display
        pg.display.flip()
