from math import trunc
import game_obj as go
import pygame as pg
import config as cf
from sys import exit

def screen_refresh():
    """
    Update the screen picture every frame.
    """
    pg.display.update()
    cf.screen.fill(cf.black)
    cf.clock.tick(cf.fps)

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
                cf.game_page = True
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
    player = go.player(cf.scr_wid/2 - cf.player_wid/2,
                       cf.scr_hgt/2 - cf.player_hgt/2,
                       "Icons/Neon_Player.png",
                       0.3,
                       0,
                       0)

    sun = go.star(x=1800, y=1300, pic_path="stars/star_red.png", 
                  rev_time=0, star_r=180, orbit_r=0, mass=80, 
                  g_range=1000, par=None, angle=0)

    red = go.star(x=0, y=0, pic_path="stars/planet_red.png", 
                  rev_time=360, star_r=60, orbit_r=400, mass=20, 
                  g_range=400, par=sun, angle=380, clockwise=False)

    wet = go.star(x=0, y=0, pic_path="stars/planet_wet.png", 
                  rev_time=720, star_r=80, orbit_r=800, mass=30, 
                  g_range=500, par=sun, angle=130)

    moon = go.star(x=0, y=0, pic_path="stars/planet_grey.png", 
                  rev_time=180, star_r=40, orbit_r=200, mass=10, 
                  g_range=200, par=wet, angle=60, clockwise=False)

    bg_pic = go.picture(0, 0, "100x100.png", 3200, 2400)
    test_pic = go.picture(500, 900, "Death.png", 100, 100)
    txt = go.text()
    while True:
        bg_pic.refresh()
        txt.write_txt([300, 300], 300, [148, 0, 211], "Hello There")
        sun.refresh()
        red.refresh()
        wet.refresh()
        moon.refresh()
        #for coor in cf.trace:
        #    txt.write_txt(coor, 12, cf.white, "*")
        test_pic.refresh()
        txt.write_txt([0, 0], 30, [255, 160, 122], 
                       "x:{} y:{}".format(cf.x_player, cf.y_player), False)
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
                cf.start_page = True
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
