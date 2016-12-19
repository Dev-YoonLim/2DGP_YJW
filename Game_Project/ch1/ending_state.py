from pico2d import *
import game_framework
import last_true_one
from time_obj import Bar
import time_obj
import random

ending_count = 0.0
ending_times = 0
no_space = False
bgm = None

class Bad:
    def __init__(self):
        self.x = 600
        self.y = 350
        self.darkview = random.randint(0, 5)
        self.image = load_image('event_e/bad_ending_1.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        global ending_times, ending_count, no_space
        if ending_times == 1:
            self.image = load_image('event_e/bad_ending_2.png')
        elif ending_times == 2:
            no_space = True
            self.darkview = random.randint(0, 5)
            if self.darkview != 0:
                self.image = load_image('event_e/bad_ending_3.png')
            else:
                self.image = load_image('event_s/darkface.png')
            ending_count += 0.01
        if ending_count > 3:
            ending_times = 10


class Normal:
    def __init__(self):
        self.x = 600
        self.y = 350
        self.image = load_image('event_e/bad.ending_1.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        global ending_times, ending_count, no_space
        if ending_times == 1:
            self.image = load_image('event_e/normal_ending_1.png')
        elif ending_times == 2:
            self.image = load_image('event_e/normal_ending_2.png')
        elif ending_times == 3:
            self.image = load_image('event_e/normal_ending_3.png')
        elif ending_times == 4:
            self.image = load_image('event_e/normal_ending_4.png')
        elif ending_times == 5:
            no_space = True
            self.darkview = random.randint(0, 5)
            if self.darkview != 0:
                self.image = load_image('event_e/bad_ending_5.png')
            else:
                self.image = load_image('event_s/darkface.png')
            ending_count += 0.01
        if ending_count > 3:
            ending_times = 10


class Good:
    def __init__(self):
        self.x = 600
        self.y = 350
        self.image = load_image('event_e/one_more3.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        global ending_times
        if ending_times == 1:
            self.image = load_image('event_e/mu3.png')
        elif ending_times == 2:
            self.image = load_image('event_e/normal_die.png')
        if ending_times == 3:
            ending_times = 10


class Hidden:
    def __init__(self):
        self.x = 600
        self.y = 350
        self.image = load_image('event_e/blue_more4.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        global ending_times
        if ending_times == 1:
            self.image = load_image('event_e/mu3.png')
        elif ending_times == 2:
            self.image = load_image('event_e/blue_die.png')
        if ending_times == 3:
            ending_times = 10



def enter():
    global bad, normal, good, trues, hidden
    global bar, bgm, gameover
    bad = Bad()
    normal = Normal()
    good = Good()
    trues = Trues()
    hidden = Hidden()
    gameover = load_image('END/end_one.png')

    bar = Bar()
    if time_obj.ch_ending != 4:
        bgm = load_music('bgm/end/ho.mp3')
        bgm.set_volume(64)
        bgm.repeat_play()

def exit():
    global bgm, gameover
    del(bgm)
    del(gameover)

def handle_events():
    global ending_times
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) and no_space == False:
                ending_times += 1


def draw():
    clear_canvas()
    print(time_obj.ch_ending)
    if time_obj.ch_ending == 0:
        bad.image.draw(600,350)
    elif time_obj.ch_ending == 1:
        normal.image.draw(600, 350)
    elif time_obj.ch_ending == 2:
        good.image.draw(600, 350)
    elif time_obj.ch_ending == 3:
        trues.image.draw(600, 350)
    elif time_obj.ch_ending == 4:
        hidden.image.draw(600, 350)
    if ending_times == 10:
        gameover.draw(600, 350)
    update_canvas()


def update():
    global bad, ending_times, ending_count
    if ending_times == 10:
        ending_count += 0.01
    if ending_count > 5:
        game_framework.quit()
        close_canvas()
    if time_obj.ch_ending == 0:
        bad.update()
    elif time_obj.ch_ending == 1:
        normal.update()
    elif time_obj.ch_ending == 2:
        good.update()
    elif time_obj.ch_ending == 3:
        trues.update()
    elif time_obj.ch_ending == 4:
        hidden.update()