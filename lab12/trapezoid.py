class trapezoid():
    def __init__(self, verhosn, levbok, nizhosn, pravbok):
        self.verhosn = verhosn
        self.levbok = levbok
        self.nizhosn = nizhosn
        self.pravbok = pravbok


    def ploshad(self):
        S = ((self.verhosn + self.nizhosn) / 2) * (self.levbok ** 2 - (((self.nizhosn - self.verhosn)**2 + self.levbok ** 2 - self.pravbok ** 2)/(2*(self.nizhosn - self.verhosn)))) ** 0.5
        return round(S,1)
    

    def rad_vpis(self):
        if (self.levbok + self.pravbok) == (self.verhosn + self.nizhosn):
            r = (self.verhosn * self.nizhosn)**0.5 / 2
            return round(r,1)
        else:
            return 'Суммы противоположных сторон трапеции не равны, нельзя вписать окружность в эту трапецию и найти радиус(('
    
    def rad_opis(self):
        if self.levbok == self.pravbok:
            diag = (self.levbok ** 2 + self.verhosn * self.nizhosn)
            p = (self.levbok + self.verhosn + self.nizhosn)/2
            R = (diag * self.nizhosn * self.levbok) / (4*(p*(p-diag)*(p-self.levbok)*(p-self.nizhosn))**0.5)
            return round(R,1)
        else:
            return 'Окружность можно описать только около равнобедренной трапеции, нельзя описать окружность около этой трапеции и найти радиус('

