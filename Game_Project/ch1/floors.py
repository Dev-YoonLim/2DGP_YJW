from pico2d import *
import last_true_one
import random


class Floor:
    global mapx, mapy, map

    def __init__(self):
        self.eventfloor = False
        self.image = load_image('floor_in/block3_1_floor.png')
        self.image0 = load_image('event_s/darkface.png')
        if last_true_one.last_stage == False:
            self.bgm = load_music('sound/main_sound1.mp3')
        self.darktext = load_image('text/hehe.png')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()
        self.count = random.randint(0, 100)
        self.darkx = random.randint(100, 1100)
        self.darky = random.randint(100, 600)

    def draw(self):
        self.image.draw(600, 350)

    def draw0(self):
        self.image0.draw(600, 350)

    def draw_text(self):
        self.darktext.draw(self.darkx, self.darky)


    def normal_update(self):
        self.darkx = random.randint(200, 1000)
        self.darky = random.randint(150, 550)
        self.count = random.randint(0, 100)
        if self.count > 0 and self.count <= 25:
            self.darktext = load_image('text/hehe.png')
        elif self.count > 25 and self.count <= 50:
            self.darktext = load_image('text/die.png')
        elif self.count > 50 and self.count <= 75:
            self.darktext = load_image('text/dontrun.png')
        elif self.count > 75 and self.count <= 100:
            self.darktext = load_image('text/fuckyou.png')


