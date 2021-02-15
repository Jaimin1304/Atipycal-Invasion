import pygame as pg
import data_storage as ds
from sys import exit
import page

pg.init()

pg.display.set_caption("Atipycal Invasion")

title_icon = pg.image.load("Player.png")
pg.display.set_icon(title_icon)

while True:
    page.start_page()

    while ds.game_page:
        page.game_page()

