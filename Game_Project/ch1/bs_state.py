import game_framework
import title_state
import main_state_test
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('screen/bs_next.png')


def exit():
    global image
    del(image)
    close_canvas()

def update():
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.change_state(main_state_test)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(600, 350)
    update_canvas()




def handle_events():
    pass


def pause(): pass


def resume(): pass