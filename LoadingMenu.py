import pygame as pg

from Const import *
from Text import Text

class LoadingMenu(object):
    """
    Lớp LoadingMenu đại diện cho màn hình tải của trò chơi, hiển thị thông tin 
    về thế giới hiện tại và điều khiển trạng thái tải.

    Thuộc tính:
        iTime (int): Thời gian bắt đầu tải.
        loadingType (bool): Loại tải (True cho tải vào game, False cho tải về menu chính).
        bg (Surface): Bề mặt nền của màn hình tải.
        text (Text): Đối tượng văn bản hiển thị tên thế giới.

    Phương thức:
        __init__(core):
            Khởi tạo LoadingMenu bằng cách thiết lập thời gian tải, loại tải, 
            tạo nền và đối tượng văn bản.
        
        update(core):
            Cập nhật trạng thái của màn hình tải dựa trên thời gian hiện tại.
        
        set_text_and_type(text, type, fontsize=32):
            Đặt lại văn bản và loại tải.
        
        render(core):
            Vẽ màn hình tải lên màn hình chính.
        
        update_time():
            Cập nhật lại thời gian bắt đầu tải.
    """
    
    def __init__(self, core):
        self.iTime = pg.time.get_ticks()
        self.loadingType = True
        self.bg = pg.Surface((WINDOW_W, WINDOW_H))
        self.text = Text('WORLD ' + core.oWorld.get_name(), 32, (WINDOW_W / 2, WINDOW_H / 2))

    def update(self, core): 
        if pg.time.get_ticks() >= self.iTime + (5250 if not self.loadingType else 2500):
            if self.loadingType:
                core.oMM.currentGameState = 'Game'
                core.get_sound().play('overworld', 999999, 0.5)
                core.get_map().in_event = False
            else:
                core.oMM.currentGameState = 'MainMenu'
                self.set_text_and_type('WORLD ' + core.oWorld.get_name(), True)
                core.get_map().reset(True)

    def set_text_and_type(self, text, type, fontsize=32):
        self.text = Text(text, fontsize, (WINDOW_W / 2, WINDOW_H / 2))
        self.loadingType = type

    def render(self, core):
        core.screen.blit(self.bg, (0, 0))
        self.text.render(core)

    def update_time(self):
        self.iTime = pg.time.get_ticks()
