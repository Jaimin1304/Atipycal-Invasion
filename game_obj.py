import random
import pygame as pg
import data_storage as ds
from math import sqrt, pow, atan

class game_obj(object):

    def __init__(self, x, y, pic_path):
        """
        :param int x: inital x position of object
        :param int y: inital y position of object
        :param str pic_path: relative path of object picture
        """

        self.x = x
        self.y = y
        self.pic_path = pic_path

    def refresh(self):
        """
        Needs to be overridden by subclasses
        """
        pass


class player(game_obj):

    def __init__(self, x, y, pic_path, acc, x_spd, y_spd):
        """
        :param int x: inital x position of player
        :param int y: inital y position of player
        :param str pic_path: relative path of object picture
        :param int acc: the determined acceleration for player object
        :param int x_spd: the speed of player in horizontal direction
        :param int y_spd: the speed of player in vertical direction
        """

        super().__init__(x, y, pic_path)
        self.img = pg.image.load(pic_path)
        self.img = pg.transform.smoothscale(self.img, (ds.player_wid, ds.player_hgt))
        self.acc = acc
        self.x_spd = x_spd
        self.y_spd = y_spd
        self.W = False
        self.A = False
        self.S = False
        self.D = False
        self.is_alive = True

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

    def collide_detect(self):
        """
        Adjust player's coor if it collides with other objects.

        :return: Whether player collided with another game object
        :rtype: boolean
        """
        pass

    def out_detect(self):
        """
        Adjust player's coor if it collides with map boundary.

        :return: Whether enemy collided with map boundary
        :rtype: boolean
        """
        pass

    def rotate(self):
        """
        Adjust player's image when its direction changes.
        """
        self.new_img = self.img
        #pg.draw.line(screen, [0, 255, 0], self.ctpos, [self.ctpos[0], self.ctpos[1]-self.y_spd*20], laser_width)
        #pg.draw.line(screen, [255, 0, 0], self.ctpos, [self.ctpos[0]+self.x_spd*20, (self.ctpos[1])], laser_width)
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

    def refresh(self):
        """
        Determine the attributes of player on the next frame.
        """

        self.key_response()
        self.collide_detect()
        self.out_detect()
        self.rotate()
        ds.screen.blit(self.new_img, [self.x - self.x_corr_val, self.y - self.y_corr_val])


class enemy(game_obj):

    def __init__(self, x, y, pic_path, acc, vel_x, vel_y, dir):
        """
        :param int x: inital x position of enemy
        :param int y: inital y position of enemy
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
        pass

    def detect_out(self, oth_game_obj):
        """
        :return: Whether enemy collided with another game object
        :rtype: boolean
        """
        pass

    def refresh(self):
        """
        Determine the attributes of enemy on the next frame

        :param str dir: a randomly generated direction
            'a' -> left,
            'd' -> right,
            'w' -> up,
            's' -> down
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
        :param int x: inital x position of tower
        :param int y: inital y position of tower
        :param str pic_path: relative path of object picture
        """
        super().__init__(x, y, pic_path)


class picture(game_obj):

    def __init__(self, x, y, pic_path):
        """
        :param int x: inital x position of picture
        :param int y: inital y position of picture
        :param str pic_path: relative path of object picture
        """
        super().__init__(x, y, pic_path)


class text(game_obj):

    def __init__(self, x, y, info):
        """
        :param int x: inital x position of picture
        :param int y: inital y position of picture
        :param str pic_path: relative path of object picture
        """
        super().__init__(x, y, font_path)