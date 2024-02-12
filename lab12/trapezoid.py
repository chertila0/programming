class triangle():
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


    def ploshad(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        S = (p*(p-self.side1)*(p-self.side2)*(p-self.side3)) ** 0.5
        return S
    

    def rad_vpis(self):
        r = ploshad() / p
        return r
    
tri1 = triangle(3,4,5)
print(tri1.rad_vpis())