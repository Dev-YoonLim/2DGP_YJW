import game_framework
import event_state
from pico2d import *


name = "TitleState"
image = None
bgm = None
title_bgm = None
title_time = 0.0
push_time = 0.0



def enter():
    global image, bgm, title_bgm
    image = load_image('screen/title_floor_fix.png')
    title_bgm = load_music('bgm/first_text_bgm/title.mp3')
    title_bgm.set_volume(128)
    title_bgm.repeat_play()



def exit():
    global image, title_bgm
    del(image)
    del(title_bgm)

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
                title_time += 1


def draw():
    clear_canvas()
    image.draw(600,350)
    update_canvas()



def update():
    global image, push_time
    if title_time == 0:
        push_time = (push_time + 1) % 40
        if push_time < 20:
            image = load_image('screen/title_floor_fix.png')
        elif push_time > 20 and push_time < 40:
            image = load_image('screen/title_floor_push.png')
    elif title_time == 1:
        game_framework.change_state(event_state)


def pause():
    pass


def resume():
    pass


