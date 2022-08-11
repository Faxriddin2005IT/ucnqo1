# class Talaba:
#     def __init__(self,ism:str,familiya:str,age:int,lavel:int):
#         self.name1 = ism
#         self.surname1 = familiya
#         self.age1 = age
#         self.lavel1 = lavel
#
#     def name(self):
#         return f'ism:{self.name1}'
#     def surname(self):
#         return f'ism:{self.surname1}'
#     def age(self):
#         return f'ism:{self.age1}'
#     def lavel(self):
#         return f'ism:{self.lavel1}'
#
# talaba1 = Talaba('Faxriddin','Urinboyev',16,3)
# print(talaba1.name())


# class Cal:
#     def __init__(self,a:int,b:int):
#         self.a = a
#         self.b = b
#
#     def hisob(self,amal):
#         if amal=='+':
#             return f'add:{self.a+self.b}'
#         elif amal=='-':
#             return f'ayirish:{self.a - self.b}'
#         elif amal=='*':
#             return f'kopaytirish:{self.a * self.b}'
#         elif amal=='/':
#             return f'bolish:{self.a / self.b}'
# qiymat1 = Cal(50,10)
# print(qiymat1.hisob('/'))


# class Mevalar:
#     def __init__(self,*args):
#         self.a = args
#     def hisob(self):
#         fruits = []
#         fruits.append(self.a)
#         a = list(filter(lambda x: True if x[0] == 'o' else False, fruits))
#         return a
#
#
# meva = Mevalar('olma','banan','tarvuz','olcha')
# print(meva.hisob())