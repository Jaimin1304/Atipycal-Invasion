import random
import pygame as pg
import config as cf
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
        cf.screen.blit(self.img, [self.x, self.y])

    def get_rect(self):
        self.img_rect = self.img.get_rect()
        self.img_rect.topleft = [self.x, self.y]
        return self.img_rect


class player(game_obj):

    def __init__(self, x, y, pic_path, acc, x_spd, y_spd):
        """
        :param int x: initial x coor of player on the map
        :param int y: initial y coor of player on the map
        :param str pic_path: relative path of object picture
        :param float acc: the player's acceleration
        :param int x_spd: the speed of player in horizontal direction
        :param int y_spd: the speed of player in vertical direction
        """
        super().__init__(x, y, pic_path)
        self.img = pg.transform.smoothscale(self.img, (cf.player_wid, cf.player_hgt))
        self.acc = acc
        self.x_spd = x_spd
        self.y_spd = y_spd
        self.is_alive = True
        # The center coor of the player
        self.ctpos = [self.x + cf.player_wid/2, self.y + cf.player_hgt/2]
        # The collision radius of the player
        self.rad = sqrt(pow(cf.player_hgt/2, 2) + pow(cf.player_wid/2, 2))
        self.engine_on = False
        # The player's speed limit
        self.spd_lim = cf.player_spd_lim
        self.txt = text()

    def adjust_scr_pos(self):
        """
        Adjust the screen's position on map according to position of player.
        """
        cf.scr_x = (self.x + cf.player_wid/2) - (cf.scr_wid/2)
        cf.scr_y = (self.y + cf.player_hgt/2) - (cf.scr_hgt/2)

    def event_esponse(self):
        """
        Handle the key input, adjust the img coor and its speed.
        :rtype: None
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    print("----------------------------")
                    print(self.x, self.y)
                    print(cf.scr_x, cf.scr_y)
                    print(self.x - cf.scr_x, self.y - cf.scr_y)
                    # print(self.x_corr_val, self.y_corr_val)
                    print(self.get_rect())
            elif event.type == pg.KEYUP:
                print('keyup')
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                #print('buttonup')
                self.engine_on = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                #print('buttondown')
                self.engine_on = True

        if self.engine_on:
            mx, my = pg.mouse.get_pos() # [0]->x [1]->y
            ctr_x = cf.scr_wid/2
            ctr_y = cf.scr_hgt/2
            dis_x = mx-ctr_x
            dis_y = my-ctr_y
            dis = sqrt(dis_x**2+dis_y**2)
            acc_x = dis_x*(self.acc/dis)
            acc_y = dis_y*(self.acc/dis)
            self.x_spd = self.x_spd + acc_x
            self.y_spd = self.y_spd + acc_y
        self.x = self.x + self.x_spd
        self.y = self.y + self.y_spd
        # Ensure that the player does not surpass the speed limit
        if pow(self.x_spd, 2) + pow(self.y_spd, 2) > pow(self.spd_lim, 2):
            spd = sqrt(pow(self.x_spd, 2) + pow(self.y_spd, 2))
            self.x_spd = (self.spd_lim/spd) * self.x_spd
            self.y_spd = (self.spd_lim/spd) * self.y_spd

    def collide_detect(self, oth_game_obj):
        """
        Adjust player's coor if it collides with other objects.
        :return: Whether player collided with another game object
        :rtype: bool
        """
        collide = pg.Rect.colliderect(self.get_rect(), oth_game_obj.get_rect())

    def out_detect(self):
        """
        Adjust player's coor if it collides with map boundary.
        :return: Whether enemy collided with map boundary
        :rtype: bool
        """
        # bounce off the wall if the collide
        if self.x < 0:
            self.x = 0 # to minimise error
            self.x_spd = -self.x_spd
        if self.x > cf.map_wid - cf.player_wid:
            self.x = cf.map_wid - cf.player_wid
            self.x_spd = -self.x_spd
        if self.y < 0:
            self.y = 0
            self.y_spd = -self.y_spd
        if self.y > cf.map_hgt - cf.player_hgt:
            self.y = cf.map_hgt - cf.player_hgt
            self.y_spd = -self.y_spd

    def rotate(self):
        """
        Adjust player's image when its direction changes.
        """
        self.new_img = self.img
        pg.draw.line(cf.screen,
                     [0, 255, 0],
                     self.ctpos,
                     [self.ctpos[0],
                     self.ctpos[1] + self.y_spd*20],
                     3)
        pg.draw.line(cf.screen,
                     [255, 0, 0],
                     self.ctpos,
                     [self.ctpos[0] + self.x_spd*20, (self.ctpos[1])],
                     3)

        mx, my = pg.mouse.get_pos() # [0]->x [1]->y
        ctr_x = cf.scr_wid/2
        ctr_y = cf.scr_hgt/2

        if not (ctr_x-mx) == 0:
            tan = (ctr_y-my)/(mx-ctr_x)
            angle = atan(tan) * 180 / cf.pi
            if (ctr_x-mx) > 0:
                self.new_img = pg.transform.rotate(self.img, angle+90)
            else:
                self.new_img = pg.transform.rotate(self.img, angle-90)
        else:
            if (ctr_y-my) > 0:
                self.new_img = pg.transform.rotate(self.img, 0)
            else:
                self.new_img = pg.transform.rotate(self.img, 180)
        self.x_corr_val = (self.new_img.get_rect().size[0] - cf.player_wid) / 2
        self.y_corr_val = (self.new_img.get_rect().size[1] - cf.player_hgt) / 2

    def refresh(self, on_map = True):
        """
        Adjust player's attributes of the next frame.
        """
        #print(pg.mouse.get_pos())
        self.ctpos = [self.x + cf.player_wid/2 - cf.scr_x,
                      self.y + cf.player_hgt/2 - cf.scr_y]
        self.event_esponse()
        # self.collide_detect(self)
        self.out_detect()
        self.rotate()
        self.adjust_scr_pos()
        new_x = self.x-self.x_corr_val-cf.scr_x
        new_y = self.y-self.y_corr_val-cf.scr_y
        self.txt.write_txt([cf.scr_wid/2-30, cf.scr_hgt/2-50], 20, [255, 255, 255], "player1", False)
        cf.screen.blit(self.new_img, [new_x, new_y])


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


class star(game_obj):

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
            cf.screen.blit(self.img, [self.x - cf.scr_x, self.y - cf.scr_y])
        else:
            cf.screen.blit(self.img, [self.x, self.y])


class text(object):

    def __init__(self, font = 'consolas'):
        """
        Initialize the text's style.
        :param str font: The font string of text info
        """
        self.font = font
        self.bg_color = cf.black

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
            cf.screen.blit(text, [pos[0] - cf.scr_x, pos[1] - cf.scr_y])
        else:
            cf.screen.blit(text, pos)