import pygame as pg

class Text(object):
    """
    Lớp Text đại diện cho văn bản hiển thị trong trò chơi.

    Thuộc tính:
        font (Font): Phông chữ của văn bản.
        text (Surface): Bề mặt chứa văn bản đã được vẽ.
        rect (Rect): Hình chữ nhật xác định vị trí và kích thước của văn bản.
        y_offset (int): Độ lệch theo trục y của văn bản.

    Phương thức:
        __init__(text, fontsize, rectcenter, font='Emulogic', textcolor=(255, 255, 255)):
            Khởi tạo đối tượng Text với văn bản, kích thước phông chữ, vị trí trung tâm, 
            phông chữ và màu văn bản.
        
        update(core):
            Cập nhật vị trí của văn bản và loại bỏ văn bản nếu đã di chuyển lên trên đủ xa.
        
        render(core):
            Vẽ văn bản lên màn hình chính.
        
        render_in_game(core):
            Vẽ văn bản lên màn hình trò chơi với áp dụng camera.
        
        get_rect():
            Trả về hình chữ nhật xác định vị trí và kích thước của văn bản.
    """

    def __init__(self, text, fontsize, rectcenter, font='Emulogic', textcolor=(255, 255, 255)):
        """
        Khởi tạo đối tượng Text với văn bản, kích thước phông chữ, vị trí trung tâm, 
        phông chữ và màu văn bản.

        Tham số:
            text (str): Văn bản cần hiển thị.
            fontsize (int): Kích thước phông chữ.
            rectcenter (tuple): Vị trí trung tâm của văn bản (x, y).
            font (str): Tên phông chữ (mặc định là 'Emulogic').
            textcolor (tuple): Màu văn bản (mặc định là màu trắng).
        """
        self.font = pg.font.Font('fonts/emulogic.ttf', fontsize)
        self.text = self.font.render(text, False, textcolor)
        self.rect = self.text.get_rect(center=rectcenter)
        self.y_offset = 0

    def update(self, core):
        """
        Cập nhật vị trí của văn bản và loại bỏ văn bản nếu đã di chuyển lên trên đủ xa.

        Tham số:
            core (Core): Đối tượng lõi của trò chơi.
        """
        self.rect.y -= 1
        self.y_offset -= 1

        if self.y_offset == -100:
            core.get_map().remove_text(self)

    def render(self, core):
        """
        Vẽ văn bản lên màn hình chính.

        Tham số:
            core (Core): Đối tượng lõi của trò chơi.
        """
        core.screen.blit(self.text, self.rect)

    def render_in_game(self, core):
        """
        Vẽ văn bản lên màn hình trò chơi với áp dụng camera.

        Tham số:
            core (Core): Đối tượng lõi của trò chơi.
        """
        core.screen.blit(self.text, core.get_map().get_camera().apply(self))

    def get_rect(self):
        """
        Trả về hình chữ nhật xác định vị trí và kích thước của văn bản.

        Trả về:
            Rect: Hình chữ nhật của văn bản.
        """
        return self.rect
