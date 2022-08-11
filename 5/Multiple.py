class Mather:
    mathername = ''

    def mather(self):
        print(self.mathername)

class Father:
    fathername = ''

    def father(self):
        print(self.fathername)

class Son(Mather, Father):

    def parents(self):
        print('Father', self.fathername)
        print('Mather', self.mathername)

son = Son()
son.mathername = "Maria"
son.fathername = "Tom"
son.parents()
