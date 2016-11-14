import random
import title_state
import game_framework
import main_state_test
from floors import Floor
from pico2d import *
from prison import Castle
from men import Men
from time_obj import Bar


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time




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
    global bulid, men, floor, bar, castle
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
    frame_time = get_frame_time()
    men.update(frame_time)
    bar.update(frame_time)

def draw():
    clear_canvas()
    floor.draw()
    men.draw()
    bar.tbdraw()
    bar.lbdraw()
    bar.ndraw()
    castle.draw()

    update_canvas()