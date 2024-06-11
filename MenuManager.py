import pygame as pg
from LoadingMenu import LoadingMenu
from MainMenu import MainMenu
from GameOverMenu import GameOverMenu

class MenuManager(object):
    """
    Lớp MenuManager cho phép quản lý trạng thái trò chơi một cách dễ dàng. 
    Tùy thuộc vào tình huống, nó sẽ cập nhật và vẽ các thành phần khác nhau.

    Thuộc tính:
        currentGameState (str): Trạng thái hiện tại của trò chơi.
        oMainMenu (MainMenu): Đối tượng MainMenu.
        oLoadingMenu (LoadingMenu): Đối tượng LoadingMenu.
        oGameOverMenu (GameOverMenu): Đối tượng GameOverMenu.

    Phương thức:
        __init__(core):
            Khởi tạo MenuManager với các menu và trạng thái hiện tại là 'MainMenu'.
        
        update(core):
            Cập nhật trạng thái hiện tại của trò chơi.
        
        render(core):
            Vẽ các thành phần tương ứng với trạng thái hiện tại của trò chơi.
        
        handle_event(event, core):
            Xử lý các sự kiện đầu vào dựa trên trạng thái hiện tại của trò chơi.
        
        start_loading():
            Bắt đầu quá trình tải cấp độ.
    """

    def __init__(self, core):
        self.currentGameState = 'MainMenu'
        self.oMainMenu = MainMenu()
        self.oLoadingMenu = LoadingMenu(core)
        self.oGameOverMenu = GameOverMenu(core)

    def update(self, core):
        """
        Cập nhật trạng thái hiện tại của trò chơi.

        Tham số:
            core (Core): Đối tượng lõi của trò chơi.
        """
        if self.currentGameState == 'MainMenu':
            self.oMainMenu.update(core)
        elif self.currentGameState == 'Loading':
            self.oLoadingMenu.update(core)
        elif self.currentGameState == 'Game':
            core.get_map().update(core)
        elif self.currentGameState == 'GameOver':
            self.oGameOverMenu.update(core)

    def render(self, core):
        """
        Vẽ các thành phần tương ứng với trạng thái hiện tại của trò chơi.

        Tham số:
            core (Core): Đối tượng lõi của trò chơi.
        """
        if self.currentGameState == 'MainMenu':
            core.get_map().render_map(core)
            self.oMainMenu.render(core)
        elif self.currentGameState == 'Loading':
            self.oLoadingMenu.render(core)
        elif self.currentGameState == 'Game':
            core.get_map().render(core)
            core.get_map().get_ui().render(core)
        elif self.currentGameState == 'GameOver':
            self.oGameOverMenu.render(core)
        pg.display.update()

    def handle_event(self, event, core):
        """
        Xử lý các sự kiện đầu vào dựa trên trạng thái hiện tại của trò chơi.

        Tham số:
            event (Event): Sự kiện cần xử lý.
            core (Core): Đối tượng lõi của trò chơi.
        """
        if self.currentGameState == 'MainMenu':
            self.oMainMenu.handle_event(event, core)

    def start_loading(self):
        """
        Bắt đầu quá trình tải cấp độ.
        """
        self.currentGameState = 'Loading'
        self.oLoadingMenu.update_time()
