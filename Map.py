import pygame as pg
from pytmx.util_pygame import load_pygame

from GameUI import GameUI
from BGObject import BGObject
from Camera import Camera
from Event import Event
from Flag import Flag
from Const import *
from Platform import Platform
from Player import Player
from Goombas import Goombas
from Mushroom import Mushroom
from Flower import Flower
from Koopa import Koopa
from Tube import Tube
from PlatformDebris import PlatformDebris
from CoinDebris import CoinDebris
from Text import Text
from Goombas_1 import Goombas_1

class Map(object):
    """
    This class contains every map object: tiles, mobs and player. Also,
    there are camera, event and UI.
    """

    def __init__(self, world_num):
        self.obj = []
        self.obj_bg = []
        self.tubes = []
        self.debris = []
        self.mobs = []
        self.mobs_1 = []
        self.projectiles = []
        self.text_objects = []
        self.koopa = []
        self.map = 0
        self.flag = None

        self.mapSize = (0, 0)
        self.sky = 0

        self.textures = {}
        self.worldNum = world_num
        self.load_world()

        self.is_mob_spawned = [False, False]
        self.score_for_killing_mob = 100
        self.score_time = 0

        self.in_event = False
        self.tick = 0
        self.time = 400

        self.oPlayer = Player(x_pos=128, y_pos=351)
        self.oCamera = Camera(self.mapSize[0] * 32, 14)
        self.oEvent = Event()
        self.oGameUI = GameUI()

    def load_world(self):
        if self.worldNum == '1-1':
            self.loadWorld_11()
        elif self.worldNum == '1-2':
            self.loadWorld_12()
        elif self.worldNum == '1-3':
            self.loadWorld_13()

    def loadWorld_11(self):
        tmx_data = load_pygame("worlds/1-1/W11.tmx")
        self.mapSize = (tmx_data.width, tmx_data.height)

        self.sky = pg.Surface((WINDOW_W, WINDOW_H))
        self.sky.fill((pg.Color('#5c94fc')))

        # 2D List
        self.map = [[0] * tmx_data.height for i in range(tmx_data.width)]

        layer_num = 0
        for layer in tmx_data.visible_layers:
            for y in range(tmx_data.height):
                for x in range(tmx_data.width):

                    # Getting pygame surface
                    image = tmx_data.get_tile_image(x, y, layer_num)

                    # It's none if there are no tile in that place
                    if image is not None:
                        tileID = tmx_data.get_tile_gid(x, y, layer_num)

                        if layer.name == 'Foreground':

                            # 22 ID is a question block, so in taht case we shoud load all it's images
                            if tileID == 22:
                                image = (
                                    image,                                      # 1
                                    tmx_data.get_tile_image(0, 15, layer_num),   # 2
                                    tmx_data.get_tile_image(1, 15, layer_num),   # 3
                                    tmx_data.get_tile_image(2, 15, layer_num)    # activated
                                )

                            # Map class has 1)"map" list, which is used in collision system because we can
                            # easily get block by x and y coordinate 2)"obj", "obj_bg" and simular arrays -
                            # they are used in rendering because you don't need to cycle through every
                            # (x, y) pair. Here we are adding the same platform object in 2 different arrays.
                            self.map[x][y] = Platform(x * tmx_data.tileheight, y * tmx_data.tilewidth, image, tileID)
                            self.obj.append(self.map[x][y])

                        elif layer.name == 'Background':
                            self.map[x][y] = BGObject(x * tmx_data.tileheight, y * tmx_data.tilewidth, image)
                            self.obj_bg.append(self.map[x][y])
            layer_num += 1


        self.spawn_tube(28, 10)
        self.spawn_tube(37, 9)
        self.spawn_tube(46, 8)
        self.spawn_tube(55, 8)
        self.spawn_tube(163, 10)
        self.spawn_tube(179, 10)

        self.mobs.append(Goombas(736, 352, False))
        self.mobs.append(Goombas(1295, 352, True))
        self.mobs.append(Goombas(1632, 352, False))
        self.mobs.append(Goombas(1672, 352, False))
        self.mobs.append(Goombas(5570, 352, False))
        self.mobs.append(Goombas(5620, 352, False))

        self.map[21][8].bonus = 'mushroom'
        self.map[78][8].bonus = 'mushroom'
        self.map[109][4].bonus = 'mushroom'

        self.flag = Flag(6336, 48)

    def loadWorld_12(self):
        tmx_data = load_pygame("worlds/1-2/W12.tmx")
        self.mapSize = (tmx_data.width, tmx_data.height)

        self.sky = pg.Surface((WINDOW_W, WINDOW_H))
        self.sky.fill((pg.Color('#5c94fc')))

        # 2D List
        self.map = [[0] * tmx_data.height for i in range(tmx_data.width)]

        layer_num = 0
        for layer in tmx_data.visible_layers:
            for y in range(tmx_data.height):
                for x in range(tmx_data.width):

                    # Getting pygame surface
                    image = tmx_data.get_tile_image(x, y, layer_num)

                    # It's none if there are no tile in that place
                    if image is not None:
                        tileID = tmx_data.get_tile_gid(x, y, layer_num)

                        if layer.name == 'Foreground':

                            # 22 ID is a question block, so in taht case we shoud load all it's images
                            if tileID == 22:
                                image = (
                                    image,                                      # 1
                                    tmx_data.get_tile_image(0, 15, layer_num),   # 2
                                    tmx_data.get_tile_image(1, 15, layer_num),   # 3
                                    tmx_data.get_tile_image(2, 15, layer_num)    # activated
                                )

                            # Map class has 1)"map" list, which is used in collision system because we can
                            # easily get block by x and y coordinate 2)"obj", "obj_bg" and simular arrays -
                            # they are used in rendering because you don't need to cycle through every
                            # (x, y) pair. Here we are adding the same platform object in 2 different arrays.
                            self.map[x][y] = Platform(x * tmx_data.tileheight, y * tmx_data.tilewidth, image, tileID)
                            self.obj.append(self.map[x][y])

                        elif layer.name == 'Background':
                            self.map[x][y] = BGObject(x * tmx_data.tileheight, y * tmx_data.tilewidth, image)
                            self.obj_bg.append(self.map[x][y])
            layer_num += 1

        self.spawn_tube(14,8)
        self.spawn_tube(28,8)
        self.spawn_tube(34,6)
        self.spawn_tube(151,8)
        self.spawn_tube(160,8)
        self.spawn_tube(167,4)

        self.spawn_goombas(608,352, False)
        self.spawn_goombas(630,352, True)
        self.spawn_goombas(650,352, False)
        self.spawn_goombas(680,352, True)
        self.spawn_goombas(700,352, True)
        self.spawn_goombas(960,352, True)
        self.spawn_goombas(1000,352, True)
        self.spawn_goombas(2400,160, False)
        self.spawn_goombas(2350, 160, False)
        self.spawn_goombas(2300,160, False)
        self.spawn_goombas(2200,160, False)
        self.spawn_goombas(2150,160, False)
        self.spawn_goombas(2100,160, False)
        self.spawn_goombas(2050,160, False)
        self.spawn_goombas(2000,160, False)
        self.spawn_goombas(4864,352, True)
        self.spawn_goombas(4900,352, False)


        self.spawn_koopa(750,352,True)
        self.spawn_koopa(4950,352, False)


        self.map[21][8].bonus = 'mushroom'
        self.map[56][2].bonus = 'mushroom'
        self.map[95][4].bonus = 'mushroom'
        self.map[109][4].bonus = 'mushroom'

        self.flag = Flag(6336, 48)

    def loadWorld_13(self):
        tmx_data = load_pygame("worlds/1-3/W13.tmx")
        self.mapSize = (tmx_data.width, tmx_data.height)

        self.sky = pg.Surface((WINDOW_W, WINDOW_H))
        self.sky.fill((pg.Color('#000000')))

        self.map = [[0] * tmx_data.height for i in range(tmx_data.width)]

        layer_num = 0
        for layer in tmx_data.visible_layers:
            for y in range(tmx_data.height):
                for x in range(tmx_data.width):
                    image = tmx_data.get_tile_image(x, y, layer_num)
                    if image is not None:
                        tileID = tmx_data.get_tile_gid(x, y, layer_num)
                        if layer.name == 'Foreground':
                            if tileID == 22:
                                image = (
                                    image,
                                    tmx_data.get_tile_image(0, 15, layer_num),
                                    tmx_data.get_tile_image(1, 15, layer_num),
                                    tmx_data.get_tile_image(2, 15, layer_num)
                                )
                            self.map[x][y] = Platform(x * tmx_data.tileheight, y * tmx_data.tilewidth, image, tileID)
                            self.obj.append(self.map[x][y])
                        elif layer.name == 'Background':
                            self.map[x][y] = BGObject(x * tmx_data.tileheight, y * tmx_data.tilewidth, image)
                            self.obj_bg.append(self.map[x][y])
            layer_num += 1

        self.spawn_tube(33,4)
        self.spawn_tube(100,5)
        self.spawn_tube(115,5)

        self.spawn_goombas_1(37*32+30,11*32,True)
        self.spawn_goombas_1(37*32+60,11*32,True)
        self.spawn_goombas_1(37*32+90,11*32,True)
        self.spawn_goombas_1(37*32+120,11*32,True)
        self.spawn_goombas_1(37*32+150,11*32,True)
        self.spawn_goombas_1(37*32+180,11*32,True)
        self.spawn_goombas_1(37*32+210,11*32,True)
        self.spawn_goombas_1(37*32+240,11*32,True)
        self.spawn_goombas_1(37*32+270,11*32,True)
        self.spawn_goombas_1(37*32+300,11*32,True)
        self.spawn_goombas_1(37*32+330,11*32,True)
        self.spawn_goombas_1(37*32+360,11*32,True)
        self.spawn_goombas_1(37*32+390,11*32,True)
        self.spawn_goombas_1(37*32+420,11*32,True)
        self.spawn_goombas_1(37*32+470,11*32,True)

        self.spawn_koopa(84*32,11*32,True)
        self.spawn_koopa(84*32+40,11*32,True)
        self.spawn_koopa(84*32-30,11*32,True)
        self.spawn_koopa(84*32+80,11*32,True)
        self.spawn_koopa(84*32+123,11*32,True)
        self.spawn_koopa(84*32+200,11*32,False)


        self.map[21][8].bonus = 'mushroom'
        self.map[56][2].bonus = 'mushroom'
        

        
        self.flag = Flag(6336, 48)

    def reset(self, reset_all):
        self.obj = []
        self.obj_bg = []
        self.tubes = []
        self.debris = []
        self.mobs = []
        self.is_mob_spawned = [False, False]

        self.in_event = False
        self.flag = None
        self.sky = None
        self.map = None

        self.tick = 0
        self.time = 400

        self.mapSize = (0, 0)
        self.textures = {}
        self.load_world()

        self.get_event().reset()
        self.get_player().reset(reset_all)
        self.get_camera().reset()

    def get_name(self):
        return self.worldNum

    def get_player(self):
        return self.oPlayer

    def get_camera(self):
        return self.oCamera

    def get_event(self):
        return self.oEvent

    def get_ui(self):
        return self.oGameUI

    def get_blocks_for_collision(self, x, y):
        """
        Returns tiles around the entity
        """


        return (
            self.map[x][y - 1],
            self.map[x][y + 1],
            self.map[x][y],
            self.map[x - 1][y],
            self.map[x + 1][y],
            self.map[x + 2][y],
            self.map[x + 1][y - 1],
            self.map[x + 1][y + 1],
            self.map[x][y + 2],
            self.map[x + 1][y + 2],
            self.map[x - 1][y + 1],
            self.map[x + 2][y + 1],
            self.map[x][y + 3],
            self.map[x + 1][y + 3]
        )

    def get_blocks_below(self, x, y):
        """
        Returns 2 blocks below entity to check its on_ground parameter
        """
        return (
            self.map[x][y + 1],
            self.map[x + 1][y + 1]
        )

    def get_mobs(self):
        return self.mobs
    def get_mobs_1(self):
        return self.mobs_1

    def spawn_tube(self, x_coord, y_coord):
        self.tubes.append(Tube(x_coord, y_coord))
        for y in range(y_coord, 12): # 12 because it's ground level.
            for x in range(x_coord, x_coord + 2):
                self.map[x][y] = Platform(x * 32, y * 32, image=None, type_id=0)

    def spawn_mushroom(self, x, y):
        self.get_mobs().append(Mushroom(x, y, True))

    def spawn_goombas(self, x, y, move_direction):
        self.get_mobs().append(Goombas(x, y, move_direction))
    def spawn_goombas_1(self, x, y, move_direction):
        self.get_mobs().append(Goombas_1(x, y, move_direction))

    def spawn_koopa(self, x, y, move_direction):
        self.get_mobs().append(Koopa(x, y, move_direction))

    def spawn_flower(self, x, y):
        self.mobs.append(Flower(x, y))

    def spawn_debris(self, x, y, type):
        if type == 0:
            self.debris.append(PlatformDebris(x, y))
        elif type == 1:
            self.debris.append(CoinDebris(x, y))

    def spawn_score_text(self, x, y, score=None):
        """
        This text appears when you, for example, kill a mob. It shows how many points
        you got.
        """
        if score is None:
            self.text_objects.append(Text(str(self.score_for_killing_mob), 16, (x, y)))
            self.score_time = pg.time.get_ticks()
            if self.score_for_killing_mob < 1600:
                self.score_for_killing_mob *= 2
        else:
            self.text_objects.append(Text(str(score), 16, (x, y)))

    def remove_object(self, object):
        self.obj.remove(object)
        self.map[object.rect.x // 32][object.rect.y // 32] = 0

    def remove_whizbang(self, whizbang):
        self.projectiles.remove(whizbang)

    def remove_text(self, text_object):
        self.text_objects.remove(text_object)

    def update_player(self, core):
        self.get_player().update(core)

    def update_entities(self, core):
        for mob in self.mobs:
            mob.update(core)
            if not self.in_event:
                self.entity_collisions(core)

        if self.worldNum == '1-2': 
            if self.get_player().rect.x > 2080 and not self.is_mob_spawned[0]:
                self.spawn_goombas(2495, 224, False)
                self.spawn_goombas(2560, 96, False)
                self.is_mob_spawned[0] = True

            elif self.get_player().rect.x > 2460 and not self.is_mob_spawned[1]:
                self.spawn_goombas(3200, 352, False)
                self.spawn_goombas(3250, 352, False)
                self.spawn_koopa(3400, 352, False)
                self.spawn_goombas(3700, 352, False)
                self.spawn_goombas(3750, 352, False)
                self.spawn_goombas(4060, 352, False)
                self.spawn_goombas(4110, 352, False)
                self.spawn_goombas(4190, 352, False)
                self.spawn_goombas(4240, 352, False)
                self.is_mob_spawned[1] = True

    def update_time(self, core):
        """
        Updating a map time.
        """
        if not self.in_event:
            self.tick += 1
            if self.tick % 40 == 0:
                self.time -= 1
                self.tick = 0
            if self.time == 100 and self.tick == 1:
                core.get_sound().start_fast_music(core)
            elif self.time == 0:
                self.player_death(core)

    def update_score_time(self):
        """
        When player kill mobs in a row, score for each mob
        will increase. When player stops kill mobs, points
        will reset to 100. This function updates these points.
        """
        if self.score_for_killing_mob != 100:
            if pg.time.get_ticks() > self.score_time + 750:
                self.score_for_killing_mob //= 2

    def entity_collisions(self, core):
        if not core.get_map().get_player().unkillable:
            for mob in self.mobs:
                mob.check_collision_with_player(core)
    def player_death(self, core):
        self.in_event = True
        self.get_player().reset_jump()
        self.get_player().reset_move()
        self.get_player().numOfLives -= 1

        if self.get_player().numOfLives == 0:
            self.get_event().start_kill(core, game_over=True)
        else:
            self.get_event().start_kill(core, game_over=False)

    def player_win(self, core):
        self.in_event = True
        self.get_player().reset_jump()
        self.get_player().reset_move()
        self.get_event().start_win(core)

    def update(self, core):
        self.update_entities(core)

        if not core.get_map().in_event:
            if self.get_player().inLevelUpAnimation:
                self.get_player().change_powerlvl_animation()
            elif self.get_player().inLevelDownAnimation:
                self.get_player().change_powerlvl_animation()
                self.update_player(core)
            else:
                self.update_player(core)
        else:
            self.get_event().update(core)

        for debris in self.debris:
            debris.update(core)

        for whizbang in self.projectiles:
            whizbang.update(core)

        for text_object in self.text_objects:
            text_object.update(core)

        if not self.in_event:
            self.get_camera().update(core.get_map().get_player().rect)

        self.update_time(core)
        self.update_score_time()
    def player_death(self, core):
        self.in_event = True
        self.get_player().reset_jump()
        self.get_player().reset_move()
        self.get_player().numOfLives -= 1
        self.get_player().score = 0  # Reset the player's score

        if self.get_player().numOfLives == 0:
            self.get_event().start_kill(core, game_over=True)
        else:
            self.get_event().start_kill(core, game_over=False)
    def render_map(self, core):
        """
        Rendering only tiles. It's used in main menu.
        """
        core.screen.blit(self.sky, (0, 0))

        for obj_group in (self.obj_bg, self.obj):
            for obj in obj_group:
                obj.render(core)

        for tube in self.tubes:
            tube.render(core)

    def render(self, core):
        """
        Renders every object.
        """
        core.screen.blit(self.sky, (0, 0))

        for obj in self.obj_bg:
            obj.render(core)

        for mob in self.mobs:
            mob.render(core)

        for obj in self.obj:
            obj.render(core)

        for tube in self.tubes:
            tube.render(core)

        for whizbang in self.projectiles:
            whizbang.render(core)

        for debris in self.debris:
            debris.render(core)

        self.flag.render(core)

        for text_object in self.text_objects:
            text_object.render_in_game(core)

        self.get_player().render(core)

        self.get_ui().render(core)

