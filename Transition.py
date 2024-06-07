import pygame as pg
"""
    Lớp để quản lý hiệu ứng chuyển cảnh trong trò chơi.

    Thuộc tính
    ----------
    screen : pygame.Surface
        Bề mặt hiển thị của hiệu ứng chuyển cảnh.
    is_fading_in : bool
        Trạng thái của hiệu ứng chuyển cảnh vào.
    is_fading_out : bool
        Trạng thái của hiệu ứng chuyển cảnh ra.
    fade_alpha : int
        Mức độ trong suốt của hiệu ứng chuyển cảnh.

    Phương thức
    ----------
    start_fade_in():
        Bắt đầu hiệu ứng chuyển cảnh vào.
    start_fade_out():
        Bắt đầu hiệu ứng chuyển cảnh ra.
    update():
        Cập nhật trạng thái của hiệu ứng chuyển cảnh.
    render():
        Hiển thị hiệu ứng chuyển cảnh lên màn hình.
    """
class Transition:
    def __init__(self, screen):
        self.screen = screen
        self.alpha = 255
        self.transitioning = False
        self.fade_in = True
        self.fade_out = False
        self.transition_complete = False

    def start_fade_in(self):
        self.transitioning = True
        self.fade_in = True
        self.fade_out = False
        self.alpha = 255

    def start_fade_out(self):
        self.transitioning = True
        self.fade_in = False
        self.fade_out = True
        self.alpha = 0

    def update(self):
        if self.transitioning:
            if self.fade_in:
                self.alpha -= 5
                if self.alpha <= 0:
                    self.alpha = 0
                    self.transitioning = False
                    self.transition_complete = True
            elif self.fade_out:
                self.alpha += 5
                if self.alpha >= 255:
                    self.alpha = 255
                    self.transitioning = False
                    self.transition_complete = True

    def render(self):
        if self.transitioning or self.transition_complete:
            fade_surface = pg.Surface((self.screen.get_width(), self.screen.get_height()))
            fade_surface.fill((0, 0, 0))
            fade_surface.set_alpha(self.alpha)
            self.screen.blit(fade_surface, (0, 0))
