from pico2d import *

def handle_events():
    global running
    global x, y, len
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                x = x + 20
            elif event.key == SDLK_LEFT:
                x = x - 20
            elif event.key == SDLK_UP:
                y = y + 20
            elif event.key == SDLK_DOWN:
                y = y - 20
            elif event.key == SDLK_a:
                if len >= 300:
                    len = 299
                len = len + 10
            elif event.key == SDLK_b:
                if len <= 20:
                    len = 21
                len = len - 10


open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

import math


running = True
x, y = 400, 300
len = 100
rad = 0
frame = 0
while (running):
    clear_canvas()
    i = math.cos(rad) * len
    j = math.sin(rad) * len
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, i+x, j+y )
    update_canvas()
    frame = (frame + 1) % 8
    rad += 0.5

    delay(0.05)
    handle_events()

close_canvas()