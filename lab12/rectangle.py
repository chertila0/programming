class rectangle():
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.S = self.side1 * self.side2
    
    def ploshad(self):
        S = self.S
        return S
    
    def rad_vpis(self):
        if self.side1 == self.side2 :
            return self.side1 / 2
        else:
            return 'B прямоугольник нельзя вписать окружность и найти её радиус(('
    
    def rad_opis(self):
        R = ((self.side1)**2 + (self.side2)**2) ** 0.5 / 2
        return R
