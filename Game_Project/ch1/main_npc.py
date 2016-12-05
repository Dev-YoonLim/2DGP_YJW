from pico2d import *

class Mnpc:

    def __init__(self):
        self.npcx = 600
        self.npcy = 400
        self.image = load_image('char_in/main_npc_s.png')
        self.textimage = load_image('text/pointch.png')

    def draw(self):
        self.image.draw(self.npcx, self.npcy)
        self.textimage.draw(600, 150)

    def get_bb(self):
        return self.npcx - 15, self.npcy - 15, self.npcx + 15, self.npcy + 15

class Mid_event:
    def __init__(self):
        self.midx = 600
        self.midy = 350
        self.image = load_image('')
