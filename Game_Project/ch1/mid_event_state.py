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
        self.s_push = 0
        self.image = load_image('event_s./point_life_times.png')

    def space_push(self):
        self.s_push += 5

    def draw(self):
        self.image.draw(600, 350)

    def event00_time(self):
        if self.s_push == 5:
            self.image = load_image('event_s/ch_gauge.png')
        elif self.s_push == 10:
            main_state_test.tutorial_ask = False
            main_state_test.tutorial = False


