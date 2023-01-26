from sprite_object import *
from random import randint, random


class NPC(AnimatedSprite):
    def __init__(self, game, path, pos=(10.5, 5.5),
                 scale=0.6, shift=0.38, animation_time=180, name='soldier'):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_images = self.get_images(self.path + '/attack')
        self.death_images = self.get_images(self.path + '/death')
        self.idle_images = self.get_images(self.path + '/idle')
        self.pain_images = self.get_images(self.path + '/pain')
        self.walk_images = self.get_images(self.path + '/walk')

        self.name = name
        self.attack_dist = randint(5, 6)
        self.stalking_dist = randint(5, 6)
        self.speed = 0.008
        self.size = 20
        self.health = 100
        self.attack_damage = 10
        self.accuracy = 0.15
        self.alive = True
        self.pain = False
        self.ray_cast_value = False
        self.frame_counter = 0
        self.player_search_trigger = False

    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.run_logic()
        # self.draw_ray_cast()

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx * self.size), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * self.size)):
            self.y += dy

    def movement(self):
        next_pos = self.game.pathfinding.get_path(self.map_pos, self.game.player.map_pos, self.stalking_dist)
        if(next_pos == None):
          return
        next_x, next_y = next_pos

        # pg.draw.rect(self.game.screen, 'blue', (100 * next_x, 100 * next_y, 100, 100))
        if next_pos not in self.game.object_handler.npc_positions:
            angle = math.atan2(next_y + 0.5 - self.y, next_x + 0.5 - self.x)
            dx = math.cos(angle) * self.speed
            dy = math.sin(angle) * self.speed
            self.check_wall_collision(dx, dy)

    def attack(self):
        if self.animation_trigger == False:
          return
        name = self.name
        if name == 'dog':
          self.game.sound.npc_dog_attack.play()
        elif name == 'soldier':
          self.game.sound.npc_soldier_attack.play()
        elif name == 'officer':
          self.game.sound.npc_officer_attack.play()
        elif name == 'ss':
          self.game.sound.npc_ss_attack.play()
        elif name == 'doctor':
          self.game.sound.npc_doctor_attack.play()
        elif name == 'hitler2':
          self.game.sound.npc_hitler2_attack.play()
        if random() < self.accuracy and self.settings.GOD_MODE == False:
          self.game.player.get_damage(self.attack_damage)

    def animate_death(self):
        if self.game.global_trigger == False or self.alive or self.frame_counter == len(self.death_images):
          return
        self.image = self.death_images[self.frame_counter]
        self.frame_counter += 1

    def animate_pain(self):
        self.animate(self.pain_images)
        if self.animation_trigger:
            self.pain = False

    def check_hit_in_npc(self):
        if not self.ray_cast_value or not self.game.player.shot:
          return
        if self.settings.HALF_WIDTH - self.sprite_half_width < self.screen_x < self.settings.HALF_WIDTH + self.sprite_half_width:
          name = self.name
          if name == 'soldier':
            self.game.sound.npc_soldier_pain.play()
          elif name == 'officer':
            self.game.sound.npc_officer_pain.play()
          elif name == 'ss':
            self.game.sound.npc_ss_pain.play()
          elif name == 'doctor':
            self.game.sound.npc_doctor_pain.play()
          elif name == 'hitler2':
            self.game.sound.npc_hitler2_pain.play()
          self.game.player.shot = False
          self.pain = True
          self.health -= self.game.weapon.damage
          self.check_health()

    def check_health(self):
        if self.health > 0:
          return
        self.alive = False
        self.frame_counter = 0
        name = self.name
        if name == 'dog':
          self.game.sound.npc_dog_death.play()
        elif name == 'soldier':
          self.game.sound.npc_soldier_death.play()
        elif name == 'officer':
          self.game.sound.npc_officer_death.play()
        elif name == 'ss':
          self.game.sound.npc_ss_death.play()
        elif name == 'doctor':
          self.game.sound.npc_doctor_death.play()
        elif name == 'hitler2':
          self.game.sound.npc_hitler2_death.play()

    def run_logic(self):
        if not self.alive:
          self.animate_death()
          return

        self.ray_cast_value = self.ray_cast_player_npc()
        self.check_hit_in_npc()

        if self.pain:
            self.animate_pain()

        elif self.ray_cast_value:
            self.player_search_trigger = True

            if self.dist < self.attack_dist:
                self.animate(self.attack_images)
                self.stalking_dist = self.stalking_dist * 2 #After attack stalking for long distance
                self.attack()
            else:
                self.animate(self.walk_images)
                self.movement()

        elif self.player_search_trigger:
            self.animate(self.walk_images)
            self.movement()

        else:
            self.animate(self.idle_images)

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    def ray_cast_player_npc(self):
        if self.game.player.map_pos == self.map_pos:
            return True

        wall_dist_v, wall_dist_h = 0, 0
        player_dist_v, player_dist_h = 0, 0

        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.theta

        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        # horizontals
        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a

        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        for i in range(self.settings.MAX_DEPTH):
            tile_hor = int(x_hor), int(y_hor)
            if tile_hor == self.map_pos:
                player_dist_h = depth_hor
                break
            if tile_hor in self.game.map.world_map:
                wall_dist_h = depth_hor
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth

        # verticals
        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a

        delta_depth = dx / cos_a
        dy = delta_depth * sin_a

        for i in range(self.settings.MAX_DEPTH):
            tile_vert = int(x_vert), int(y_vert)
            if tile_vert == self.map_pos:
                player_dist_v = depth_vert
                break
            if tile_vert in self.game.map.world_map:
                wall_dist_v = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth

        player_dist = max(player_dist_v, player_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)

        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False

    def draw_ray_cast(self):
        pg.draw.circle(self.game.screen, 'red', (100 * self.x, 100 * self.y), 15)
        if self.ray_cast_player_npc():
            pg.draw.line(self.game.screen, 'orange', (100 * self.game.player.x, 100 * self.game.player.y),
                         (100 * self.x, 100 * self.y), 2)


