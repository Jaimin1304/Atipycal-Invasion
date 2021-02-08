import random

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

    def change_status(self):
        """
        Needs to be overridden by subclasses
        """
        pass


class player(game_obj):

    def __init__(self, x, y, pic_path, acc, vel_x, vel_y, dir):
        """
        :param int x: inital x position of player
        :param int y: inital y position of player
        :param str pic_path: relative path of object picture
        :param int acc: the determined acceleration for player object (no direction involved)
        :param int vel_x: the speed of player in vertical direction
        :param int vel_y: the speed of player in horizontal direction
        :param str dir: the direction of player given as input
        """

        self.acc = acc
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.dir = dir
        super().__init__(x, y, pic_path)

        self.is_alive = True

    def change_status(self, dir):
        """
        Determine the attributes of player on the next frame

        :param str dir: the direction of player given as input
            null -> no input,
            'a' -> left,
            'd' -> right,
            'w' -> up,
            's' -> down
        """

        if dir == None:
            # no input given, continue in previous direction
            self.x += vel_x
            self.y += vel_y

        elif dir == 'a':
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

    def is_alive(self):
        """
        :return: Whether player is alive
        :rtype: boolean
        """
        return self.is_alive

    def collide(self, oth_game_obj):
        """
        :return: Whether player collided with another game object
        :rtype: boolean
        """
        pass


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

    def change_status(self):
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

    def is_alive(self):
        """
        :return: Whether enemy is alive
        :rtype: boolean
        """
        return self.is_alive

    def collide(self, oth_game_obj):
        """
        :return: Whether enemy collided with another game object
        :rtype: boolean
        """
        pass


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