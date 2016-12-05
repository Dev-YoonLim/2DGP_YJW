import random
from pico2d import *
from time_obj import Bar
from men import Men

men = None
boomtime = 0.0
boomcount = 0.0
juch = False

class Blue:
    def __init__(self):
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.count = random.randint(0, 100)

        self.jub = load_image('ju/blue2.png')
        self.image = load_image('pso/gamok4.png')

    def get_bb(self):
        return self.bux - 45, self.buy - 45, self.bux + 45, self.buy + 45

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def draw(self):
        global bar
        bar = Bar()
        if bar.update_t != False:
            self.image.draw(self.bux, self.buy)
            self.jub.draw(self.bux, self.buy - 5)

    def update(self, men):
        global bulid, bulids
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.count = random.randint(0, 100)


class Green:
    def __init__(self):
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.bx = random.randint(100, 1100)
        self.by = random.randint(100, 500)
        self.count = random.randint(0, 100)

        self.jug = load_image('ju/green2.png')
        self.jub = load_image('ju/blue2.png')
        self.image = load_image('pso/gamok4.png')

    def get_bb(self):
        return self.bux - 40, self.buy - 40, self.bux + 40, self.buy + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        global bar, juch
        bar = Bar()
        if bar.update_t != False:
            if self.count > 60 and self.count < 90:
                juch = False
                self.image.draw(self.bux, self.buy)
                self.jug.draw(self.bux, self.buy - 5)
            else:
                juch = True
                self.image.draw(self.bux, self.buy)
                self.jub.draw(self.bux, self.buy - 5)


    def update(self, men):
        global bulid, bulids
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.count = random.randint(0, 100)



class Red:
    def __init__(self):
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.count = random.randint(0, 100)
        self.bx = random.randint(100, 1100)
        self.by = random.randint(100, 500)
        self.jur = load_image('ju/red2.png')
        self.jub = load_image('ju/blue2.png')
        self.image = load_image('pso/gamok4.png')

    def get_bb(self):
        return self.bux - 40, self.buy - 40, self.bux + 40, self.buy + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        global bar, juch
        bar = Bar()
        if bar.update_t != False:
            if self.count >= 90:
                juch = False
                self.image.draw(self.bux, self.buy)
                self.jur.draw(self.bux, self.buy - 5)
            else:
                juch = True
                self.image.draw(self.bux, self.buy)
                self.jub.draw(self.bux, self.buy - 5)

    def update(self, men):
        global bulid, bulids
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.count = random.randint(0, 100)




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
        self.image = load_image('pso/gamok4.png')
        self.image0 = load_image('pso/gamok4.png')

    def get_bb(self):
        return self.bux - 50, self.buy - 50, self.bux + 50, self.buy + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        global bar
        bar = Bar()
        if bar.update_t != False: #아직 타임이 끝나기 전
            self.image.draw(self.bux, self.buy)
            self.ju.draw(self.bux, self.buy-5)

    def update(self, men):
        global bulid, bulids
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.count = random.randint(0, 100)
        if self.count >= 97:
            self.ju = load_image('ju/red2.png')
        elif self.count > 80 and self.count < 97:
            self.ju = load_image('ju/green2.png')
        elif self.count <= 80:
            self.ju = load_image('ju/blue2.png')



class Boom:
    def __init__(self):
        global men
        men = Men()
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
            self.buy = random.randint(100, 600)
            self.alcount = 0
            boomtime = 0

    def draw(self):
            self.image.clip_draw(self.bframe * 222, self.bstate * 200, 260, 255, self.bux, self.buy)

    def get_bb(self):
        return self.bux - 30, self.buy - 30, self.bux + 30, self.buy + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())








