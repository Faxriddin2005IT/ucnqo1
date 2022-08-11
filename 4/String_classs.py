class String:
    def __init__(self,text):
        self.text = text

    def upper(self):
        place = ''
        for i in self.text:
            if ord(i)>91:
                place+=chr(ord(i)-32)
            else:
                place+=i
        return place

    def lower(self):
        place = ''
        for i in self.text:
            if ord(i)<91:
                place+=chr(ord(i)+32)
            else:
                place+=i
        return place
    def replace(self,old,new):
        place=''
        for i in self.text:
            if old in i:
                place+=new
            else:
                place+=i
        return place
    def join(self,txt):
        place = ''
        for i in self.text:
            place+=i
            place+=txt
        return place[0:-1]
    def capitalize(self):
        place = ''
        for i in self.text:
            if ord(i)>91:
                place+=chr(ord(self.text[0] -32))
            else:
                place+=chr(ord(self.text[0]+32))
                place+=chr(ord(i)+32)


txt1 = String('assalom')
print(txt1.capitalize())