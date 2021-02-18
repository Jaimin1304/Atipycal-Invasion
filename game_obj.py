import random
import pygame as pg
import data_storage as ds
from math import sqrt, pow, atan


class game_obj(object):

    def __init__(self, x, y, pic_path):
        """
        :param int x: initial x coor of object
        :param int y: initial y coor of object
        :param str pic_path: relative path of object picture
        """

        self.x = x
        self.y = y
        self.pic_path = pic_path
        self.img = pg.image.load(pic_path)

    def refresh(self):
        """
        Needs to be overridden by subclasses if necessary

        :param bool on_map: 
            if true, show pic on the game map, else, show pic on the screen. 
            A pic is on screen means it and the screen remain relatively still.
        """
        ds.screen.blit(self.img, [self.x, self.y])

    def get_rect(self):
        self.img_rect = self.img.get_rect()
        self.img_rect.topleft = [self.x, self.y]
        return self.img_rect


class player(game_obj):

    def __init__(self, x, y, pic_path, acc, x_spd, y_spd):
        """
        :param int x: initial x coor of player
        :param int y: initial y coor of player
        :param str pic_path: relative path of object picture
        :param float acc: the player's acceleration
        :param int x_spd: the speed of player in horizontal direction
        :param int y_spd: the speed of player in vertical direction
        """

        super().__init__(x, y, pic_path)
        self.img = pg.transform.smoothscale(self.img, (ds.player_wid, ds.player_hgt))
        self.acc = acc
        self.x_spd = x_spd
        self.y_spd = y_spd
        self.is_alive = True
        # The center coor of the player
        self.ctpos = [self.x + ds.player_wid/2, self.y + ds.player_hgt/2]
        # The collision radius of the player
        self.rad = sqrt(pow(ds.player_hgt/2, 2) + pow(ds.player_wid/2, 2))
        # Whether the corresponding key is pressed
        self.W = False
        self.A = False
        self.S = False
        self.D = False

    def adjust_scr_pos(self):
        """
        Adjust the screen's position on map according to position of player.
        """

        ds.scr_x = (self.x + ds.player_wid/2) - (ds.scr_wid/2)
        ds.scr_y = (self.y + ds.player_hgt/2) - (ds.scr_hgt/2)

        # If the screen touches the left end of map
        if ds.scr_x < 0:
            ds.scr_x = 0
        # If the screen touches the right end of map
        if ds.scr_x > ds.map_wid - ds.scr_wid:
            ds.scr_x = ds.map_wid - ds.scr_wid
        # If the screen touches the top end of map
        if ds.scr_y < 0:
            ds.scr_y = 0
        # If the screen touches the bottom end of map
        if ds.scr_y > ds.map_hgt - ds.scr_hgt:
            ds.scr_y = ds.map_hgt - ds.scr_hgt

    def key_response(self):
        """
        Handle the key input, adjust the img coor and its speed.

        :rtype: None
        """

        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.W = True
                if event.key == pg.K_a:
                    self.A = True
                if event.key == pg.K_s:
                    self.S = True
                if event.key == pg.K_d:
                    self.D = True
                if event.key == pg.K_p:
                    print("----------------------------")
                    print(self.x, self.y)
                    print(ds.scr_x, ds.scr_y)
                    print(self.x - ds.scr_x, self.y - ds.scr_y)
                    # print(self.x_corr_val, self.y_corr_val)
                    print(self.get_rect())
            elif event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    self.W = False
                if event.key == pg.K_a:
                    self.A = False
                if event.key == pg.K_s:
                    self.S = False
                if event.key == pg.K_d:
                    self.D = False

        if self.W:
            self.y_spd = self.y_spd - self.acc
        if self.A:
            self.x_spd = self.x_spd - self.acc
        if self.S:
            self.y_spd = self.y_spd + self.acc
        if self.D:
            self.x_spd = self.x_spd + self.acc

        self.x = self.x + self.x_spd
        self.y = self.y + self.y_spd

    def collide_detect(self, oth_game_obj):
        """
        Adjust player's coor if it collides with other objects.

        :return: Whether player collided with another game object
        :rtype: bool
        """
        collide = pg.Rect.colliderect(self.get_rect(), oth_game_obj.get_rect())

    def wall_detect(self):
        """
        Adjust player's coor if it collides with map boundary.

        :return: Whether enemy collided with map boundary
        :rtype: bool
        """
    
        # bounce off the wall if the collide
        if self.x < 0:
            self.x = 0 # to minimise error
            self.x_spd = -self.x_spd
        if self.x > ds.map_wid - ds.player_wid:
            self.x = ds.map_wid - ds.player_wid
            self.x_spd = -self.x_spd
        if self.y < 0:
            self.y = 0
            self.y_spd = - self.y_spd
        if self.y > ds.map_hgt - ds.player_hgt:
            self.y = ds.map_hgt - ds.player_hgt
            self.y_spd = -self.y_spd


    def rotate(self):
        """
        Adjust player's image when its direction changes.
        """
        self.new_img = self.img

        pg.draw.line(ds.screen,
                     [0, 255, 0],
                     self.ctpos,
                     [self.ctpos[0],
                     self.ctpos[1] + self.y_spd*20],
                     3)
        pg.draw.line(ds.screen,
                     [255, 0, 0],
                     self.ctpos,
                     [self.ctpos[0] + self.x_spd*20, (self.ctpos[1])],
                     3)

        if not self.y_spd == 0:

            tan = self.x_spd / self.y_spd
            angle = atan(tan) * 180 / ds.pi

            if self.y_spd > 0:
                self.new_img = pg.transform.rotate(self.img, angle + 180)
            else:
                self.new_img = pg.transform.rotate(self.img, angle)
        else:
            if self.x_spd > 0:
                self.new_img = pg.transform.rotate(self.img, -90)
            else:
                self.new_img = pg.transform.rotate(self.img, 90)

        self.x_corr_val = (self.new_img.get_rect().size[0] - ds.player_wid) / 2
        self.y_corr_val = (self.new_img.get_rect().size[1] - ds.player_hgt) / 2

    def refresh(self, on_map = True):
        """
        Adjust player's attributes of the next frame.
        """

        self.ctpos = [self.x + ds.player_wid/2 - ds.scr_x,
                      self.y + ds.player_hgt/2 - ds.scr_y]

        self.key_response()
        # self.collide_detect(self)
        self.out_detect()
        self.rotate()
        self.adjust_scr_pos()
        ds.screen.blit(self.new_img,
                       [self.x - self.x_corr_val - ds.scr_x, 
                       self.y - self.y_corr_val - ds.scr_y])


