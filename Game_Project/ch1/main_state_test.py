
import game_framework
import time_obj
import end_state
import prison
from pico2d import *
from floors import Floor
from prison import Bulid, Boom, Blue, Green, Red
from men import Men
from time_obj import Bar
from main_npc import Mnpc
from mid_event_state import event_01, event_00


running = None
point_state = 0
current_time = 0.0
sum_point = 0.0
game_ftpoint = 0.0
event_on = False
tutorial = True
game_set = False


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

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            men.handle_event(event)
        if time_obj.chup == True:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_y):
                bar.ch_points_life()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_n):
                bar.ch_points_times()
                bar.ch_level()


def create_world():
    global bulid, men, floor, bar, castle, mnpc, boom, bulids
    global blue, green, red, reds, blues, greens, redsbar
    global event01, event00
    global game_set
    mnpc = Mnpc()
    event00 = event_00()
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
    create_world()

def exit():
    destroy_world()

def update():
    global hit_stack, blues, greens, reds, tutorial, game_ftpoint
    frame_time = get_frame_time()
    men.update(frame_time)
    bar.update_t(frame_time)
    bar.update_l(frame_time)
    bar.update_p()
    bar.ch_check_p()
    boom.update()
    bar.sum_points()
    bar.ch_bar(frame_time)
    if time_obj.chup == True:
        event00.event00_time()
    if men.draw() == True:
        blues = [Blue() for i in range(8)]
        blue.update(men)
        greens = [Green() for i in range(3)]
        green.update(men)
        reds = [Red() for i in range(1)]
        red.update(men)
        floor.normal_update()
    if bar.end_time() == True:
        game_framework.change_state(end_state)
    if game_set == False:
        game_ftpoint = 0.00001
    elif game_set == True:
        game_ftpoint = frame_time



def draw():
    global point_state, sum_point, tutorial, game_set
    clear_canvas()
    floor.draw()
    men.draw()
    men.draw_bb()
    bar.lbdraw()
    bar.pbdraw()
    bar.ndraw()
    bar.tbdraw()
    if time_obj.chup == False:
        point_state = 0
        boom.draw()
        boom.draw_bb()
        if high_crush(men, boom):
            point_state = 4
        for blue in blues:
            blue.draw()
            blue.draw_bb()
            if high_crush(men, blue):
                blues.remove(blue)
                point_state = 1
        for green in greens:
            green.draw()
            green.draw_bb()
            if high_crush(men, green) and prison.juch == False:
                greens.remove(green)
                point_state = 2
            elif high_crush(men, green) and prison.juch == True:
                greens.remove(green)
                point_state = 1
        for red in reds:
            red.draw()
            red.draw_bb()
            if high_crush(men, red) and prison.juch == False:
                reds.remove(red)
                point_state = 3
            elif high_crush(men, red) and prison.juch == True:
                reds.remove(red)
                point_state = 1
    elif time_obj.chup == True:
        if tutorial == True:
            event00.draw()
            if tutorial == False:
                mnpc.draw()
        else:
            mnpc.draw()
        #if crush(men, mnpc):



    update_canvas()
    game_set = True

