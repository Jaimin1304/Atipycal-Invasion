import pygame as pg

scr_wid = 800
scr_hgt = 600

screen = pg.display.set_mode((scr_wid, scr_hgt))

clock = pg.time.Clock()

fps = 60

black = [0, 0, 0]
white = [255, 255, 255]

page_lst = []

player_hgt = 30
player_wid = 30

enemy_hgt = 30
enemy_wid = 30

tower_hgt = 70
tower_wid = 70

pi = 3.14  #  The approx val of pi

start_page = False
game_page = False
info_page = False
score_page = False
settings_page = False

map_hgt = 2400  # The hight of the game map
map_wid = 3200  # The width of the game map

scr_x = 0  #  The screen's x coor on the game map
scr_y = 0  #  The screen's y coor on the game map
