import random
from pico2d import *
import men

men = None

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

    def update(self, men):
        self.bux = random.randint(100, 1100)
        self.buy = random.randint(100, 500)
        self.count = random.randint(0, 100)
        if self.count >= 97:
            self.ju = load_image('ju/red2.png')
        elif self.count > 80 and self.count < 97:
            self.ju = load_image('ju/green2.png')
        elif self.count <= 80:
            self.ju = load_image('ju/blue2.png')




