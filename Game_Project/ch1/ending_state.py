from pico2d import *
import game_framework
import last_true_one
from time_obj import Bar
import time_obj

ending_times = 0
bgm = None

class Bad:
    def __init__(self):
        self.x = 600
        self.y = 350
        self.image = load_image('event_e/one_more.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        global ending_times
        if ending_times == 1:
            self.image = load_image('event_e/mu.png')
        elif ending_times == 2:
            self.image = load_image('event_e/bad_die.png')
        elif ending_times == 3:
            ending_times = 10


class Normal:
    def __init__(self):
        self.x = 600
        self.y = 350
        self.image = load_image('event_e/one_more2.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        global ending_times
        if ending_times == 1:
            self.image = load_image('event_e/mu2.png')
        elif ending_times == 2:
            self.image = load_image('event_e/normal_die.png')
        if ending_times == 3:
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

class Trues:
    def __init__(self):
        self.x = 600
        self.y = 350
        self.image = load_image('event_e/trues_more.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        global ending_times
        if ending_times == 1:
            self.image = load_image('event_e/trues_um.png')
        elif ending_times == 2:
            self.image = load_image('event_e/trues_wait.png')
        elif ending_times == 3:
            self.image = load_image('event_e/trues_yami.png')
        elif ending_times == 4:
            self.image = load_image('event_e/trues_stop!!.png')
        elif ending_times == 5:
            self.image = load_image('event_e/trues_yami2.png')
        elif ending_times == 6:
            self.image = load_image('event_e/trues_rollback.png')
        elif ending_times == 7:
            self.image = load_image('event_e/trues_uha.png')
        elif ending_times == 8:
            self.image = load_image('event_e/goodyami.png')
        elif ending_times == 9:
            self.image = load_image('event_e/goodyami.png')
        elif ending_times == 10:
            close_canvas()
            game_framework.change_state(last_true_one)


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

class Trues_win:
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


class Trues_lose:
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
    global bar, bgm
    delay(2)
    open_canvas(1200, 700)
    bad = Bad()
    normal = Normal()
    good = Good()
    trues = Trues()
    hidden = Hidden()

    bar = Bar()
    if time_obj.ch_ending != 4:
        bgm = load_music('bgm/end/ho.mp3')
        bgm.set_volume(64)
        bgm.repeat_play()

def exit():
    global bgm, image
    del(bgm)
    del(image)

def handle_events():
    global ending_times
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
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
    update_canvas()


def update():
    global bad, ending_times
    if ending_times == 10:
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