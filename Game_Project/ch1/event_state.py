import game_framework
from event_swith import Swith
import main_state_test
from pico2d import *
import start_state

level = 0.0
name = "EventState"
space_on = False
event_time = 1
bgm = None

def enter():
    global image0, swith, bgm
    swith = Swith()
    image0 = load_image('event_s/wellcome.png')
    bgm = load_music('bgm/tutorial/tutorial.mp3')
    bgm.set_volume(128)
    bgm.repeat_play()


def exit():
    global image0
    del(image0)

def handle_events():
    global event_time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                event_time += 1
                print(event_time)
                if event_time == 9:
                    game_framework.change_state(main_state_test)




def draw():
    clear_canvas()
    image0.draw(600,350)
    update_canvas()


def update():
    global space_on, event_time
    if level == 0.0:
        global image0, image1, image2, image3, image4
        if event_time == 1:
            image0 = load_image('event_s/wellcome.png')
        elif event_time == 2:
            image0 = load_image('event_s/helpme.png')
        elif event_time == 3:
            image0 = load_image('event_s/rungame.png')
        elif event_time == 4:
            image0 = load_image('event_s/inpoint.png')
        elif event_time == 5:
            image0 = load_image('event_s/points.png')
        elif event_time == 6:
            image0 = load_image('event_s/lifeout.png')
        elif event_time == 7:
            image0 = load_image('event_s/booms.png')
        elif event_time == 8:
            image0 = load_image('event_s/timespoint.png')

    #global event_time, image0, level
    #if event_time > 10:
        #event_time = 0.0
        #game_framework.change_state(main_state_test)
    #event_time += 0.005
    #delay(0.001)
    #time_state()
