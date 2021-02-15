import game_obj as go
import pygame as pg
import data_storage as ds
from sys import exit

#class page(object):
#
#    def __init__(self):
#        """
#        """
#        self.obj_lst = []
#
#    def handle_logic(self):
#        """
#        """
#        for i in self.obj_lst:
#            i.refresh()
#
#
#class start_menu(page):
#
#    def __init__(self):
#        """
#        The start menu page.
#        """
#        self.play_txt = go.text(100,100,"Play")
#        self.settings_txt = go.text(100,100,"Settings")
#        self.help_txt = go.text(100,100,"Help")
#        self.info_txt = go.text(100,100,"Info")
#        self.quit_txt = go.text(100,100,"Quit")
#        self.difficultly_txt = go.text(100,100,"diffculty")
#        self.logo_pic = go.picture(100,100,0)
#
#
#class game(page):
#
#    def __init__(self):
#        """
#        The main game page.
#        """
#        self.player = go.player(
#            400,
#            300,
#            "Player.png",
#            0.4,
#            0,
#            0
#            )
#        self.obj_lst = [self.player]


def screen_refresh():
    """
    Update the screen picture every frame.
    """
    pg.display.update()
    ds.screen.fill(ds.black)
    ds.clock.tick(ds.fps)


def start_page():
    """
    Display the start menu page and handle its logic.
    """
    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                ds.game_page = True
                print("ds.game_page: " + str(ds.game_page))
            if event.key == pg.K_s:
                print("Settings page")
    screen_refresh()


def game_page():
    """
    Display the game page and handle its logic.
    """
    player = go.player(400, 300, "Player.png", 0.5, 0 ,0)
    while True:
        player.refresh()
        screen_refresh()


def info_page():
    """
    Display the infomation page and handle its logic.
    """
    screen_refresh()


def score_page():
    """
    Display the score board page and handle its logic.
    """
    screen_refresh()


def settings_page():
    """
    Display the settings page and handle its logic.
    """
    screen_refresh()
