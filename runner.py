import pygame as pg
import config as cf
from sys import exit
import page

pg.init()

pg.display.set_caption("Atipycal Invasion")

title_icon = pg.image.load("Icons/Neon_Player.png")
pg.display.set_icon(title_icon)

while True:
    page.start_page()

    while cf.game_page:
        page.game_page()
