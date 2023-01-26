import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/textures/sky.png', (self.settings.WIDTH, self.settings.HALF_HEIGHT))
        self.sky_offset = 0
        self.blood_screen = self.get_texture('resources/textures/blood_screen.png', self.settings.RES)
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'resources/textures/digits/{i}.png', [self.digit_size] * 2)
                             for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_image = self.get_texture('resources/textures/game_over.png', self.settings.RES)
        self.win_image = self.get_texture('resources/textures/win.png', self.settings.RES)

    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()

    def win(self):
        self.screen.blit(self.win_image, (0, 0))

    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size, 0))
        self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size, 0))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % self.settings.WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + self.settings.WIDTH, 0))
        # floor
        pg.draw.rect(self.screen, self.settings.FLOOR_COLOR, (0, self.settings.HALF_HEIGHT, self.settings.WIDTH, self.settings.HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        res = (self.settings.TEXTURE_SIZE, self.settings.TEXTURE_SIZE)
        return {
            1: self.get_texture('resources/textures/walls/wall_01.png', res),
            2: self.get_texture('resources/textures/walls/wall_02.png', res),
            3: self.get_texture('resources/textures/walls/wall_03.png', res),
            4: self.get_texture('resources/textures/walls/wall_07.png', res),
            5: self.get_texture('resources/textures/walls/wall_14.png', res),
        }