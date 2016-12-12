from pico2d import*
import main_state_test


ft_swith = False
chup = False
ch_ending = 0

class Bar:
    chup = False
    PIXEL_PER_METER = (10.0 / 0.2)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

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
        self.chup_count = 5.0
        self.count_time = 0
        self.blue_sum = 0.0
        self.green_sum = 0.0
        self.red_sum = 0.0
        self.all_sum = 0.0
        self.all_gauge = 0.0
        self.nimage = load_image('text/eng5.png')

    def update_t(self, frame_time):
        global chup
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

    def ch_bar(self, frame_time):
        global ft_swith
        distance = Bar.RUN_SPEED_PPS * main_state_test.game_ftpoint
        if self.times >= 0 and self.chup_count > 0 and chup == False:
            self.times = self.times - (distance / self.chup_count)
            print('%f' % main_state_test.game_ftpoint)
        if  main_state_test.point_state == 1:
            print("blue up")
            self.blue_sum += 50
            self.points += 50
            main_state_test.point_state = 0

        elif main_state_test.point_state == 2:
            print("green up")
            if self.life > 300:
                self.life -= 300
                self.green_sum += 500
                self.points += 400
                main_state_test.point_state = 0
            else:
                self.times -= 300
                self.green_sum += 500
                self.points += 150
                main_state_test.point_state = 0

        elif main_state_test.point_state == 3:
            print("red up")
            if self.life > 1000:
                self.life -= 700
                self.red_sum += 1500
                self.points += 1000
                main_state_test.point_state = 0
            else:
                self.times -= 700
                self.red_sum += 1500
                self.points += 350
                main_state_test.point_state = 0

        if main_state_test.point_state == 4:
            self.times -= 10
            main_state_test.point_state = 0


    def tbdraw(self):
        self.tbimage.draw(self.tx, self.ty)
    def lbdraw(self):
        self.lbimage.draw(self.lx, self.ly)
    def ndraw(self):
        self.nimage.draw(self.nx, self.ny)
    def pbdraw(self):
        self.pbimage.draw(self.px, self.py)

    def ch_points_times(self):
        global chup
        self.times = self.points
        self.points = 0
        chup = False

    def ch_points_life(self):
        if self.points > 100:
            self.life += 150
            self.points -= 100

    def ch_level(self):
        if self.chup_count < 1:
            self.chup_count = self.chup_count*0.5
        else:
            self.chup_count = self.chup_count - 0.5

    def ch_check_p(self):
        global chup
        if self.times < 0:
            self.times = 0
            chup = True


    def sum_points(self):
        global ch_ending
        self.all_sum = self.blue_sum + self.green_sum + self.red_sum
        if self.all_sum < 5000 and self.all_sum > 3000:
            ch_ending = 0
        elif self.all_sum >= 5000 and self.all_sum < 15000:
            ch_ending = 1
        elif self.all_sum >= 15000 and self.all_sum < 20000:
            ch_ending = 2
        elif self.all_sum >= 23000 or (self.blue_sum > 15000 and self.green_sum  > 5000 and self.red_sum > 4500):
            ch_ending = 3
        elif self.all_sum > 25000 or (self.blue_sum > 20000 and self.red_sum > 4500):
            ch_ending = 4



    def sum_gauge(self):
        self.all_gauge = self.times + self.life + self.points

    def end_time(self):
        if self.times <= 100 and self.points <= 100:
            return True




