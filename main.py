#ENCAPSULATION: Membuat class dari entitas

class Makhluk:
    def __init__(self):
        self.stat_makan = 0

    def makan(self):
        self.stat_makan = self.stat_makan + 1

    def bicara(self):
        pass

class Kambing(Makhluk):
    def bicara(self):
        return "Mbek!"

suatu_makhluk = Makhluk()
suatu_makhluk.makan()
suatu_makhluk.makan()

print(suatu_makhluk.stat_makan)
print(suatu_makhluk.bicara())

suatu_kambing = Kambing()
print(suatu_kambing.bicara())

a = suatu_makhluk
print('a', a.bicara())

a = suatu_kambing
print('a', a.bicara())
