
import game_framework
import main_state_test
import prison
from pico2d import *
from floors import Floor
from prison import Bulid, Boom, Blue, Green, Red
from men import Men
from time_obj import Bar

current_time = 0.0
lsat_stage = True
last_sumpoint = 0.0
last_time = 2500
Lose = False
Win = False

PIXEL_PER_METER = (10.0 / 0.2)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

def get_frame_time():
    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

frame_time = get_frame_time()

def high_crush(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def get_frame_time():
    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

frame_time = get_frame_time()

distance = Bar.RUN_SPEED_PPS * frame_time

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            men.handle_event(event)


def create_world():
    global bulid, men, floor, bar, castle, mnpc, boom, bulids
    global blue, green, red, reds, blues, greens, redsbar
    global event01, event00
    global game_set, last_sumpoint
    open_canvas(1200, 700)
    last_sumpoint = 0.0
    bulid = Bulid()
    bulids = [Bulid() for i in range(10)]
    blue = Blue()
    blues = [Blue() for i in range(12)]
    green = Green()
    greens = [Green() for i in range(6)]
    red = Red()
    reds = [Red() for i in range(2)]

    boom = Boom()
    men = Men()
    floor = Floor()
    bar = Bar()



def destroy_world():
    global men, floor, bulid, bar
    del (men)
    del (floor)
    del (bulid)
    del (bar)


def enter():
    global last_stage
    create_world()
    last_stage = True

def exit():
    destroy_world()

def update():
    global hit_stack, blues, greens, reds, tutorial, game_ftpoint, last_time
    global Win, Lose
    frame_time = get_frame_time()
    men.update(frame_time)
    if men.draw() == True:
        floor.normal_update()
        blues = [Blue() for i in range(8)]
        blue.update(men)
        greens = [Green() for i in range(3)]
        green.update(men)
        reds = [Red() for i in range(1)]
        red.update(men)
        last_time -= distance
        if last_time < 0:
            if last_sumpoint > 5000:
                Win = True
            else:
                Lose = True



def draw():
    global point_state, sum_point, tutorial, game_set, last_sumpoint
    clear_canvas()
    floor.draw0()
    floor.draw_text()
    men.draw()
    men.draw_bb()
    point_state = 0
    boom.draw()
    boom.draw_bb()
    if high_crush(men, boom):
        last_sumpoint -= 200
    for blue in blues:
        blue.draw()
        blue.draw_bb()
        if high_crush(men, blue):
            blues.remove(blue)
            last_sumpoint += 50
    for green in greens:
        green.draw()
        green.draw_bb()
        if high_crush(men, green) and prison.juch == False:
            greens.remove(green)
            last_sumpoint += 500
        elif high_crush(men, green) and prison.juch == True:
            greens.remove(green)
            last_sumpoint += 50
    for red in reds:
        red.draw()
        red.draw_bb()
        if high_crush(men, red) and prison.juch == False:
            reds.remove(red)
            last_sumpoint += 1500
        elif high_crush(men, red) and prison.juch == True:
            reds.remove(red)
            last_sumpoint += 50





    update_canvas()
    game_set = True