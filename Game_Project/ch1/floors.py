from pico2d import *


class Floor:
    global mapx, mapy, map

    def __init__(self):
        self.mapx = 600
        self.mapy = 350
        self.image = load_image('floor_in/block3_1_floor.png')
        self.bgm = load_music('sound/main_sound1.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.mapx, self.mapy)
