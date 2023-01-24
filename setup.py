import pyautogui as pag
import pygame as pg
import sys
from settings import TITLE_SETUP
from config_file import save_config

WIDTH = 640
HEIGHT = 480

config_default = {
  'screen': {
    'width': 640,
    'height': 480,
    'fullscreen': True
  },
  'cheats': {
    'god_mode': True
  }
}

screen = pg.display.set_mode((WIDTH, HEIGHT), 0)
pg.time.delay(3 * 1000)
pg.quit()

res = save_config(config_default)
if(res['error']):
  pag.alert(text=res['error_message'], title=TITLE_SETUP)
sys.exit()


