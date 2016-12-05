
class Swith:
    def __init__(self):
        self.swith = False

    def ch(self):
        if self.swith == False:
            self.swith = True
            return self.swith

    def back(self):
        if self.swith == True:
            self.swith = False


