import game_framework
import event_state
from pico2d import *


name = "TitleState"
image = None
title_time = 0.0

def enter():
    global image
    image = load_image('event_s/men_start.png')


def exit():
    global image
    del(image)


def handle_events():
    global title_time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                title_time += 1.0


def draw():
    clear_canvas()
    image.draw(600,350)
    update_canvas()



def update():
    global image
    if title_time == 1:
        image = load_image('event_s/men_start2.png')
    elif title_time == 2:
        image = load_image('event_s/men_start3.png')
    elif title_time == 3:
        image = load_image('screen/title_floor.png')
    elif title_time == 4:
        game_framework.change_state(event_state)


def pause():
    pass


def resume():
    pass






