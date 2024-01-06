class Player:
    def __init__(self, name, heart):
        self.name = name
        self.heart = heart
        self.maxheart = heart
        self.isSelect = False

    def getName(self):
        return self.name
    def getHeart(self):
        return self.heart
    def isSelected(self):
        return self.isSelect
    def setSelect(self, value):
        self.isSelect = value
    def subtractHeart(self):
        self.heart -= 1