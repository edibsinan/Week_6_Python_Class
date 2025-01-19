class Memur:
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
    
    def tanit(self):
        return f"""
        ismim: {self.ad},
        soyadim: {self.soyad},
        maas: {self.maas}"""

kisi1=Memur("talha","eroglu",3300)

class Yonetici(Memur):
    def __init__(self, ad, soyad, maas):
        # super().__init__(ad, soyad, maas)
        Memur.__init__(self, ad, soyad, maas) #bu sekilde de olabiliri

yonetici1=Yonetici('ali', 'guzel',6000)

class Stajyer(Memur):
    def __init__(self, ad, soyad, maas=1000):
        Memur.__init__(self,ad, soyad,maas)

stajyer1=Stajyer('kadir','yolcu')


print(stajyer1.tanit())
print(kisi1.tanit())
print(yonetici1.tanit())


