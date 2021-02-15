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

tower_hgt = 70
tower_wid = 70

pi = 3.14

start_page = False
game_page = False
info_page = False
score_page = False
settings_page = False