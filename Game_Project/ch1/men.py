from pico2d import *
import random

runch = 0

class Men:

    UP_RUN, RIGHT_RUN, LEFT_RUN, DOWN_RUN = 0, 1, 2, 3

    PIXEL_PER_METER = (10.0 / 0.2)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    men_point = 1.0

    def handle_event(self, event):
        global running
        global runch
        #events = get_events()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
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


    def handle_up_run(self, frame_time):
        distance = Men.RUN_SPEED_PPS * frame_time
        self.move = distance
        self.y += self.move
        if self.state == self.UP_RUN and runch == 1:
            self.state = self.LEFT_RUN
        elif self.state == self.UP_RUN and runch == 2:
            self.state = self.RIGHT_RUN




    def handle_left_run(self, frame_time):
        distance = Men.RUN_SPEED_PPS * frame_time
        self.move = distance
        self.x -= self.move
        if self.state == self.LEFT_RUN and runch == 4:
            self.state = self.DOWN_RUN
        elif self.state == self.LEFT_RUN and runch == 3:
            self.state = self.UP_RUN


    def handle_down_run(self, frame_time):
        distance = Men.RUN_SPEED_PPS * frame_time
        self.move = distance
        self.y -= self.move
        if self.state == self.DOWN_RUN and runch == 2:
            self.state = self.RIGHT_RUN
        elif self.state == self.DOWN_RUN and runch == 1:
            self.state = self.LEFT_RUN


    def handle_right_run(self, frame_time):
        distance = Men.RUN_SPEED_PPS * frame_time
        self.move = distance
        self.x += self.move

        if self.state == self.RIGHT_RUN and runch == 3:
            self.state = self.UP_RUN
        elif self.state == self.RIGHT_RUN and runch == 4:
            self.state = self.DOWN_RUN

    handle_state = {
        UP_RUN : handle_up_run,
        LEFT_RUN: handle_left_run,
        DOWN_RUN : handle_down_run,
        RIGHT_RUN: handle_right_run,
    }
    def update(self, frame_time):
        global runch
        self.total_frames += 1.0
        self.frame = (self.frame + 1) % 3
        self.handle_state[self.state](self, frame_time)
        runch = 0


    def draw(self):
        if self.x > 1280:
            self.x = 50
            return True
        elif self.x < 0:
            self.x = 1230
            return True
        if self.y > 720:
            self.y = 50
            return True
        elif self.y < 0:
            self.y = 670
            return True
        self.image.draw(self.x, self.y)
        self.c1image.clip_draw(self.frame * 50, self.state * 47, 50, 43, self.x, self.y)



    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def hit_point(self):
        pass




    def __init__(self):
        self.x = 640
        self.y = 360
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.UP_RUN
        self.total_frames = 0
        self.dir = 1
        self.image = load_image('screen/white.png')
        self.c1image = load_image('char_in/men3.png')