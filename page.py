import game_obj as go
import pygame as pg
import data_storage as ds
from sys import exit


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
            if event.key == pg.K_a:
                print("About page")
            if event.key == pg.K_h:
                print("Help page")
            if event.key == pg.K_e:
                pg.quit()
                exit()

    screen_refresh()


def game_page():
    """
    Display the game page and handle its logic.
    """
    player = go.player(ds.scr_wid/2 - ds.player_wid/2,
                       ds.scr_hgt/2 - ds.player_hgt/2,
                       "Player.png",
                       0.3,
                       0 ,
                       0)
    bg_pic = go.picture(0, 0, "100x100.png")
    test_txt = go.text()
    while True:
        bg_pic.refresh()
        test_txt.write_txt([300, 600], 300, [148, 0, 211], "Hello There")
        test_txt.write_txt([0, 0], 30, [255, 160, 122], "Test2", False)

        player.refresh()
        screen_refresh()


def about_page():
    """
    Display the infomation page and handle its logic.
    """

    test_txt = go.text()
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_b:
                ds.start_page = True

        test_txt.write_txt([0, 0], 30, [255, 160, 122], "about page", False)
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
