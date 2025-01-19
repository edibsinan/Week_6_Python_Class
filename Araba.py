class Araba:
    marka='MERCEDES'

    def __init__(self, model,renk, yil, km=0):
        self.model=model
        self.renk=renk
        self.yil=yil
        self.km=km

    
    def goster(self):
        print(f"""
            MARKA   ={self.marka}
            MODEL   ={self.model}
            RENK    ={self.renk}
            YIL     ={self.yil}
            KM      ={self.km}
                    """)
    
    def kmEkle(self, eklenen_km):
        if eklenen_km<0:
            print(f"""
            Yanlis giris yaptiniz.
            Lutfen pozitif sayi giriniz
                """)
        else:
            self.km+=eklenen_km


araba1=Araba('A class', 'kirmizi', 2010)

araba1.kmEkle(20000)

araba1.goster()