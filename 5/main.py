# class one:
#     def salom1(self):
#         print('salom')
# class two(one):
#     def salom2(self):
#         print('salom2')
#
# obj1 = two()
# obj1.salom1()
class Mather:
    mathername = ''

    def maser(self):
        print(self.mathername)


class Father:
    fathername = ''

    def father(self):
        print(self.fathername)


class Son(Mather, Father):
    def ism(self):
        print('ota:', self.fathername)
        print('ona:', self.mathername)


obj1 = Son()
obj1.mathername = 'Munojat'
obj1.fathername = 'Baxtiyor'
obj1.ism()



# class Mather:
#     mathername = ''
#
#     def mather(self):
#         print(self.mathername)
#
# class Father:
#     fathername = ''
#
#     def father(self):
#         print(self.fathername)
#
# class Son(Mather, Father):
#
#     def parents(self):
#         print('Father', self.fathername)
#         print('Mather', self.mathername)
#
# son = Son()
# son.mathername = "Maria"
# son.fathername = "Tom"
# son.parents()


