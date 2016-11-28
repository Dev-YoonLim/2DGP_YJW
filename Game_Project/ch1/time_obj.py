from pico2d import*
import main_state_test

chup = False


class Bar:
    chup = False
    PIXEL_PER_METER = (10.0 / 0.2)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    def tbdraw(self):
        self.tbimage.draw(self.tx, self.ty)
    def lbdraw(self):
        self.lbimage.draw(self.lx, self.ly)
    def ndraw(self):
        self.nimage.draw(self.nx, self.ny)
    def pbdraw(self):
        self.pbimage.draw(self.px, self.py)

    def __init__(self):
        self.nx = 50
        self.ny = 635
        self.tx = 600
        self.ty = 670
        self.lx = 115
        self.ly = 635
        self.px = 115
        self.py = 595
        self.times = 2500
        self.life = 0
        self.points = 100
        self.plus_count = 5.0
        self.count_time = 0
        self.blue_sum = 0.0
        self.green_sum = 0.0
        self.red_sum = 0.0
        self.all_sum = 0.0
        self.nimage = load_image('text/eng5.png')

    def update_t(self, frame_time):
        global chup
        distance = Bar.RUN_SPEED_PPS * frame_time
        if self.times >= 0 and self.plus_count > 0 and chup == False:
            self.times = self.times - (distance/self.plus_count)
        if self.times >= 2000:
            self.tx = 600
            self.ty = 670
            self.tbimage = load_image('bar/timebar.png')
        elif self.times >= 1600 and self.times < 2000:
            self.tx = 500
            self.ty = 670
            self.tbimage = load_image('bar/timebar2.png')
        elif self.times >= 1200 and self.times < 1600:
            self.tx = 400
            self.ty = 670
            self.tbimage = load_image('bar/timebar3.png')
        elif self.times >= 800 and self.times < 1200:
            self.tx = 300
            self.ty = 670
            self.tbimage = load_image('bar/timebar4.png')
        elif self.times >= 400 and self.times < 800:
            self.tx = 200
            self.ty = 670
            self.tbimage = load_image('bar/timebar5.png')
        elif self.times < 400:
            self.tx = 115
            self.ty = 670
            self.tbimage = load_image('bar/timebar6.png')

    def update_l(self, frame_time):
        global chup, sub_count

        if self.life >= 2000:
            self.lx = 600
            self.ly = 632
            self.lbimage = load_image('bar/timebar.png')
        elif self.life >= 1600 and self.life < 2000:
            self.lx = 500
            self.ly = 632
            self.lbimage = load_image('bar/timebar2.png')
        elif self.life >= 1200 and self.life < 1600:
            self.lx = 400
            self.ly = 632
            self.lbimage = load_image('bar/timebar3.png')
        elif self.life >= 800 and self.life < 1200:
            self.lx = 300
            self.ly = 632
            self.lbimage = load_image('bar/timebar4.png')
        elif self.life >= 400 and self.life < 800:
            self.lx = 200
            self.ly = 632
            self.lbimage = load_image('bar/timebar5.png')
        elif self.life < 400:
            self.lx = 115
            self.ly = 632
            self.lbimage = load_image('bar/timebar6.png')


    def update_p(self):
        global chpoint
        if self.times >= 0 and main_state_test.blue_point == True:
            self.points += 50
            self.blue_sum += 50
            main_state_test.blue_point = False

        if main_state_test.green_point == True:
            if self.life >= 300:
                self.life -= 300
                self.points += 300
                self.green_sum += 300
                main_state_test.green_point = False
            elif self.life < 300:
                self.times = self.times - 300
                self.points += 10
                self.green_sum += 10
                main_state_test.green_point = False

        if self.times >= 0 and main_state_test.red_point == True:
            if self.life >= 1000:
                self.life -= 1000
                self.points += 700
                self.red_sum += 1000
                main_state_test.red_point = False
            elif self.life < 1000:
                self.points += 20
                self.red_sum += 20
                main_state_test.red_point = False

        if self.points >= 2000:
            self.px = 600
            self.py = 595
            self.pbimage = load_image('bar/timebar_point.png')
        elif self.points >= 1600 and self.times < 2000:
            self.px = 500
            self.py = 595
            self.pbimage = load_image('bar/timebar2_point.png')
        elif self.points >= 1200 and self.times < 1600:
            self.px = 400
            self.py = 595
            self.pbimage = load_image('bar/timebar3_point.png')
        elif self.points >= 800 and self.times < 1200:
            self.px = 300
            self.py = 595
            self.pbimage = load_image('bar/timebar4_point.png')
        elif self.points >= 400 and self.times < 800:
            self.px = 200
            self.py = 595
            self.pbimage = load_image('bar/timebar5_point.png')
        elif self.points < 400:
            self.px = 115
            self.py = 595
            self.pbimage = load_image('bar/timebar6_point.png')

    def count_times(self, frame_time):
        global chup, sub_count
        distance = Bar.RUN_SPEED_PPS * frame_time
        if self.times > 0:
            self.count_time = 0
        elif self.times < 0:
            chup = True
            self.plus_count = self.plus_count - 0.5
            self.times = 0
        if chup == True:
            self.count_time = self.count_time + distance
        if self.count_time > 2500:
            self.times = self.points
            self.points = 0
            chup = False


    def chcrush_points(self):
        global chpoint
        if self.count_time <= 2500 and self.points > 10:
            self.life += 10
            self.points -= 10

    def sum_points(self):
        self.all_sum = self.blue_sum + self.green_sum + self.red_sum
        return self.all_sum

    def end_time(self):
        if self.plus_count == 0:
            return True





