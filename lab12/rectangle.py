class rectangle():
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.S = self.side1 * self.side2
    
    def ploshad(self):
        S = self.S
        return S
    
    def rad_vpis(self):
        if self.side1 == self.side2 :
            return self.side1 / 2
        else:
            return 'B прямоугольник нельзя вписать окружность(('
    
    def rad_opis(self):
        r = ((self.side1)**2 + (self.side2)**2) ** 0.5 / 2
        return r
    

rec1 = rectangle(5, 5)
print(rec1.rad_vpis())