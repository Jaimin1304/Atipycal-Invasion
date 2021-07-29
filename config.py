import pygame as pg

scr_wid = 1600
scr_hgt = 900

screen = pg.display.set_mode((scr_wid, scr_hgt))

clock = pg.time.Clock()

fps = 60

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

page_lst = []

player = 'player object'
player_hgt = 30
player_wid = 30
player_spd_lim = 18  # The player's speed limit

x_player = 0
y_player = 0

enemy_hgt = 30
enemy_wid = 30

pi = 3.1416 # The approx val of pi
const_G = 16.67 # The gravitational constant

enemy_lst = []
star_lst = []

map_hgt = 2400  # The hight of the game map
map_wid = 3200  # The width of the game map

scr_x = 0  # The screen's x coor on the game map
scr_y = 0  # The screen's y coor on the game map

start_page = False
game_page = False
info_page = False
score_page = False
settings_page = False