class SoldierNPC(NPC):
    def __init__(self, game, path='resources/sprites/npc/soldier/soldier_01.png', pos=(10.5, 5.5),
                 scale=1.0, shift=0, animation_time=320, name='soldier'):
        super().__init__(game, path, pos, scale, shift, animation_time, name)
        self.name = name
        self.stalking_dist = randint(50, 60)
        self.attack_dist = randint(6, 8)
        self.health = 100
        self.attack_damage = 10
        self.speed = 0.035
        self.accuracy = 0.15


class DogNPC(NPC):
    def __init__(self, game, path='resources/sprites/npc/dog/dog_01.png', pos=(10.5, 5.5),
                 scale=1.0, shift=0, animation_time=320, name='dog'):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.name = name
        self.stalking_dist = randint(90, 120)
        self.attack_dist = 1.0
        self.health = 50
        self.attack_damage = 5
        self.speed = 0.04
        self.accuracy = 0.45

class SSNPC(NPC):
    def __init__(self, game, path='resources/sprites/npc/ss/ss_01.png', pos=(10.5, 5.5),
                 scale=0.9, shift=0, animation_time=320, name='ss'):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.name = name
        self.stalking_dist = randint(70, 80)
        self.attack_dist = 9.5
        self.health = 200
        self.attack_damage = 25
        self.speed = 0.035
        self.accuracy = 0.35

class DoctorNPC(NPC):
    def __init__(self, game, path='resources/sprites/npc/doctor/doctor_01.png', pos=(10.5, 5.5),
                 scale=1.0, shift=0, animation_time=320, name='doctor'):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.name = name
        self.stalking_dist = randint(60, 70)
        self.attack_dist = 10.0
        self.health = 200
        self.attack_damage = 35
        self.speed = 0.035
        self.accuracy = 0.25

class OfficerNPC(NPC):
    def __init__(self, game, path='resources/sprites/npc/officer/officer_01.png', pos=(10.5, 5.5),
                 scale=0.95, shift=0, animation_time=320, name = 'officer'):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.name = name
        self.stalking_dist = randint(60, 70)
        self.attack_dist = 9.0
        self.health = 150
        self.attack_damage = 20
        self.speed = 0.035
        self.accuracy = 0.25

class Hitler2NPC(NPC):
    def __init__(self, game, path='resources/sprites/npc/hitler2/hitler2_01.png', pos=(10.5, 5.5),
                 scale=1.0, shift=0, animation_time=320, name='hitler2'):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.name = name
        self.stalking_dist = randint(20, 40)
        self.attack_dist = 8.8
        self.health = 300
        self.attack_damage = 45
        self.speed = 0.035
        self.accuracy = 0.35




















