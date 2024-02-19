class triangle():
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.p = (self.side1 + self.side2 + self.side3) / 2
        self.S = (self.p*(self.p-self.side1)*(self.p-self.side2)*(self.p-self.side3)) ** 0.5

    def ploshad(self):
        S = self.S
        return round(S,1)
    

    def rad_vpis(self):
        p = self.p
        S = self.S
        r = S / p
        return round(r,1)
    

    def rad_opis(self):
        S = self.S
        R = (self.side1 * self.side2 * self.side3) / (4 * S)
        return round(R,1)


