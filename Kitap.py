class Kitap:
    dil = "Turkce"

    def __init__(self, baslik, yazar, sayfa_sayisi):
        self.baslik = baslik
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi

    def yazdir(self):
        print(f"""
        KITAP ADI       : {self.baslik}
        YAZAR ADI       : {self.yazar}
        SAYFA SAYISI    : {self.sayfa_sayisi}
        """)

    def sayfa_ekle(self, sayi):
        self.sayfa_sayisi += sayi  


# Test edelim
kitap1 = Kitap("Simyacı", "Paulo Coelho", 184)
kitap1.yazdir()

kitap1.sayfa_ekle(20)  # Sayfa sayısını 20 artırıyoruz
kitap1.yazdir()


#kitap1=Kitap('kader','ahmet',300)
#kitap2=Kitap('gurbet','hasan',200)

#kitap1.sayfa_ekle(10)
#kitap1.yazdir()