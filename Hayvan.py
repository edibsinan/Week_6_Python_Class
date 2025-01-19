class Hayvan:
    tur_sayisi=0

    def __init__(self, ad, cins):
        self.ad=ad
        self.cins=cins
        Hayvan.tur_sayisi += 1

hayvan1=Hayvan('leo','aslan')
hayvan2=Hayvan('pamuk','kedi')
print(hayvan1.tur_sayisi)




