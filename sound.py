import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        pg.mixer.set_num_channels(32)
        self.path = 'resources/sound/'

        self.npc_dog_attack = pg.mixer.Sound(self.path + 'npc/dog/attack.wav')
        self.npc_dog_death = pg.mixer.Sound(self.path + 'npc/dog/death.wav')

        self.npc_soldier_attack = pg.mixer.Sound(self.path + 'npc/soldier/attack.wav')
        self.npc_soldier_pain = pg.mixer.Sound(self.path + 'npc/soldier/pain.wav')
        self.npc_soldier_death = pg.mixer.Sound(self.path + 'npc/soldier/death.wav')
        self.npc_soldier_attack.set_volume(0.5)

        self.npc_officer_attack = pg.mixer.Sound(self.path + 'npc/officer/attack.wav')
        self.npc_officer_pain = pg.mixer.Sound(self.path + 'npc/officer/pain.wav')
        self.npc_officer_death = pg.mixer.Sound(self.path + 'npc/officer/death.wav')

        self.npc_ss_attack = pg.mixer.Sound(self.path + 'npc/ss/attack.wav')
        self.npc_ss_pain = pg.mixer.Sound(self.path + 'npc/ss/pain.wav')
        self.npc_ss_death = pg.mixer.Sound(self.path + 'npc/ss/death.wav')

        self.npc_doctor_attack = pg.mixer.Sound(self.path + 'npc/doctor/attack.wav')
        self.npc_doctor_pain = pg.mixer.Sound(self.path + 'npc/doctor/pain.wav')
        self.npc_doctor_death = pg.mixer.Sound(self.path + 'npc/doctor/death.wav')

        self.npc_hitler2_attack = pg.mixer.Sound(self.path + 'npc/hitler2/attack.wav')
        self.npc_hitler2_pain = pg.mixer.Sound(self.path + 'npc/hitler2/pain.wav')
        self.npc_hitler2_death = pg.mixer.Sound(self.path + 'npc/hitler2/death.wav')

        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
        pg.mixer.music.set_volume(0.4)