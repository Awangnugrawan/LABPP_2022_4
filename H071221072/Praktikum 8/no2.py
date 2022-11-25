class Kubus:
    def __init__(self, lebar, tinggi, panjang, massa,):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
        self.massa = massa
    def setMassa(self, massa):
        self.massa = massa
    def getMassaJenis(self):
        return self.massa / (self.lebar * self.tinggi * self.panjang)
lebar = float(input())
tinggi = float(input())
panjang = int(input())
massa = float(input())

kubus = Kubus(lebar, tinggi, panjang, massa)

kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print("Massa Jenis =", kubus.getMassaJenis())


