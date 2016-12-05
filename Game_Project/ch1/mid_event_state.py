import floors
from pico2d import *
import main_state_test
import random

event_time = 0.0
mid_event = True
event00_swith = False

class event_00:
    def __init__(self):
        self.event00_times = 0
        self.event00plus_point = 0.01
        self.image = load_image('event_s./point_life_times.png')

    def draw(self):
        self.image.draw(600, 350)

    def event00_time(self):
        global event00_swith
        self.event00_times += self.event00plus_point
        if self.event00_times > 5 and event00_swith == False:
            self.image = load_image('event_s/ch_gauge.png')
            self.event00_times = 0
            event00_swith = True
        elif self.event00_times > 5 and event00_swith == True:
            main_state_test.tutorial = False






class event_01:
    def __init__(self):
        self.image0 = load_image('event_s/save.png')
        self.x = 600
        self.y = 350

    def draw(self):
        self.image0.draw(self.x, self.y)

    def update(self):
        global event_time
        event_time += 0.01
        if event_time > 100:
            event_time == 0
            self.image0 = load_image('event_s/follow.png')

class event_02:
    def __init__(self):
        self.image0

