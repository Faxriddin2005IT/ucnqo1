# class Talaba:
#     def __init__(self,ism,familiya,tyil):
#         self.ism = 'Faxriddin' if ism == 'Faxriddin' else False
#         self.familiya = familiya
#         self.tyil = int(tyil)
#     def name(self):
#         return self.ism
#     def yosh(self,yil=2022):
#         return yil-self.tyil
#     def tanishtir(self):
#         print(f'isim-sharifim {self.ism},{self.familiya},tugilgan yilim {self.tyil}')
#
# talaba1 = Talaba('Faxriddin','Urinboyev','2005')
# talaba1.tanishtir()


class Talaba:
    def __init__(self, ism, familiya, yosh, ball):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.ball = f'siz {ball} topladingiz va budjed asosida oqishga qabul qilindingiz' if ball > 160 else f'siz {ball} topladingiz va kontrakt asosida oqishga qabul qilindingiz' if ball < 150 and ball > 60 else f'siz {ball} topladingiz va oqishga kira olmadingiz'

    def name(self):
        return self.ism

    def surname(self):
        return self.familiya

    def age(self):
        for i in self.yosh:
           print(i)

    def toplam(self):
        return self.ball


talaba1 = Talaba('Faxriddin', 'Urinboyev', '16', 120)
(talaba1.age())
