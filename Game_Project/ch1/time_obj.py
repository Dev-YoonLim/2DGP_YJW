from pico2d import*

chup = False


class Bar:
    PIXEL_PER_METER = (10.0 / 0.2)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def tbdraw(self):
        self.tbimage.draw(self.bx, self.by)
    def lbdraw(self):
        self.lbimage.draw(self.lx, self.ly)
    def ndraw(self):
        self.nimage.draw(self.nx, self.ny)

    def __init__(self):
        self.nx = 50
        self.ny = 650
        self.bx = 600
        self.by = 670
        self.lx = 115
        self.ly = 627
        self.times = 2500
        self.life = 0
        self.plus_count = 4.0
        self.sub_count = 1.0
        self.nimage = load_image('text/eng3.png')
        self.tbimage = load_image('bar/timebar6.png')
        self.lbimage = load_image('bar/timebar6.png')

    def update_t(self, frame_time):
        global chup, plus_count
        distance = Bar.RUN_SPEED_PPS * frame_time
        if self.times >= 0 and self.plus_count > 0 and chup == False:
            self.times = self.times - distance/self.plus_count
        elif self.times < 0:
            chup = True
            self.plus_count = self.plus_count - 1
            self.sub_count = self.sub_count + 0.5
            self.times = 0
        if self.times >= 2000:
            self.bx = 600
            self.by = 670
            self.tbimage = load_image('bar/timebar.png')
        elif self.times >= 1600 and self.times < 2000:
            self.bx = 500
            self.by = 670
            self.tbimage = load_image('bar/timebar2.png')
        elif self.times >= 1200 and self.times < 1600:
            self.bx = 400
            self.by = 670
            self.tbimage = load_image('bar/timebar3.png')
        elif self.times >= 800 and self.times < 1200:
            self.bx = 300
            self.by = 670
            self.tbimage = load_image('bar/timebar4.png')
        elif self.times >= 400 and self.times < 800:
            self.bx = 200
            self.by = 670
            self.tbimage = load_image('bar/timebar5.png')
        elif self.times < 400:
            self.bx = 115
            self.by = 670
            self.tbimage = load_image('bar/timebar6.png')

    def update_l(self, frame_time):
        global chup, sub_count
        distance = Bar.RUN_SPEED_PPS * frame_time
        if chup == True and self.sub_count < 6:
            self.life = self.life + distance/self.sub_count
            if self.life > 2100:
                chup = False
                self.times = self.life
                self.life = 0
        if self.life >= 2000:
            self.lx = 600
            self.ly = 630
            self.lbimage = load_image('bar/timebar.png')
        elif self.life >= 1600 and self.life < 2000:
            self.lx = 500
            self.ly = 630
            self.lbimage = load_image('bar/timebar2.png')
        elif self.life >= 1200 and self.life < 1600:
            self.lx = 400
            self.ly = 630
            self.lbimage = load_image('bar/timebar3.png')
        elif self.life >= 800 and self.life < 1200:
            self.lx = 300
            self.ly = 630
            self.lbimage = load_image('bar/timebar4.png')
        elif self.life >= 400 and self.life < 800:
            self.lx = 200
            self.ly = 630
            self.lbimage = load_image('bar/timebar5.png')
        elif self.life < 400:
            self.lx = 115
            self.ly = 630
            self.lbimage = load_image('bar/timebar6.png')


    def next(self):
        if self.plus_count == 0:
            return True


