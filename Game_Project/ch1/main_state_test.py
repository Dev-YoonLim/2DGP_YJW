import random
import title_state
import game_framework
from pico2d import *
from floors import Floor
from prison import Bulid
from men import Men
from time_obj import Bar


running = None
runch = 0
point = False
X = 640
Y = 360
T = 2500
L = 0
C = 0
ST = T
SL = 0

class Boom:
    def __init__(self):
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.image = load_image('boom effect/boom/boom0.png')
        self.bframe = 0
        self.bstate = 0
        self.fcount = 0
        self.alcount = 0

    def update(self):
        self.alcount = (self.alcount +1) % 16
        self.fcount = (self.fcount + 1 ) % 6
        self.bframe = (self.bframe + 1 ) % 5
        if self.fcount > 4:
            self.bstate = (self.bstate + 1) % 3
            self.fcount = 0
        if self.alcount > 14:
            self.bux = random.randint(100, 1100)
            self.buy = random.randint(100, 500)
            self.alcount = 0

    def draw(self):
        self.image.clip_draw(self.bframe * 222, self.bstate * 200, 260, 255, self.bux, self.buy)




class Swap:
    def update(self):
        global C, L, T, ST, SL
        L += 10
        SL += 10
        if SL > 2200:
            L -= 30
            T += 15
            if L < 0:
                SL = L
                ST = T



class Bar_and_Name:

    def __init__(self):
        self.nx = 50
        self.ny = 650
        self.bx = 600
        self.by = 670
        self.lx = 110
        self.lx = 627
        self.nimage = load_image('text/eng3.png')
        self.tbimage = load_image('bar/timebar.png')
        self.lbimage = load_image('bar/timebar6.png')

    def update(self):
        global T
        global S
        global ST
        if T >= 2000:
            self.bx = 600
            self.by = 670
            self.tbimage = load_image('bar/timebar.png')
        elif T >= 1600 and T < 2000:
            self.bx = 500
            self.by = 670
            self.tbimage = load_image('bar/timebar2.png')
        elif T >= 1200 and T < 1600:
            self.bx = 400
            self.by = 670
            self.tbimage = load_image('bar/timebar3.png')
        elif T >= 800 and T < 1200:
            self.bx = 300
            self.by = 670
            self.tbimage = load_image('bar/timebar4.png')
        elif T >= 400 and T < 800:
            self.bx = 200
            self.by = 670
            self.tbimage = load_image('bar/timebar5.png')
        elif T < 400:
            self.bx = 115
            self.by = 670
            self.tbimage = load_image('bar/timebar6.png')


        if L >= 2000:
            self.lx = 600
            self.ly = 630
            self.lbimage = load_image('bar/timebar.png')
        elif L >= 1600 and T < 2000:
            self.lx = 500
            self.ly = 630
            self.lbimage = load_image('bar/timebar2.png')
        elif L >= 1200 and T < 1600:
            self.lx = 400
            self.ly = 630
            self.lbimage = load_image('bar/timebar3.png')
        elif L >= 800 and T < 1200:
            self.lx = 300
            self.ly = 630
            self.lbimage = load_image('bar/timebar4.png')
        elif L >= 400 and T < 800:
            self.lx = 200
            self.ly = 630
            self.lbimage = load_image('bar/timebar5.png')
        elif L < 400:
            self.lx = 115
            self.ly = 630
            self.lbimage = load_image('bar/timebar6.png')


    def bdraw(self):
        self.tbimage.draw(self.bx, self.by)
        self.lbimage.draw(self.lx, self.ly)

    def ndraw(self):
        self.nimage.draw(self.nx, self.ny)

class Npc1:

    def __init__(self):
        self.x = 640
        self.y = 400
        self.image = load_image('char_in/npc1.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class Ca:
    global T
    def __init__(self):
        self.x = 640
        self.y = 600
        self.image = load_image('pso/ca1.png')

    def draw(self):
        self.image.draw(self.x, self.y)


current_time = 0.0

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



def nmcrush(men, npc):
    left_a, bottom_a, right_a, top_a = men.mcrush()
    left_b, bottom_b, right_b, top_b = npc.ncrush()

    if left_a > right_b: return False
    if right_a > left_b: return False
    if top_a < bottom_b: return False
    if bottom_b > top_b: return False

    return True


def create_world():
    global bulid, bulids, men, floor, bar
    bulid = Bulid()
    bulids = [Bulid() for i in range(10)]
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
    if men.draw() == True:
        for bulid in bulids:
            bulid.update(men)

def draw():
    clear_canvas()
    floor.draw()
    men.draw()
    bar.tbdraw()
    bar.lbdraw()
    bar.ndraw()
    for bulid in bulids:
        bulid.draw()

    update_canvas()

def main():
    open_canvas(1280, 700)


    floor = Floor()
    floors = [Floor() for i in range(92)]
    floors2 = [Floor() for i in range(4)]

    bulid = Bulid()
    bulids = [Bulid() for i in range(10)]

    ca = Ca()

    men = Men()
    npc = Npc1()

    ban = Bar_and_Name()
    boom = Boom()

    swap = Swap()

    global runch
    global running
    global X, Y, T, L, C, ST
    running = True

    while (ST >= 1 and running == True):
        frame_time = get_frame_time()
        handle_events()
        men.update(frame_time)

        clear_canvas()

        for floor in floors:
            for floor in floors:
                floor.draw()
                floor.update()


        for bulid in bulids:
            bulid.draw()
        if X > 1280:
            for bulid in bulids:
                bulid.update()
            X = 50
        elif X < 0:
            for bulid in bulids:
                bulid.update()
            X = 1230
        if Y > 720:
            for bulid in bulids:
                bulid.update()
            Y = 50
        elif Y < 0:
            for bulid in bulids:
                bulid.update()
            Y = 670
        ban.update()
        ban.ndraw()
        ban.bdraw()


        if runch == 1 or 2 or 3 or 4:
            runch = 0
        men.draw()
        boom.draw()
        boom.update()
        update_canvas()


        T -= 5
        ST -= 5
        if ST == 1:
            C += 1

        while (ST < 1 and running == True):

            clear_canvas()

            for floor in floors:
                for floor in floors:
                    floor.draw()
                    floor.update()

            ca.draw()
            npc.draw()
            handle_events(frame_time)
            men.update(frame_time)
            if runch == 1 or 2 or 3 or 4:
                runch = 0
            men.draw()

            ban.update()
            ban.ndraw()
            ban.bdraw()
            update_canvas()
            swap.update()

            delay(0)
        delay(0)



    close_canvas()
if __name__ == '__main__':
    main()


