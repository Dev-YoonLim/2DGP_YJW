import random
from pico2d import *
from time_obj import Bar
import men

men = None
boomtime = 0.0
boomcount = 0.0

class Bulid:

    def __init__(self):
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.count = random.randint(0, 100)
        if self.count >= 97:
            self.ju = load_image('ju/red2.png')
        elif self.count > 80 and self.count < 97:
            self.ju = load_image('ju/green2.png')
        elif self.count <= 80:
            self.ju = load_image('ju/blue2.png')
        self.image = load_image('pso/gamok3.png')

    def draw(self):
        global bar
        bar = Bar()
        if bar.update_t != False:
            self.image.draw(self.bux, self.buy)
            self.ju.draw(self.bux, self.buy-5)

    def update(self, men):
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.count = random.randint(0, 100)
        if self.count >= 97:
            self.ju = load_image('ju/red2.png')
        elif self.count > 80 and self.count < 97:
            self.ju = load_image('ju/green2.png')
        elif self.count <= 80:
            self.ju = load_image('ju/blue2.png')

class Castle:

    def __init__(self):
        self.bux = 600
        self.buy = 500
        self.image = load_image('pso/ca1.png')

    def draw(self):
        self.image.draw(self.bux, self.buy)


class Boom:
    def __init__(self):
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.image = load_image('boom effect/boom/boom0.png')
        self.bframe = 0
        self.bstate = 0
        self.fcount = 0
        self.alcount = 0
        self.boomroll = True

    def update(self):
        global boomtime, boomcount
        self.alcount = (self.alcount +1) % 62
        if boomtime == 200:
            self.fcount = (self.fcount + 1 ) % 6
            self.bframe = (self.bframe + 1 ) % 5
            boomtime = 0
        boomtime += 50
        if self.fcount > 4:
            self.bstate = (self.bstate + 1) % 3
            self.fcount = 0
        if self.alcount > 60:
            self.bux = random.randint(100, 1100)
            self.buy = random.randint(100, 500)
            self.alcount = 0
            boomtime = 0

    def draw(self):
            self.image.clip_draw(self.bframe * 222, self.bstate * 200, 260, 255, self.bux, self.buy)








