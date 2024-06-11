import pygame as pg

from Const import *
from Text import Text

class MainMenu(object):
    """
    Lớp MainMenu đại diện cho menu chính của trò chơi, bao gồm hình nền, 
    hình ảnh bổ sung và các tùy chọn văn bản.

    Thuộc tính:
        mainImage (Surface): Hình nền cho menu chính.
        additionalImage (Surface): Hình ảnh bổ sung hiển thị trong menu chính.
        additionalImage_rect (Rect): Hình chữ nhật để định vị hình ảnh bổ sung.
        texts (list): Danh sách các đối tượng Text cho các tùy chọn menu.

    Phương thức:
        __init__():
            Khởi tạo MainMenu bằng cách tải và thay đổi kích thước hình ảnh, 
            tạo các đối tượng văn bản và đặt vị trí của chúng.
        
        update(core):
            Cập nhật trạng thái của menu chính.
        
        render(core):
            Vẽ menu chính lên màn hình.
        
        get_option_rects():
            Trả về danh sách các hình chữ nhật tương ứng với từng tùy chọn menu.
        
        get_option_at_pos(pos):
            Trả về chỉ số của tùy chọn tại vị trí được cung cấp.
    """

    def __init__(self):
        """
        Khởi tạo MainMenu bằng cách tải và thay đổi kích thước hình ảnh, 
        tạo các đối tượng văn bản và đặt vị trí của chúng.
        """
        # Tải hình nền
        self.mainImage = pg.image.load(r'images/menu.png').convert_alpha()
        
        # Thay đổi kích thước hình nền để phù hợp với toàn màn hình
        self.mainImage = pg.transform.scale(self.mainImage, (WINDOW_W, WINDOW_H))
        
        # Tải hình ảnh bổ sung
        self.additionalImage = pg.image.load(r'images/mario_bro.png').convert_alpha()
        
        # Thay đổi kích thước hình ảnh bổ sung theo kích thước mong muốn (ví dụ: 300x200 pixel)
        self.additionalImage = pg.transform.scale(self.additionalImage, (300, 200))
        
        # Tính toán vị trí trung tâm cho hình ảnh bổ sung
        self.additionalImage_rect = self.additionalImage.get_rect(center=((WINDOW_W / 2), (WINDOW_H / 2) * 0.65))
        
        # Khởi tạo các đối tượng văn bản
        self.texts = []

        # Tạo các đối tượng văn bản với vị trí trung tâm
        self.texts.append(Text('  PLAY GAME', 16, ((WINDOW_W / 2), (WINDOW_H / 2) + 40), textcolor=(0, 0, 0)))
        self.texts.append(Text('  Guide', 16, ((WINDOW_W / 2), (WINDOW_H / 2) + 60), textcolor=(0, 0, 0)))
        self.texts.append(Text('  EXIT', 16, ((WINDOW_W / 2), (WINDOW_H / 2) + 80), textcolor=(0, 0, 0)))

    def update(self, core):
        """
        Cập nhật trạng thái của menu chính.

        Tham số:
            core (Core): Đối tượng lõi của trò chơi.
        """
        pass

    def render(self, core):
        """
        Vẽ menu chính lên màn hình.

        Tham số:
            core (Core): Đối tượng lõi của trò chơi.
        """
        # Vẽ hình nền để phù hợp với toàn màn hình
        core.screen.blit(self.mainImage, (0, 0))
        
        # Vẽ hình ảnh bổ sung ở trung tâm màn hình
        core.screen.blit(self.additionalImage, self.additionalImage_rect.topleft)
        
        # Vẽ từng văn bản
        for text in self.texts:
            text.render(core)
        
        # Cập nhật hiển thị
        pg.display.flip()

    def get_option_rects(self):
        """
        Trả về danh sách các hình chữ nhật tương ứng với từng tùy chọn menu.

        Trả về:
            list: Danh sách các hình chữ nhật của các tùy chọn menu.
        """
        return [text.get_rect() for text in self.texts]

    def get_option_at_pos(self, pos):
        """
        Trả về chỉ số của tùy chọn tại vị trí được cung cấp.

        Tham số:
            pos (tuple): Vị trí cần kiểm tra (x, y).

        Trả về:
            int: Chỉ số của tùy chọn tại vị trí đã cho, hoặc -1 nếu không có tùy chọn nào tại vị trí đó.
        """
        for i, text in enumerate(self.texts):
            if text.get_rect().collidepoint(pos):
                return i
        return -1
