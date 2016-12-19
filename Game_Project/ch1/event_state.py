import game_framework
import main_state_test
import end_state
from pico2d import *
import random

level = 0.0
name = "EventState"
event_time = 1
bgm = None
yes = True
select_time = False
no_key = False
death_count = 0

def enter():
    global image0, swith, bgm, test_yes, test_no, tests, death_face, death_bgm
    image0 = load_image('event_s_re/event_s1.png')
    test_yes = load_image('event_s_re/Yes_red.png')
    test_no = load_image('event_s_re/No.png')
    death_face = load_image('event_s_re/no_event_s3.png')
    death_bgm = load_music('bgm/end/ho.mp3')
    bgm = load_music('bgm/tutorial/tutorial.mp3')
    bgm.set_volume(128)
    bgm.repeat_play()


def exit():
    global image0
    del(image0)

def handle_events():
    global event_time, yes, no
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) and no_key == False:
                event_time += 1
                print(event_time)
                if event_time == 16:
                    game_framework.change_state(main_state_test)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_y) and select_time == True and no_key == False:
                yes = True
                event_time += 1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_n) and select_time == True and no_key == False:
                yes = False
                event_time += 1




def draw():
    global tests, death_count
    clear_canvas()
    image0.draw(600,350)
    if select_time == True:
        for i in range(20):
            test_no.draw(random.randint(100, 1100), random.randint(100, 600))
        test_yes.draw(600, 350)
    if no_key == True:
        for i in range(10):
            death_face.draw(random.randint(100, 1100), random.randint(100, 600))
            death_count += 1





    update_canvas()


def update():
    global event_time, image0, select_time, no_key
    if event_time == 1:
        image0 = load_image('event_s_re/event_s1.png')
    elif event_time == 2:
        image0 = load_image('event_s_re/event_s2.png')
    elif event_time == 3:
        image0 = load_image('event_s_re/event_s3.png')
    elif event_time == 4:
        image0 = load_image('event_s_re/event_s4.png')

    elif event_time == 5:
        select_time = True
        image0 = load_image('event_s_re/yes_no.png')

    elif event_time == 6:
        select_time = False
        if yes == False:
            death_bgm.set_volume(128)
            death_bgm.repeat_play()
            image0 = load_image('event_s_re/no_event_s1.png')
        else:
            image0 = load_image("event_s_re/yes_event_s1.png")


    elif event_time == 7 and yes == False:
        if yes == False:
            no_key = True
            image0 = load_image('event_s_re/no_event_s2.png')
        else:
            image0 = load_image("event_s_re/yes_event_s2.png")


    elif event_time == 8:
        image0 = load_image("event_s_re/yes_event_s3.png")
    elif event_time == 9:
        image0 = load_image("event_s_re/yes_event_s3-4.png")
    elif event_time == 10:
        image0 = load_image("event_s_re/yes_event_s4.png")
    elif event_time == 11:
        image0 = load_image("event_s_re/yes_event_s5.png")
    elif event_time == 12:
        image0 = load_image("event_s_re/yes_event_s6.png")
    elif event_time == 13:
        image0 = load_image("event_s_re/yes_event_s7.png")
    elif event_time == 14:
        image0 = load_image("event_s_re/yes_event_s8.png")
    elif event_time == 15:
        image0 = load_image("event_s_re/yes_event_s9.png")
    if death_count > 2400:
        no_key = True
        image0 = load_image('End/end_one.png')





    #global event_time, image0, level
    #if event_time > 10:
        #event_time = 0.0
        #game_framework.change_state(main_state_test)
    #event_time += 0.005
    #delay(0.001)
    #time_state()
