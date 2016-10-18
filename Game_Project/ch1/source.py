import random
from pico2d import *

running = None
runch = 0
X = 640
Y = 360
T = 2200
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
        if SL > 2000:
            L -= 40
            T += 20
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



class Men:

    UP_RUN, RIGHT_RUN, LEFT_RUN, DOWN_RUN, STAND = 0, 1, 2, 3, 5

    def handle_up_run(self):
        global Y
        global ST
        if ST > 1:
            self.y += 13
            Y += 13
        elif ST == 0:
            self.y += 13
            Y += 13
        if self.state == self.UP_RUN and runch == 1:
            self.state = self.LEFT_RUN
        elif self.state == self.UP_RUN and runch == 2:
            self.state = self.RIGHT_RUN
        elif self.state == self.UP_RUN and self.y > 720 and ST == 0:
            self.state = self.DOWN_RUN
        elif self.state == self.UP_RUN and self.y > 720 and ST == 0:
            self.state = self.DOWN_RUN




    def handle_left_run(self):
        global X
        global ST
        if ST > 1:
            self.x -= 13
            X -= 13
        elif ST == 0:
            self.x -= 13
            X -= 13
        if self.state == self.LEFT_RUN and runch == 4:
            self.state = self.DOWN_RUN
        elif self.state == self.LEFT_RUN and runch == 3:
            self.state = self.UP_RUN
        elif self.state == self.LEFT_RUN and self.x < 0 and ST == 0:
            self.state = self.RIGHT_RUN

    def handle_down_run(self):
        global Y
        global ST
        if ST > 1:
            self.y -= 13
            Y -= 13
        elif ST == 0:
            self.y -= 13
            Y -= 13
        if self.state == self.DOWN_RUN and runch == 2:
            self.state = self.RIGHT_RUN
        elif self.state == self.DOWN_RUN and runch == 1:
            self.state = self.LEFT_RUN
        elif self.state == self.DOWN_RUN and self.y < 0 and ST == 0:
            self.state = self.UP_RUN

    def handle_right_run(self):
        global X
        global ST
        if ST > 1:
            self.x += 13
            X += 13
        elif ST == 0:
            self.x += 13
            X += 13
        if self.state == self.RIGHT_RUN and runch == 3:
            self.state = self.UP_RUN
        elif self.state == self.RIGHT_RUN and runch == 4:
            self.state = self.DOWN_RUN
        elif self.state == self.RIGHT_RUN and self.x > 1280 and ST == 0:
            self.state = self.LEFT_RUN

    handle_state = {
        UP_RUN : handle_up_run,
        LEFT_RUN: handle_left_run,
        DOWN_RUN : handle_down_run,
        RIGHT_RUN: handle_right_run,
    }
    def update(self):
        self.frame = (self.frame + 1) % 3
        self.handle_state[self.state](self)

    def draw(self):
        if ST > 1:
            if self.x > 1280:
                self.x = 50
            elif self.x < 0:
                self.x = 1230
            if self.y > 720:
                self.y = 50
            elif self.y < 0:
                self.y = 670
            self.c1image.clip_draw(self.frame * 50, self.state * 47, 50, 43, self.x, self.y)
        elif ST == 0:
            if self.x > 1280:
                self.x = 1230
            elif self.x < 0:
                self.x = 50
            if self.y > 720:
                self.y = 670
            elif self.y < 0:
                self.y = 50
            self.c2image.clip_draw(self.frame * 100, self.state * 95, 100, 85, self.x, self.y)



    def __init__(self):
        self.x = 640
        self.y = 360
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.UP_RUN

        self.c1image = load_image('char_in/men3.png')
        self.c2image = load_image('char_in/men1.png')

class Npc1:

    def __init__(self):
        self.x = 640
        self.y = 400
        self.image = load_image('char_in/npc1.png')

    def draw(self):
        self.image.draw(self.x, self.y)


class Bulid:

    def __init__(self):
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.count = random.randint(0, 100)
        if self.count >= 97:
            self.ju = load_image('ju/red2.png')
        elif self.count > 80 and self.count < 97:
            self.ju = load_image('ju/green2.png')
        elif self.count <= 80:
            self.ju = load_image('ju/blue2.png')
        self.image = load_image('pso/gamok3.png')

    def draw(self):
        self.image.draw(self.bux, self.buy)
        self.ju.draw(self.bux, self.buy-5)

    def update(self):
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.count = random.randint(0, 100)
        if self.count >= 97:
            self.ju = load_image('ju/red2.png')
        elif self.count > 80 and self.count < 97:
            self.ju = load_image('ju/green2.png')
        elif self.count <= 80:
            self.ju = load_image('ju/blue2.png')

class Ca:
    global T
    def __init__(self):
        self.x = 640
        self.y = 600
        self.image = load_image('pso/ca1.png')

    def draw(self):
        self.image.draw(self.x, self.y)


class Floor:
    global mapx, mapy, map

    def __init__(self):
        self.mapx = 50
        self.mapy = 50
        self.image = load_image('floor_in/block2_floor.png')

    def draw(self):
        self.image.draw(self.mapx, self.mapy)

    def update(self):
        self.mapx += 100
        if(self.mapx > 1280):
            self.mapx = 50
            self.mapy += 100
        elif(self.mapy > 720):
            self.mapx = 50
            self.mapy = 50







def handle_events():
    global running
    global runch
    global T, ST
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                if runch == 0:
                    runch = 1
            elif event.key == SDLK_RIGHT:
                if runch == 0:
                    runch = 2
            elif event.key == SDLK_UP:
                if runch == 0:
                    runch = 3
            elif event.key == SDLK_DOWN:
                if runch == 0:
                    runch = 4
            elif event.key == SDLK_SPACE:
                T = 1
                ST = 1


def nmcrush(men, npc):
    left_a, bottom_a, right_a, top_a = men.mcrush()
    left_b, bottom_b, right_b, top_b = npc.ncrush()

    if left_a > right_b: return False
    if right_a > left_b: return False
    if top_a < bottom_b: return False
    if bottom_b > top_b: return False

    return True


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
        handle_events()
        men.update()
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
            handle_events()
            men.update()
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


