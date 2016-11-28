from pico2d import *

class Mnpc:

    def __init__(self):
        self.npcx = 600
        self.npcy = 400
        self.image = load_image('char_in/main_npc_s.png')

    def draw(self):
        self.image.draw(self.npcx, self.npcy)

    def get_bb(self):
        return self.npcx - 15, self.npcy - 15, self.npcx + 15, self.npcy + 15