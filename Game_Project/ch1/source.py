import random
from pico2d import *

running = None
runch = 0
X = 640
Y = 360
T = 300


class Men:

    global X, Y, T

    UP_RUN, RIGHT_RUN, LEFT_RUN, DOWN_RUN = 0, 1, 2, 3

    def handle_up_run(self):
        global Y
        global T
        if T > 1:
            self.y += 15
            Y += 15
        elif T == 0:
            self.y += 5
            Y += 5
        if self.state == self.UP_RUN and runch == 1:
            self.state = self.LEFT_RUN
        elif self.state == self.UP_RUN and runch == 2:
            self.state = self.RIGHT_RUN
        elif self.state == self.UP_RUN and Y > 710 and T == 0:
            self.state == self. DOWN_RUN

    def handle_left_run(self):
        global X
        global T
        if T > 1:
            self.x -= 15
            X -= 15
        elif T == 0:
            self.x -= 5
            X -= 5
        if self.state == self.LEFT_RUN and runch == 4:
            self.state = self.DOWN_RUN
        elif self.state == self.LEFT_RUN and runch == 3:
            self.state = self.UP_RUN
        elif self.state == self.UP_RUN and X < 0 and T == 0:
            self.state == self.RIGHT_RUN

    def handle_down_run(self):
        global Y
        global T
        if T > 1:
            self.y -= 15
            Y -= 15
        elif T == 0:
            self.y -= 5
            Y -= 5
        if self.state == self.DOWN_RUN and runch == 2:
            self.state = self.RIGHT_RUN
        elif self.state == self.DOWN_RUN and runch == 1:
            self.state = self.LEFT_RUN
        elif self.state == self.UP_RUN and Y < 0 and T == 0:
            self.state == self.UP_RUN

    def handle_right_run(self):
        global X
        global T
        if T > 1:
            self.x += 15
            X += 15
        elif T == 0:
            self.x += 5
            X += 5
        if self.state == self.RIGHT_RUN and runch == 3:
            self.state = self.UP_RUN
        elif self.state == self.RIGHT_RUN and runch == 4:
            self.state = self.DOWN_RUN
        elif self.state == self.UP_RUN and Y > 1280 and T == 0:
            self.state == self.LEFT_RUN

    handle_state = {
        UP_RUN : handle_up_run,
        LEFT_RUN: handle_left_run,
        DOWN_RUN : handle_down_run,
        RIGHT_RUN: handle_right_run
    }
    def update(self):
        self.frame = (self.frame + 1) % 3
        self.handle_state[self.state](self)

    def draw(self):
        global T
        if T > 1:
            if self.x > 1280:
                self.x = 50
            elif self.x < 0:
                self.x = 1230
            if self.y > 720:
                self.y = 50
            elif self.y < 0:
                self.y = 670
            self.image.clip_draw(self.frame * 100, self.state * 100, 100, 85, self.x, self.y)
        elif T == 0:
            if self.x > 1280:
                self.x = 1230
            elif self.x < 0:
                self.x = 50
            if self.y > 720:
                self.y = 670
            elif self.y < 0:
                self.y = 50
            self.image.clip_draw(self.frame * 100, self.state * 100, 100, 85, self.x, self.y)

    def __init__(self):
        self.x = 640
        self.y = 360
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.UP_RUN

        Men.image = load_image('char_in/men1.png')

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
        self.buy = random.randint(100, 600)
        self.image = load_image('pso/gamok2.png')

    def draw(self):
        self.image.draw(self.bux, self.buy)

    def update(self):
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 600)

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
def main():
    open_canvas(1280, 700)

    floor = Floor()
    floors = [Floor() for i in range(92)]
    floors2 = [Floor() for i in range(4)]

    bulid = Bulid()
    bulids = [Bulid() for i in range(6)]

    ca = Ca()

    men = Men()
    npc = Npc1()

    global runch
    global running
    global X, Y
    global T
    running = True

    while (T >= 1 and running == True):
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
        handle_events()
        men.update()
        if runch == 1 or 2 or 3 or 4:
            runch = 0
        men.draw()
        update_canvas()
        T -= 1
        delay(0)

    while (T < 1 and running == True):
        T == 0
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
        update_canvas()

        delay(0)


    close_canvas()
if __name__ == '__main__':
    main()


