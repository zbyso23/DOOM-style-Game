import math

TITLE = 'Inglourious Basterds 3D'
TITLE_SETUP = 'Inglourious Basterds 3D Setup'
VERSION = '0.1'
CONFIG_PATH = './config.json'

class Settings:
    def __init__(self, config):
      self.GOD_MODE = config['cheats']['god_mode']
      self.FULLSCREEN = config['screen']['fullscreen']

      self.WIDTH = config['screen']['width']
      self.HEIGHT = config['screen']['height']
      self.RES = self.WIDTH, self.HEIGHT

      self.HALF_WIDTH = self.WIDTH // 2
      self.HALF_HEIGHT = self.HEIGHT // 2
      self.FPS = 0
      
      self.MOUSE_BORDER_LEFT = 100
      self.MOUSE_BORDER_RIGHT = self.WIDTH - self.MOUSE_BORDER_LEFT

      self.FOV = math.pi / 3
      self.HALF_FOV = self.FOV / 2
      self.NUM_RAYS = self.WIDTH // 2
      self.HALF_NUM_RAYS = self.NUM_RAYS // 2
      self.DELTA_ANGLE = self.FOV / self.NUM_RAYS
      self.MAX_DEPTH = 20

      self.SCREEN_DIST = self.HALF_WIDTH / math.tan(self.HALF_FOV)
      self.SCALE = self.WIDTH // self.NUM_RAYS

      self.PLAYER_POS = 1.5, 5  # mini_map
      self.PLAYER_ANGLE = 0
      self.PLAYER_SPEED_WALK = 0.004
      self.PLAYER_SPEED_RUN = 0.009
      self.PLAYER_ROT_SPEED = 0.002
      self.PLAYER_SIZE_SCALE = 60
      self.PLAYER_MAX_HEALTH = 100

      self.MOUSE_SENSITIVITY = 0.0003
      self.MOUSE_MAX_REL = 40

      self.FLOOR_COLOR = (30, 30, 30)

      self.TEXTURE_SIZE = 512
      self.HALF_TEXTURE_SIZE = self.TEXTURE_SIZE // 2

