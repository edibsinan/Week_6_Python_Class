class Okul:
    def __init__(self, ad, soyad, tel):
        self.ad=ad
        self.soyad=soyad
        self.tel=tel

class Ogrenci(Okul):
    def __init__(self, ad, soyad, tel, not_ort):
        super().__init__(ad, soyad, tel)
        self.not_ort=not_ort
    
    def yazdir(self):
        print(f"""
            AD      ={self.ad}
            SOYAD   ={self.soyad}
            TEL     ={self.tel}
            NOT     ={self.not_ort}
            """)

class Ogretmen(Okul):
    def __init__(self, ad, soyad, tel, maas):
        super().__init__(ad, soyad, tel)
        self.maas=maas
            
    def yazdir(self):
        print(f"""
            AD      ={self.ad}
            SOYAD   ={self.soyad}
            TEL     ={self.tel}
            MAAS    ={self.maas}
            """)


ogrenci1=Ogrenci('ali', 'can', '12345',85)
ogretmen1=Ogretmen('Hasan','Can','98765',3000)

ogrenci1.yazdir()
ogretmen1.yazdir()



