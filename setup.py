import pyautogui as pag
import pygame as pg
import pygame_menu as pgm
import sys
from pygame_menu import sound
from settings import TITLE_SETUP
from config_file import save_config
from typing import Tuple, Any
from pygame_menu.examples import create_example_window

WIDTH = 640
HEIGHT = 480

config_default = {
  'screen': {
    'width': 1024,
    'height': 768,
    'fullscreen': True
  },
  'cheats': {
    'god_mode': False
  }
}


screen = create_example_window(TITLE_SETUP, (WIDTH, HEIGHT))
engine = sound.Sound()

engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, 'resources/sound/ui/click.ogg')

def menu_set_resolution(selected: Tuple, value: Any) -> None:
  engine.play_open_menu()
  config_default['screen']['width'] = value['width']
  config_default['screen']['height'] = value['height']
  pass

def menu_set_fullscreen(selected: Tuple, value: bool) -> None:
  engine.play_open_menu()
  config_default['screen']['fullscreen'] = value
  pass

def menu_set_godmode(selected: Tuple, value: bool) -> None:
  engine.play_open_menu()
  config_default['cheats']['god_mode'] = value
  pass

def menu_save_config():
  engine.play_open_menu()
  res = save_config(config_default)
  pg.time.delay(300)
  if(res['error']):
    pag.alert(text=res['error_message'], title=TITLE_SETUP)
    pg.quit()
    sys.exit()
  else:
    pg.quit()
    sys.exit()

def menu_quit():
  engine.play_open_menu()
  pg.time.delay(300)
  pg.quit()
  sys.exit()


menu = pgm.Menu('Setup', WIDTH, HEIGHT, theme=pgm.themes.THEME_BLUE)

menu_control_resolution = menu.add.selector('Resolution: ', [
  ('1024 x 768', { 'width': 1024, 'height': 768 }), 
  ('1366 x 768', { 'width': 1366, 'height': 768 }), 
  ('1680 x 1050', { 'width': 1680, 'height': 1050 }), 
  ('1920 x 1680', { 'width': 1920, 'height': 1080 })
  ], onchange=menu_set_resolution)
menu_control_fullscreen = menu.add.selector('Fullscreen: ', [('Yes', True), ('No', False)], onchange=menu_set_fullscreen)
menu_control_godmode = menu.add.selector('God mode: ', [('No', False), ('Yes', True)], onchange=menu_set_fullscreen)
menu_control_save_config = menu.add.button('Save Config & Exit', menu_save_config)
menu_control_exit = menu.add.button('Exit', menu_quit)

menu_control_save_config.translate(0,10)
menu_control_exit.translate(0,10)

menu.mainloop(screen)
