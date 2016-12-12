import game_framework
import title_state_two
from pico2d import *


name = "TitleState"
image = None
bgm = None
title_bgm = None
title_time = 0.0
push_time = 0.0
title_bgmon = False
title_bgmon_nu = 0


def enter():
    global image, bgm, title_bgm
    image = load_image('event_s/men_start.png')
    bgm = load_music('bgm/first_text_bgm/wind.mp3')
    bgm.set_volume(128)
    bgm.repeat_play()



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
                title_time += 1


def draw():
    clear_canvas()
    image.draw(600,350)
    update_canvas()



def update():
    global image, push_time, title_bgmon, title_bgmon_nu
    if title_time == 1:
        image = load_image('event_s/men_start2.png')
    elif title_time == 2:
        image = load_image('event_s/men_start3.png')
    elif title_time == 3:
        image = load_image('event_s/main_start4.png')
    elif title_time == 4:
        image = load_image('event_s/main_start5.png')
    elif title_time == 5:
        game_framework.change_state(title_state_two)


def pause():
    pass


def resume():
    pass






