from os import environ
import pygame as pg
from pygame.locals import *
from Const import *
from Map import Map
from MenuManager import MenuManager
from Sound import Sound
from Transition import Transition
from Guide import Guide
"""
    Lớp chính của trò chơi.

    Thuộc tính
    ----------
    screen : pygame.Surface
        Bề mặt hiển thị của trò chơi.
    clock : pygame.time.Clock
        Đồng hồ để kiểm soát tốc độ khung hình của trò chơi.
    worlds : list
        Danh sách các thế giới trong trò chơi.
    current_world_index : int
        Chỉ số của thế giới hiện tại.
    oWorld : Map
        Bản đồ của thế giới hiện tại.
    oSound : Sound
        Đối tượng âm thanh của trò chơi.
    oMM : MenuManager
        Quản lý menu của trò chơi.
    transition : Transition
        Hiệu ứng chuyển cảnh.
    guide : Guide
        Hướng dẫn trò chơi.
    run : bool
        Trạng thái chạy của trò chơi.
    keyR : bool
        Trạng thái phím mũi tên phải.
    keyL : bool
        Trạng thái phím mũi tên trái.
    keyU : bool
        Trạng thái phím mũi tên lên.
    keyD : bool
        Trạng thái phím mũi tên xuống.
    keyShift : bool
        Trạng thái phím Shift.
    keySpace : bool
        Trạng thái phím Space.
    total_score : int
        Tổng điểm của người chơi.

    Phương thức
    ----------
    main_loop():
        Vòng lặp chính của trò chơi.
    input():
        Xử lý đầu vào từ người chơi.
    input_player():
        Xử lý đầu vào khi ở trạng thái trò chơi.
    input_menu():
        Xử lý đầu vào khi ở trạng thái menu.
    update():
        Cập nhật trạng thái của trò chơi.
    render():
        Hiển thị trò chơi lên màn hình.
    get_map():
        Trả về bản đồ hiện tại.
    get_mm():
        Trả về quản lý menu.
    get_sound():
        Trả về đối tượng âm thanh.
    load_next_map():
        Tải bản đồ tiếp theo.
    reset_to_menu():
        Đặt lại trò chơi về menu chính.
    start_game():
        Bắt đầu trò chơi.
    show_map_message():
        Hiển thị thông báo bản đồ hiện tại.
    show_guide():
        Hiển thị hướng dẫn.
    hide_guide():
        Ẩn hướng dẫn.
    """
class Core(object):
    """
    Main class.
    """
    def __init__(self, world_num='1-2'):
        environ['SDL_VIDEO_CENTERED'] = '1'
        pg.mixer.pre_init(44100, -16, 2, 1024)
        pg.init()
        pg.display.set_caption('Mario Game')
        pg.display.set_mode((WINDOW_W, WINDOW_H))

        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))
        self.clock = pg.time.Clock()

        self.worlds = ['1-1', '1-2', '1-3']
        self.current_world_index = self.worlds.index(world_num)
        self.oWorld = Map(self.worlds[self.current_world_index])
        self.oSound = Sound()
        self.oMM = MenuManager(self)
        self.transition = Transition(self.screen)
        self.guide = Guide(self.screen)

        self.run = True
        self.keyR = False
        self.keyL = False
        self.keyU = False
        self.keyD = False
        self.keyShift = False
        self.keySpace = False

        self.total_score = 0

    def main_loop(self):
        self.transition.start_fade_in()
        while self.run:
            self.input()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def input(self):
        if self.get_mm().currentGameState == 'Game':
            self.input_player()
        else:
            self.input_menu()

    def input_player(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.transition.start_fade_out()
                self.run = False
            elif e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    self.keyR = True
                elif e.key == K_LEFT:
                    self.keyL = True
                elif e.key == K_DOWN:
                    self.keyD = True
                elif e.key == K_UP:
                    self.keyU = True
                elif e.key == K_LSHIFT:
                    self.keyShift = True
                elif e.key == K_SPACE:
                    self.keySpace = True
            elif e.type == KEYUP:
                if e.key == K_RIGHT:
                    self.keyR = False
                elif e.key == K_LEFT:
                    self.keyL = False
                elif e.key == K_DOWN:
                    self.keyD = False
                elif e.key == K_UP:
                    self.keyU = False
                elif e.key == K_LSHIFT:
                    self.keyShift = False
                elif e.key == K_SPACE:
                    self.keySpace = False

    def input_menu(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.transition.start_fade_out()
                self.run = False
            elif e.type == KEYDOWN:
                if e.key == K_1:
                    self.start_game()
                elif e.key == K_2:
                    self.show_guide()
                elif e.key == K_3:
                    self.run = False

    def update(self):
        self.get_mm().update(self)
        self.transition.update()

    def render(self):
        self.get_mm().render(self)
        self.transition.render()

    def get_map(self):
        return self.oWorld

    def get_mm(self):
        return self.oMM

    def get_sound(self):
        return self.oSound

    def load_next_map(self):
        self.total_score += self.oWorld.get_player().score
        self.current_world_index += 1
        if self.current_world_index < len(self.worlds):
            self.oWorld = Map(self.worlds[self.current_world_index])
            self.show_map_message()
            self.get_sound().play('overworld', 9999999, 0.5)
            self.transition.start_fade_in()
        else:
            self.get_mm().currentGameState = 'Loading'
            self.get_mm().oLoadingMenu.set_text_and_type(f'I hope you enjoyed. Total Score: {self.total_score}', False, 24)
            self.get_mm().oLoadingMenu.update_time()
            self.get_sound().play('game_over', 0, 0.5)

    def reset_to_menu(self):
        self.total_score = 0
        self.current_world_index = 0
        self.oMM.currentGameState = 'MainMenu'
        self.transition.start_fade_in()
        self.get_sound().play('game_over', 0, 0.5)

    def start_game(self):
        self.total_score = 0
        self.current_world_index = 0
        self.oWorld = Map(self.worlds[self.current_world_index])
        self.oMM.currentGameState = 'Game'
        self.transition.start_fade_in()
        self.show_map_message()
        self.get_sound().play('overworld', 9999999, 0.5)

    def show_map_message(self):
        self.screen.fill((0, 0, 0))
        font = pg.font.Font(None, 74)
        text = font.render(f'Map {self.worlds[self.current_world_index]}', True, (255, 255, 255))
        text_rect = text.get_rect(center=(WINDOW_W/2, WINDOW_H/2))
        self.screen.blit(text, text_rect)
        pg.display.flip()
        pg.time.wait(2000)

    def show_guide(self):
        self.guide.show(self)

    def hide_guide(self):
        self.guide.hide(self)

# Entry point for the game
if __name__ == "__main__":
    core = Core(world_num='1-2')
    core.main_loop()
