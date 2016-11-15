from pico2d import *

class Mnpc:

    def __init__(self):
        self.bux = 600
        self.buy = 300
        self.image = load_image('char_in/main_npc_s.png')

    def draw(self):
        self.image.draw(self.bux, self.buy)