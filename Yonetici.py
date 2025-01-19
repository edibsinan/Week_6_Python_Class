
class Yonetici(Memur1):
    def __init__(self,ad, soyad, maas):
        super().__init__(ad, soyad,maas)

yonetici=Yonetici('ali', 'fatura',6000)

yonetici.tanit()