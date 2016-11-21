
import game_framework
import time_obj
from pico2d import *
from floors import Floor
from prison import Bulid, Castle, Boom, Blue, Green, Red
from men import Men
from time_obj import Bar
from main_npc import Mnpc


running = None
runch = 0
point = False

current_time = 0.0
hit_stack = 0.0


def crush(a, b):
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
        else :
            men.handle_event(event)


def create_world():
    global bulid, men, floor, bar, castle, mnpc, boom, bulids
    global blue, green, red, blues, greens, reds
    mnpc = Mnpc()

    bulid = Bulid()
    bulids = [Bulid() for i in range(10)]
    blue = Blue()
    blues = [Blue() for i in range(12)]
    green = Green()
    greens = [Green() for i in range(6)]
    red = Red()
    reds = [Red() for i in range(2)]

    boom = Boom()
    castle = Castle()
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
    close_canvas()

def update():
    global hit_stack, blues, greens, reds
    frame_time = get_frame_time()
    men.update(frame_time)
    bar.update_t(frame_time)
    bar.update_l(frame_time)
    boom.update()
    if men.draw() == True:
        blues = [Blue() for i in range(12)]
        blue.update(men)
        greens = [Green() for i in range(6)]
        green.update(men)
        reds = [Red() for i in range(2)]
        red.update(men)




def draw():
    clear_canvas()
    floor.draw()
    men.draw()
    men.draw_bb()
    bar.tbdraw()
    bar.lbdraw()
    bar.ndraw()
    if time_obj.chup == False:
        boom.draw()
        for blue in blues:
            blue.draw()
            if crush(men, blue):
                blues.remove(blue)
        for green in greens:
            green.draw()
            if crush(men, green):
                greens.remove(green)
        for red in reds:
            red.draw()
            if crush(men, red):
                reds.remove(red)


    elif time_obj.chup == True:
        castle.draw()
        mnpc.draw()


    update_canvas()