class enemy(game_obj):

    def __init__(self, x, y, pic_path, acc, vel_x, vel_y, dir):
        """
        :param int x: initial x coor of enemy
        :param int y: initial y coor of enemy
        :param str pic_path: relative path of object picture
        :param int acc: the determined acceleration for enemy object (no direction involved)
        :param int vel_x: the speed of enemy in vertical direction
        :param int vel_y: the speed of enemy in horizontal direction
        :param str dir: the direction of enemy given as input
        """

        self.acc = acc
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.dir = dir
        super().__init__(x, y, pic_path)

        self.is_alive = True

    def is_alive(self):
        """
        :return: Whether enemy is alive
        :rtype: boolean
        """
        return self.is_alive

    def detect_collide(self, oth_game_obj):
        """
        :return: Whether enemy collided with another game object
        :rtype: boolean
        """
        return pg.Rect.colliderect(self.get_rect(), oth_game_obj.get_rect())

    def detect_out(self):
        """
        :return: Whether enemy collided with the map wall
        :rtype: boolean
        """
        pass

    def refresh(self, on_map = True):
        """
        Adjust enemy's attributes of the next frame.
        """

        dir = random.choice(['a', 'd', 'w', 's'])

        if dir == 'a':
            # input of left given
            self.vel_x -= acc
            self.x += vel_x
            self.y += vel_y

        elif dir == 'd':
            # input of right given
            self.vel_x += acc
            self.x += vel_x
            self.y += vel_y

        elif dir == 'w':
            # input of up given
            self.vel_y += acc
            self.x += vel_x
            self.y += vel_y

        elif dir == 's':
            # input of down given
            self.vel_y -= acc
            self.x += vel_x
            self.y += vel_y


class tower(game_obj):

    def __init__(self, x, y, pic_path):
        """
        :param int x: initial x coor of tower
        :param int y: initial y coor of tower
        :param str pic_path: relative path of object picture
        """
        super().__init__(x, y, pic_path)


class picture(game_obj):

    def __init__(self, x, y, pic_path):
        """
        :param int x: initial x coor of picture
        :param int y: initial y coor of picture
        :param str pic_path: relative path of object picture
        """
        super().__init__(x, y, pic_path)
    
    def refresh(self, on_map = True):
        """
        :param bool on_map: 
            if true, show pic on the game map, else, show pic on the screen. 
            A pic is on screen means it and the screen remain relatively still.
        """
        if on_map:
            ds.screen.blit(self.img, [self.x - ds.scr_x, self.y - ds.scr_y])
        else:
            ds.screen.blit(self.img, [self.x, self.y])


class text(object):

    def __init__(self, font = 'consolas'):
        """
        Initialize the text's style.

        :param str font: The font string of text info
        """

        self.font = font
        self.bg_color = ds.black

    def write_txt(self, pos, size, color, info, on_map = True):
        """
        Display the text content on the screen.

        :param list pos: The list of [x,y] coor of text
        :param int size: The font size of text
        :param list color: The [r, g, b] color list of text info
        :param str info: Specific text content
        :param bool on_map: 
            if true, write text on the game map, else, write text on the screen. 
            A piece of text is on screen means it and the screen remain relatively 
            still.
        """

        self.pos = pos
        self.size = size
        self.color = color
        self.ft = pg.font.SysFont(self.font, size)
        text = self.ft.render(info, True, color)

        if on_map:
            ds.screen.blit(text, [pos[0] - ds.scr_x, pos[1] - ds.scr_y])
        else:
            ds.screen.blit(text, pos)